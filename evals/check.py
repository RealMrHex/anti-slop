#!/usr/bin/env python3
"""Dependency-free checks for the Anti-Slop skill repository.

  python3 evals/check.py skill
      Validate SKILL.md frontmatter against the Agent Skills spec, resolve every
      relative Markdown link, and validate evals/cases.json against its fixtures.

  python3 evals/check.py output CASE_ID OUTPUT_FILE
      Run the mechanical checks of one eval case against an agent's output file
      (the working copy of the fixture after the run).

These checks show that the repository is well-formed and that an output respects
mechanical constraints. They do not show that any interface got better.
"""
import difflib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EVALS = ROOT / "evals"
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
SPEC_FIELDS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
MECHANICAL = {"fixture_unchanged", "max_changed_lines", "preserved", "absent"}
JUDGED = {"route", "must_find", "must_not_flag", "judge"}


def slug(heading):
    text = re.sub(r"[`*_\[\]()]", "", heading.strip().lower())
    text = re.sub(r"[^\w\- ]", "", text)
    return text.replace(" ", "-")


def anchors(path):
    return {slug(m.group(1)) for m in re.finditer(r"^#{1,6}\s+(.+)$", path.read_text(), re.M)}


def check_frontmatter(errors):
    text = (ROOT / "SKILL.md").read_text()
    match = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not match:
        errors.append("SKILL.md: missing YAML frontmatter")
        return
    top = {}
    for line in match.group(1).splitlines():
        m = re.match(r"^([A-Za-z-]+):\s*(.*)$", line)
        if m:
            top[m.group(1)] = m.group(2).strip()
    for key in top.keys() - SPEC_FIELDS:
        errors.append(f"SKILL.md: frontmatter field '{key}' is not in the Agent Skills spec")
    name = top.get("name", "")
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name) or len(name) > 64:
        errors.append(f"SKILL.md: invalid name '{name}'")
    desc = top.get("description", "")
    if not 1 <= len(desc) <= 1024:
        errors.append(f"SKILL.md: description length {len(desc)} not in 1..1024")
    lines = text.count("\n")
    if lines > 500:
        errors.append(f"SKILL.md: {lines} lines (spec recommends under 500)")
    if ROOT.name != name:
        print(f"note: directory '{ROOT.name}' differs from skill name '{name}'; "
              f"install into a directory named '{name}'")


def check_links(errors):
    files = [p for p in ROOT.rglob("*.md") if ".git" not in p.parts]
    linked = set()
    for path in files:
        for target in LINK.findall(path.read_text()):
            if re.match(r"^[a-z]+:", target):
                continue
            file_part, _, anchor = target.partition("#")
            dest = (path.parent / file_part).resolve() if file_part else path
            if not dest.exists():
                errors.append(f"{path.relative_to(ROOT)}: broken link {target}")
                continue
            linked.add(dest)
            if anchor and dest.suffix == ".md" and anchor not in anchors(dest):
                errors.append(f"{path.relative_to(ROOT)}: missing anchor {target}")
    skill_text = (ROOT / "SKILL.md").read_text()
    for folder in ("references", "workflows"):
        for path in sorted((ROOT / folder).glob("*.md")):
            if f"{folder}/{path.name}" not in skill_text:
                errors.append(f"SKILL.md does not reference {folder}/{path.name}")


def load_cases():
    return json.loads((EVALS / "cases.json").read_text())


def check_cases(errors):
    data = load_cases()
    fixtures = data["fixtures"]
    for name, fx in fixtures.items():
        path = EVALS / fx["file"]
        if not path.exists():
            errors.append(f"cases.json: fixture file missing for '{name}'")
            continue
        text = path.read_text()
        for item in fx["seeded"] + fx["decoys"]:
            if item["locator"] not in text:
                errors.append(f"cases.json: locator for {item['id']} not found in {fx['file']}")
    ids = set()
    for case in data["cases"]:
        cid = case["id"]
        if cid in ids:
            errors.append(f"cases.json: duplicate case id {cid}")
        ids.add(cid)
        fx = fixtures.get(case["fixture"]) if case["fixture"] else None
        if case["fixture"] and fx is None:
            errors.append(f"{cid}: unknown fixture '{case['fixture']}'")
            continue
        known = {i["id"] for i in (fx["seeded"] + fx["decoys"])} if fx else set()
        original = (EVALS / fx["file"]).read_text() if fx else ""
        for check in case["checks"]:
            kind = check["type"]
            if kind not in MECHANICAL | JUDGED:
                errors.append(f"{cid}: unknown check type '{kind}'")
            for ref in check.get("ids", []):
                if ref not in known:
                    errors.append(f"{cid}: unknown seeded/decoy id {ref}")
            if kind == "preserved":
                for s in check["strings"]:
                    if s not in original:
                        errors.append(f"{cid}: 'preserved' string not in original fixture: {s}")
    return data


def cmd_skill():
    errors = []
    check_frontmatter(errors)
    check_links(errors)
    data = check_cases(errors)
    for e in errors:
        print("FAIL", e)
    if not errors:
        print(f"ok: frontmatter, links, {len(data['fixtures'])} fixtures, {len(data['cases'])} cases")
    return 1 if errors else 0


def cmd_output(case_id, output_file):
    data = load_cases()
    case = next((c for c in data["cases"] if c["id"] == case_id), None)
    if case is None:
        print(f"unknown case {case_id}")
        return 2
    output = Path(output_file).read_text()
    original = ""
    if case["fixture"]:
        original = (EVALS / data["fixtures"][case["fixture"]]["file"]).read_text()
    failed = 0
    for check in case["checks"]:
        kind = check["type"]
        if kind in JUDGED:
            print(f"JUDGE  {kind}: {check.get('expect') or check.get('ids') or check.get('criterion')}")
            continue
        if kind == "fixture_unchanged":
            ok, detail = output == original, ""
        elif kind == "max_changed_lines":
            diff = difflib.unified_diff(original.splitlines(), output.splitlines(), lineterm="", n=0)
            changed = sum(1 for l in diff if l[:1] in "+-" and l[:3] not in ("+++", "---"))
            ok, detail = changed <= check["value"], f"{changed} changed, limit {check['value']}"
        elif kind == "preserved":
            missing = [s for s in check["strings"] if s not in output]
            ok, detail = not missing, f"missing: {missing}" if missing else ""
        else:  # absent
            found = [s for s in check["strings"] if s in output]
            ok, detail = not found, f"found: {found}" if found else ""
        failed += not ok
        print(f"{'PASS' if ok else 'FAIL'}   {kind} {detail}".rstrip())
    return 1 if failed else 0


if __name__ == "__main__":
    args = sys.argv[1:]
    if args == ["skill"]:
        sys.exit(cmd_skill())
    if len(args) == 3 and args[0] == "output":
        sys.exit(cmd_output(args[1], args[2]))
    print(__doc__)
    sys.exit(2)
