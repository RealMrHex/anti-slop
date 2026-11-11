# Evaluating Anti-Slop

Two different questions, kept separate on purpose:

| Question | Answered by | Status |
|---|---|---|
| Is the repository a well-formed skill? | `python3 evals/check.py skill` | Runs locally, no dependencies |
| Does the skill make an agent's UI work better? | Paired behavioural runs in `cases.json`, judged by people | Protocol below; see [RESULTS.md](RESULTS.md) for what has and has not been run |

Passing the first says nothing about the second. A valid `SKILL.md` and
resolving links do not show that any interface improved.

## Repository checks

```bash
python3 evals/check.py skill
```

Validates `SKILL.md` frontmatter against the Agent Skills specification (name
format, description length, spec-only fields, line count), resolves every
relative Markdown link and anchor, confirms `SKILL.md` references every file in
`references/` and `workflows/`, and checks that every seeded defect and decoy in
`cases.json` points at text that exists in its fixture.

## Behavioural cases

[`cases.json`](cases.json) defines fixtures and cases.

**Fixtures** are small self-contained HTML files in `fixtures/`:

| Fixture | Role |
|---|---|
| `slop-landing.html` | Deliberately poor landing page: seeded accessibility failures and generic patterns |
| `mixed-dashboard.html` | Real defects mixed with legitimate choices (dark theme, brand gradient, proper cards) |
| `plain-form.html` | Accessible but unstructured: tests polish without regression |
| `good-editorial.html` | Already good: tests no-op |
| `good-admin-table.html` | Already good and deliberately dense: tests false positives and the "modernise" trap |
| `playful-brand.html` | Loud documented brand with one small real issue: tests style tolerance and scope |

Each fixture lists **seeded** defects (should be found) and **decoys**
(legitimate choices that should not be flagged), each with an evidence class.

**Cases** cover: workflow routing, audit not editing files, preservation,
detection of real problems, false-positive avoidance, no-op on good interfaces,
handling of different visual styles, and context-sensitive creation.

Each case has two kinds of check:

- **Mechanical** (`fixture_unchanged`, `max_changed_lines`, `preserved`,
  `absent`), run by the script.
- **Judged** (`route`, `must_find`, `must_not_flag`, `judge`), answered by a
  human or a separate judge model reading the transcript and output.

### Running a case

1. Copy the fixture to a scratch directory (never run against `fixtures/`
   directly).
2. Start a fresh agent session. **Treatment:** Anti-Slop installed. **Baseline:**
   same agent, model, and settings, skill not installed. For the baseline,
   remove the words "use anti-slop" / "/anti-slop" from the prompt and keep the rest.
3. Give the case's `prompt`, replacing `{file}` with the scratch copy's path (or
   `{outfile}` with a new path for create cases).
4. Save the transcript and the resulting file.
5. Run the mechanical checks:

   ```bash
   python3 evals/check.py output PRES-01 /path/to/scratch/plain-form.html
   ```

6. Judge the remaining checks (the script prints them).

### Judging

- Judge treatment and baseline **blind and in random order** where the check
  compares quality.
- For audits, score against the seeded list: a seeded defect reported is a true
  positive; a decoy reported as a defect is a false positive; report precision
  and recall, not a single score. Findings outside both lists are adjudicated
  individually (the fixtures are not guaranteed free of unseeded problems).
- For create and refine quality, use **pairwise preference** (which of A or B is
  better for this product, on hierarchy, clarity, contextual fit, coherence),
  not absolute ratings. Pairwise judgment avoids inventing a universal
  aesthetic scale.
- If an LLM judge is used, it must be a different session from the generator,
  and its verdicts are a proxy: say so, and spot-check with people.

### What counts as evidence

- One run per case is a smoke test. Agents are stochastic; run each arm several
  times before believing a difference.
- For any public claim that Anti-Slop improves UI quality: 8–12 tasks across at
  least six interface types, the same model and budget in both arms, at least
  five independent raters per pair for formative work (more before publishing),
  a pre-declared analysis, and effect sizes with intervals. These numbers are
  engineering recommendations, not validated thresholds.
- Report failures and regressions alongside wins.

### The experiment that matters most

Negative transfer. Run the three `CTX-*` create cases and compare the treatment
outputs with each other. If a developer dashboard, a magazine article, and a
teenagers' app come out sharing one restrained, "tasteful" look, the skill has
replaced one template with another and has failed, whatever the other cases
say.

Other open questions worth testing: whether naming anti-patterns causes
overcorrection; whether the agent loads the right references; whether
`SKILL.md` alone performs as well as the full library; no-op accuracy on a
larger set of good interfaces.

## Adding a case

When the skill does something wrong in real use, add the smallest fixture that
reproduces it, with the defect seeded or the legitimate choice listed as a
decoy, then a case. Add a positive and a negative together: something that
should be caught, and a look-alike that should be left alone. Run
`python3 evals/check.py skill` to confirm the locators resolve.
