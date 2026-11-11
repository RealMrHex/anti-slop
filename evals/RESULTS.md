# Results

**Headline, one judge (the project owner), blind:** building new pages, the
skill's page was preferred 10 times of 12 (Run 5, v0.3.0). Refining rough
drafts, 6 of 8, short of the bar set beforehand (Run 6, v0.3.0). Refining
already-designed pages, 0 of 4 on v0.3.0 (Run 7); after reworking refine, 4 of 6
on unseen pages, again short of its bar (Run 8, v0.4.0). One model, one run per
arm; not a general benchmark. Earlier
runs were small and exploratory, and are kept below with their mistakes. All
runs are from 10 November 2026; the newest is first.

**How the runs were done** (Runs 4 and 5 differ where they say so)

- Agent: Claude Sonnet as a sub-agent with file tools. In Runs 1 to 3 it could
  not render pages; in Runs 4 and 5 it could screenshot its work.
- Treatment: told a skill was installed at the repository path and to read
  `SKILL.md` first. This simulates installation; it is not a real skill-loader
  activation.
- Baseline: the same request without the skill and without the skill's name.
- **One run per arm per case.** Agents are stochastic; any difference below may
  be chance.
- **Judged unblinded by the skill's author** (an AI model) who also wrote the
  fixtures. Run 2 outputs were viewed rendered in a browser; no human rated
  anything.

## Run 12: three-way blind test on two third-party example screens (skill v0.8.0, smallest model)

**Result: Anti-Slop was picked as worst on both screens, below no skill. The
other skill was picked as best on both.**

| Screen | Best | Middle | Worst |
|---|---|---|---|
| Landing-page hero | the other skill | no skill | Anti-Slop |
| Dashboard | the other skill | no skill | Anti-Slop |

This is a clear loss on the job the other skill is built for. What the outputs
show, looked at after the picks:

- **Anti-Slop kept the slop palette as "identity".** Both of its runs chose
  elevate mode and kept the violet colour and default typeface, on a product
  whose own name suggests a different colour. The other skill's runs replaced
  the palette with one drawn from the product.
- **It kept the decorative image.** The hero's abstract blob stayed, framed in
  a black box, because v0.4.1 had added a rule that existing images are content
  and must not be replaced. That rule was written for mismatched photographs
  and was too blunt.
- **It did not show the product.** The other skill's hero built an invoice in
  code and put it in the main area; Anti-Slop's hero had the blob.
- **It chose the wrong mode.** The request said the page looked AI-generated,
  which the workflow's own table maps to reinvent; the small model picked
  elevate anyway. The mode system asks for more judgment than it should.
- On the dashboard, two cards were stretched tall around a single number,
  leaving empty space, and a greeting line and a bare percentage were kept.

Changes made in response (v0.9.0, see below) have not been judged.

- Two deliberately AI-looking screens for a fictional invoicing product (a
  landing-page hero and a dashboard), published as before-examples by the other
  skill used in Run 10. Each was fixed three times by the smallest model: with
  no skill, with Anti-Slop v0.8.0, and with that other skill. One run each,
  unattended, all able to screenshot. Same request wording in every arm.
- This is the other skill's home ground: these are its own showcase inputs, and
  its files include reference images of finished versions of them. Anti-Slop
  had not seen them.
- The pages are kept out of the repository because they are third-party
  material; the blind page was served locally. Judge: the project owner,
  picking best and worst.

## Run 11: three-way blind test repeated on a stronger model (skill v0.8.0)

**Result: Anti-Slop was picked as worst on both prompts.**

| Prompt | Best | Middle | Worst |
|---|---|---|---|
| MetricFlow dashboard | the other skill | no skill | Anti-Slop |
| Atmos weather homepage | no skill | the other skill | Anti-Slop |

On a strong model, for building from a detailed brief, this skill made the
result worse than using no skill at all, on both prompts. That confirms the
owner's report that prompted Run 10. With Run 10 it gives a consistent picture:
on the smallest model the skill beat no skill; on a strong model it lost to it.

What the outputs show, looked at after the picks. On the strong model every
arm produced a competent page; the differences are of taste and finish, not
of defects.

- The v0.8.0 instruction to name the default and replace at least two parts of
  it did what it said: Anti-Slop's pages were the most different from the
  usual (a forest-and-amber dashboard with one large revenue panel; a
  full-bleed sky-blue weather page with an oversized numeral). The owner
  ranked both last. Different was not better.
- The pages the owner preferred were the more restrained ones: neutral
  surfaces, one accent, even composition, small type details.
- Anti-Slop's weather page left a large empty area beside the hero and used
  uppercase wide-tracked labels, which is one of the signs this skill's own
  checklist lists. The create workflow does not read that checklist.

Where this leaves the create workflow: it has lost or tied in every blind
comparison since Run 5, and Run 5 was on a much earlier version and on short
prompts. It should not be described as improving output on capable models.
The other skill differs in kind: it prescribes one specific visual language
with exact values, where this one asks the model to exercise judgment without
a house style. On this owner's taste and these prompts, the prescriptive
approach did better. Whether to adopt a house style is a product decision that
contradicts this project's original brief, and has not been made.

- Identical to Run 10 (the two detailed build prompts, three arms, one run
  each) but on Claude Opus instead of the smallest model, to test whether the
  skill helps a strong model or only constrains it.
- Outputs in [`runs/2026-11-10-three-way-strong/`](runs/2026-11-10-three-way-strong/index.html).
  Judge: the project owner, picking best and worst.

## Run 10: three-way blind test on the smallest model (skill v0.8.0)

**Result (owner's blind picks, two prompts):**

| Prompt | Best | Middle | Worst |
|---|---|---|---|
| MetricFlow dashboard | the other skill | Anti-Slop | no skill |
| Atmos weather homepage | Anti-Slop | the other skill | no skill |

On both prompts the no-skill page was picked as worst, and the two skills split
the best picks one each. Two prompts, one run each, one judge: this shows
nothing about which skill is better, and only hints that on the smallest model
either skill beats none.

It also sits oddly beside the owner's report that prompted the run (no skill
doing better in their own use). The likeliest reconciliation is the model:
this run used the smallest model, where guidance has the most to add, and the
owner's runs may have used a stronger one, where the same guidance mostly
constrains. That fits the research finding in `references/findings.md` that AI
assistance helps the least capable most. It was not tested here; the same
three-way comparison on a stronger model would settle it.

Prompted by the owner's report that, in their own use, output with skills
turned off was better and more creative than output with this skill.

- The two detailed prompts from Run 9 (MetricFlow dashboard, Atmos weather
  homepage), each built three times by the smallest available model (Claude
  Haiku): with no skill, with Anti-Slop v0.8.0, and with another publicly
  available skill aimed at the same problem. One run each; all arms could
  screenshot their work; skill arms were told to run unattended.
- The other skill is designed for improving existing screens, not building new
  ones, and it relies on image generation for some results, which was not
  available. It is being used here outside its main purpose.
- Outputs in [`runs/2026-11-10-three-way/`](runs/2026-11-10-three-way/index.html),
  three unlabelled options per prompt in random order. Judge: the project
  owner, picking best and worst.
- Two prompts cannot establish a ranking. This is a look, to be followed by a
  larger test if it shows a pattern.

## Run 9: detailed prompts showed no difference; a fix, checked once (v0.7.0, then v0.8.0)

**Reported by the project owner:** on two long, fully specified build prompts (a
"MetricFlow" SaaS analytics dashboard and an "Atmos" weather homepage, each
listing every required section, the data, and the tech stack), output with and
without the skill looked the same.

**Reproduced.** Both prompts were run verbatim with and without the skill
(v0.7.0), one run each, same model, both able to screenshot. The author viewed
all four rendered, unblinded. The pairs were near-identical: for MetricFlow,
both had a dark sidebar, a teal accent, four equal KPI cards, a revenue chart
beside a traffic panel, and a greeting; for Atmos, both had city chips, a large
hero card with the temperature, an hourly strip of tiles, and the same sections
in the same order. The skill's MetricFlow page also had two faults the baseline
did not: trend lines spilling outside their cards, and a chart total that
disagreed with the revenue figure.

**Cause, as far as can be told.** A detailed brief dictates the structure, which
was where the create workflow made its difference; the skill rated dashboards as
low-boldness and told the agent to keep structure conventional, which is what
the plain agent does anyway; and the earlier create result (Run 5) used short,
open prompts. It is also possible that in the owner's own runs the skill was not
loaded at all, since the prompts do not name it; that was not checked.

**Change (v0.8.0).** `workflows/create.md` step 2 now has the agent write down
the default version of the screen (palette, typeface, layout, focal element),
then replace at least two of those with something from the product, and says
where the difference must come from when the brief fixes the sections
(identity, hierarchy among the required pieces, how the main element is drawn,
content, finish). Step 6 adds checks that the result can be told apart from the
default, that numbers agree, and that nothing spills out of its container.
`references/craft.md` gains a short section on why the first idea is the common
one.

**Rerun on v0.8.0, one run per prompt.** Both results are visibly different
from the baseline and from the v0.7.0 output:

- MetricFlow: total revenue is a large dark panel containing the 12-month
  chart; the other three KPIs are a quieter strip beneath it; forest and lime
  palette with a display typeface.
- Atmos: light theme, a very large heavy temperature numeral, the next 24 hours
  drawn as a temperature curve instead of tiles, weather details as a list with
  plain-language notes, a daylight arc.

Caveats: both rerun agents were cut off by a usage limit after writing a
complete page but before finishing their own checks, so the pages are less
polished than they would have been. Faults seen: the MetricFlow revenue panel
is labelled "last 30 days" above a 12-month chart; the Atmos hero has an empty
band above the hourly chart, and its daylight arc renders only partly.
"Visibly different" is the author's unblinded reading of two pages. Whether
different is *better* has not been judged by anyone; the owner's blind pick is
the test that counts. The earlier create result (Run 5) was measured on v0.3.0
and does not carry over to this version.

Pages: [`runs/2026-11-10-detailed-prompts/`](runs/2026-11-10-detailed-prompts/)
(`without.html`, `with-v0.7.0.html`, `with-v0.8.0.html` for each prompt).

## v0.9.0: changes after Run 12, not yet judged

`workflows/refine.md`: a test for whether a page has a real identity (default
purple palettes, default typefaces, glows and glass never count); "looks
AI-generated" always means reinvent; in reinvent, colour and type come from the
product's own world and the old palette is not carried over; a landing page's
main area shows the product, built in code; images of real things are kept but
decorative filler is removed. `references/craft.md`: palette from the product,
no box larger than its content needs, every change figure states its baseline.

These were written after seeing the Run 12 outputs, so the two example screens
are now tuning cases for this skill and cannot serve as a fair test of it.

**Rerun, judged blind by the owner (two-way, Anti-Slop v0.9.0 against the
other skill, smallest model): the other skill was preferred on both screens
again.** The changes fixed the specific faults named above (the palette was
replaced, the filler image removed, the product shown) and still did not close
the gap, even on screens this skill had by then been tuned on.

## v0.7.0: untested changes

Adds `references/findings.md`, a digest of further research findings with their
reach and a list of common design claims that lack support, plus one evidence
line each in `color.md`, `components.md`, and `tells.md`. It is a reference the
agent opens on demand and is not loaded by any workflow by default. **Not
evaluated.**

## v0.6.0: untested changes

Adds `references/striking-or-odd.md` (research on aesthetics and creativity
turned into eight rules and a diagnostic table for telling striking from odd),
a short "Bold without odd" section in `references/craft.md`, and pointers from
the entry point and the refine workflow. **None of it has been evaluated.**

One thing to watch when it is: craft.md is read by the create workflow, whose
10-of-12 result was obtained on v0.3.0. The new section tells agents to keep
page structure conventional and concentrate novelty in the focal layer. That
could make create outputs better or blander. It needs a retest before the
earlier create result can be claimed for this version.

## v0.5.0: untested changes

After Run 8 the skill was extended, with no test runs because of usage limits.
**Nothing in this section has been evaluated.**

- `references/tells.md`: an evidence-tagged checklist of reported signs of
  AI-made UI, with a section on the newer "tasteful default".
- `references/values.md`: concrete starting numbers, each tagged with its basis.
- `workflows/refine.md`: now audit, triage, a direction confirmed with the user
  before editing, then the screen worked through in layers.
- The create workflow, which is the only part with a result that met its bar,
  was deliberately left almost unchanged.

## Run 8: blind A/B on refine after reworking it (skill v0.4.0)

**Result on the six new pages: skill preferred on 4, baseline on 2, no ties.
The bar set beforehand (at most one loss) was not met.** Better than Run 7's
0 of 4, but 4 or more of 6 would happen by chance about a third of the time.
On the two tuned-on pages the result was one each.

| Page | Request | Set | Owner preferred |
|---|---|---|---|
| Fernhaus landing page | refine | new | without skill |
| Castline dashboard | a lot better | new | with skill |
| Saltwick recipe home | refine | new | with skill |
| Kiln Street booking | a lot better | new | without skill |
| Ledgerly dashboard | refine | new | with skill |
| Marlow & Finch home | a lot better | new | with skill |
| Atmos | refine | tuned on | with skill |
| MetricFlow | a lot better | tuned on | without skill |

Notes written after the picks:

- **Seeded faults:** Castline had a wrong canvas id that stopped its script
  (blank charts, dead range buttons); Saltwick had a wrong selector that left
  its category filters dead. Both arms found and fixed both. On MetricFlow the
  skill run fixed the chart error this time (it had not in Run 7), as did the
  baseline. So the "check that it works" step did what it was for, but the
  plain agent was already doing this on its own when it could read console
  errors, which both arms could in this run and could not easily in Run 7.
- **The two losses on new pages.** On Fernhaus the skill run replaced the
  page's photographs with drawn SVG illustrations because the photos did not
  match their captions; the baseline kept the photos and flagged the mismatch.
  Replacing real imagery with stand-in drawings is overreach the skill does not
  warn against. On Kiln Street both arms made similar improvements; no obvious
  cause.
- **MetricFlow, tuned on.** Told to make it "a lot better", the skill run
  restructured the dashboard around a large revenue hero card; the baseline
  polished the existing layout. The owner preferred the polish. Going further
  is not automatically better on a dashboard.
- **Timidity is reduced but not gone.** Three of the eight skill runs still
  described their work as a light pass because the page "already had a strong
  identity".

After this run, v0.4.1 added two lines to `workflows/refine.md`: existing
imagery is content and must not be replaced with stand-in drawings, and on
dashboards "a lot better" means sharper hierarchy and finish within the layout
unless the structure itself is the problem. **Neither change has been tested.**

**Where refine stands:** rough drafts 6 of 8 (Run 6, v0.3.0); designed pages
0 of 4 on v0.3.0 (Run 7), then 4 of 6 on unseen pages on v0.4.0 (this run).
Neither refine result has met its pre-set bar. Refine is improved and still
unproven.

Changes in v0.4.0, made in response to Run 7: `workflows/refine.md` rewritten
with a "check that it works" step (find the cause of anything blank or broken;
do not blame tooling without evidence), three modes (tune, elevate, reinvent)
with elevate as the default (keep identity, content, and behaviour; improve
hierarchy, layout, components, and finish), scaling to the user's wording, and a
before/after test; `references/core-contract.md` now states that preserving
information architecture does not freeze a screen's layout, that preservation is
not timidity, and that a visible failure is a finding.

Setup:

- Six new, already-designed pages generated for this run by a separate agent
  asked for polished pages with their own identity (plant subscription landing
  page, podcast analytics dashboard, recipe site home, climbing gym booking
  page, budgeting dashboard, bookshop home). None were seen while changing the
  skill. A script fault was seeded into two of them before refining, to test
  the new step; which two is recorded after judging.
- Plus the two owner-supplied pages from Run 7, marked "tuned on", because
  v0.4.0 was written in response to them. They are reported separately.
- Three of the new pages were given "refine", three "make it look a lot
  better". Same agent and model in both arms, one run each, both able to
  screenshot and read console errors.
- Outputs in [`runs/2026-11-10-blind-refine-v4/`](runs/2026-11-10-blind-refine-v4/index.html).
  Judge: the project owner, blind.
- **Bar set before judging, on the six new pages only:** the fix has worked if
  the skill is preferred or tied at least as often as the baseline with at most
  one loss. Preferred on 5 or more of 6 would be a strong result (6 of 6 about
  1.6% by luck, 5 or more about 11%).

## Run 7: blind A/B on refine, two pages supplied by the owner (skill v0.3.0, frozen)

**Result: the skill won none. The owner preferred the baseline's refinement on
both Atmos pairs and called both MetricFlow pairs about the same.** Four pairs
is too few to be conclusive in either direction, but it is the first run on
real, already-designed pages, and the skill did not help on any of them.

| Pair | Owner preferred |
|---|---|
| Atmos, "refine" | without skill |
| Atmos, "make it look a lot better" | without skill |
| MetricFlow, "refine" | about the same |
| MetricFlow, "make it look a lot better" | about the same |

What the transcripts and files show, read after the picks:

- **The skill was too timid on designed pages.** In all four skill runs the
  agent saw an existing type and colour system, chose "tune" mode, and made
  small edits, including when the request was "make it look a lot better". On
  Atmos it noticed that the brand name appeared twice and that the current
  temperature, the thing people open a weather page for, was buried, and then
  left both alone because fixing them "changes the page structure". The
  baseline restructured the hero around the temperature.
- **The skill missed a functional bug the baseline fixed.** MetricFlow's two
  charts never draw: a tick callback reads a variable before it is assigned and
  throws. Both baseline runs found and fixed it. Both skill runs saw blank
  charts in their screenshots and put it down to the headless browser. (The
  skill's author made the same wrong assumption while the runs were in
  progress.) The skill says nothing about checking that a page works before
  polishing it.
- This is the same over-preservation failure as Run 2, in a subtler form: the
  v0.1.1 fix stopped the skill from protecting template defaults, but it still
  treats "this page has a design system" as "only small changes are allowed".

**Taken together, Runs 5 to 7:** preferred on create (10 of 12), favourable but
unproven on refining rough drafts (6 of 8), and no better than, or worse than,
the plain agent on refining already-designed pages (0 of 4, 2 losses). The
refine workflow should not be relied on for designed pages in v0.3.0.

- Two existing pages supplied by the project owner: "Atmos" (a weather home
  page) and "MetricFlow" (an analytics dashboard). Unlike Run 6's rough drafts,
  both are already designed, with their own typefaces, palettes, and
  components, and load Tailwind, fonts, Chart.js, and images from CDNs.
- Each page was refined under two requests ("refine" and "make it look a lot
  better"), each with and without the skill, from identical copies: four pairs,
  eight runs, one run each. Same agent and model as before; both arms could
  screenshot and iterate. The owner's original files were not modified.
- Outputs in [`runs/2026-11-10-blind-yours/`](runs/2026-11-10-blind-yours/index.html),
  original shown beside A and B, sides randomised, key hidden until all four
  picks are made. Judge: the project owner.
- **Four pairs cannot establish anything on their own**: even 4 of 4 for one
  side would occur by chance about 6% of the time. This run is a look at
  behaviour on real, already-designed pages, which Run 6 did not cover.

## Run 6: blind A/B on refine (skill v0.3.0, frozen)

**Result: the owner preferred the skill's refinement on 6 of 8 pages, the
baseline's on 1, and called 1 about the same.** This falls one short of the bar
set before judging (7 of 8), so by that bar it is **inconclusive**: favourable,
not established. Among the 7 decided pairs, 6 or more for one side would occur
by chance about 6% of the time.

| Page | Owner preferred |
|---|---|
| Dog-walking landing page | with skill |
| To-do app home | with skill |
| Dental clinic contact page | about the same |
| Gym member dashboard | with skill |
| Headphones product page | without skill |
| Banking send-money screen | with skill |
| Travel blog home | with skill |
| Careers page | with skill |

- Eight starting pages, each a deliberately rough first draft written by a
  smaller model (Claude Haiku) told not to spend effort on polish: dog-walking
  landing page, to-do app home, dental clinic contact page, gym member
  dashboard, headphones product page, banking send-money screen, travel blog
  home, careers page. None were used before.
- Each was refined twice by the same agent (Claude Sonnet), with and without
  the skill, from identical copies. Four prompts said "refine"; four said the
  page "looks generic and thrown together; make it look a lot better". Both
  arms could screenshot and iterate.
- Outputs in [`runs/2026-11-10-blind-refine/`](runs/2026-11-10-blind-refine/index.html):
  the original plus the two refinements as A and B, sides randomised, key
  hidden until all eight picks are made. Judge: the project owner.
- **Bar set before judging:** 7 or more of 8 for one side is a strong result
  (about 3.5% by luck); anything less is inconclusive.

What this run cannot show: every starting page is an unstyled rough draft with
no brand or design system, which is the easy case for refine. It does not test
whether the skill respects an existing brand, leaves good pages alone, or
preserves behaviour in a real codebase. Preservation was not checked
mechanically here.

## Run 5: larger blind A/B, twelve unseen tasks (skill v0.3.0, frozen)

**Result: the owner preferred the skill's page on 10 of 12 tasks, the
baseline's on 1, and called 1 about the same.** This meets the bar set before
judging. Counting the tie against the skill, 10 or more of 12 would occur by
chance about 2% of the time; among the 11 decided pairs, 10 or more would occur
about 0.6% of the time.

| Task | Owner preferred |
|---|---|
| Settings page | without skill |
| Kanban board | with skill |
| Recipe detail | with skill |
| Yoga studio landing page | with skill |
| Weather home | with skill |
| Store analytics dashboard | with skill |
| Language-app sign-up | with skill |
| Photographer portfolio | about the same |
| Post-run workout summary | with skill |
| Email inbox | with skill |
| Restaurant menu | with skill |
| Festival event page | with skill |

What this does and does not show:

- It is the first result here that is unlikely to be luck: one person, judging
  blind, on tasks the skill was not tuned on, preferred the skill's output
  clearly more often. Together with the four unseen tasks in Run 4, that is 14
  of 16 unseen tasks.
- It is one judge's taste. Another person might weigh things differently.
- It covers creating new single-page interfaces only, with one model (Claude
  Sonnet), one run per arm, and a simulated skill installation. It says nothing
  about refine or audit, about work inside an existing codebase or design
  system, or about other models and agents.
- The theme confound noted below was not controlled.
- Skill runs cost roughly 1.2 to 1.4 times the tokens and about twice the time
  of baseline runs in this test.

Same method as Run 4, scaled up, with the skill unchanged since Run 4.

- Twelve create tasks, none used in any earlier run or while writing the skill:
  settings page, kanban board, recipe detail, yoga studio landing page, weather
  home, store analytics dashboard, language-app sign-up, photographer
  portfolio, post-run workout summary, email inbox, restaurant menu, music
  festival event page. Six desktop, six phone.
- Same agent and model in both arms, one run each, both able to screenshot and
  iterate. Outputs in [`runs/2026-11-10-blind-12/`](runs/2026-11-10-blind-12/index.html),
  sides randomised, key hidden until all twelve picks are made.
- Judge: the project owner. The skill's author did not view the outputs before
  the picks, beyond an automated check that all 24 load.
- **Bar set before judging:** 10 or more of 12 for one side is a strong result
  (about a 2% chance by luck), 9 is suggestive (about 7%), anything closer is
  inconclusive.

One edit was made to an output before judging: a sample email subject in one
inbox page contained the text "[anti-slop]" (picked up from a folder path),
which could have hinted at the arm; it was replaced with a neutral repository
name. Nothing else was altered.

Known confound: several baseline pages follow the system light/dark setting
while several skill pages are light-only or dark-only, so on a dark-mode
machine the two sides often differ in theme as well as design.

## Run 4: blind A/B judged by the project owner (skill v0.3.0)

**Result: the owner preferred the skill's page on 4 of 6 tasks, the baseline's
on 2, none tied.** With six tasks, four or more preferences for one side would
happen by chance about a third of the time (22 in 64), so this is an
encouraging first signal and not evidence of an effect.

| Task | Set | Owner preferred |
|---|---|---|
| API usage dashboard | tuned on | without skill |
| Teen habit tracker | tuned on | without skill |
| Coffee subscription landing page | new | with skill |
| Music "now playing" screen | new | with skill |
| Team notes pricing page | new | with skill |
| Personal finance home screen | new | with skill |

Notes, written after the picks were in:

- The skill's page was preferred on all four tasks it had never been tuned on
  and lost on the two it had. That argues against the result being an artefact
  of tuning to the test, but four tasks is too few to say more.
- On the two losses, viewed afterwards, the two arms had converged on the same
  kind of design (stat tiles, chart, quota panel, table; ring, streak, habit
  cards, tab bar). The skill no longer produced the stark outputs of v0.1.0
  that prompted this rework. Why the baseline was preferred there is the
  owner's to say; the author's guess, for what it is worth, is that the skill
  versions are slightly busier.
- The complaint that drove this run (the skill making results "weird") did not
  recur in the owner's picks, which is the main thing v0.3.0 was meant to fix.

Why this run exists: after Run 3 the owner still found the skill's outputs
"weird" and less appealing than the baseline's, and questioned the testing.
Both criticisms held. The earlier runs were judged unblinded by the skill's
author, tuned and reported on the same tasks, and forbade agents from looking
at their own pages.

Changes to the skill (v0.3.0): `SKILL.md` and `workflows/create.md` rewritten
and shortened; create now reads two files instead of up to thirteen; the slop
catalog is reserved for audit and refine diagnosis and is not read while
creating, because naming patterns made agents avoid them wholesale;
`references/craft.md` rewritten around appeal and finish, states that familiar
patterns (cards, gradients, rounded corners, emoji, rings) are welcome, and
adds an "odd check"; agents are told to look at the rendered page whenever the
host allows.

Setup:

- Six create tasks. Two were used during tuning (API dashboard, teen habit
  tracker); four are new and were not seen while writing the skill (coffee
  subscription landing page, music "now playing" screen, pricing page,
  personal finance home screen).
- Same agent and model in both arms (Claude Sonnet sub-agent), same prompt
  apart from the skill, one run each.
- Both arms could screenshot their page with headless Chrome and iterate.
  Headless Chrome would not go narrower than about 500px, which affected
  phone-width checks in both arms.
- Outputs are in [`runs/2026-11-10-blind/`](runs/2026-11-10-blind/index.html)
  as `a.html` / `b.html` per task, sides assigned at random. The key is not
  stored in readable form in the repository; the page reveals it after all six
  picks are made.
- Judge: the project owner, picking A, B, or "about the same" per task.
- The skill's author did not view the outputs before building the page, beyond
  an automated check that all twelve load.

Limits that remain: one judge, one run per arm, six tasks, one model, simulated
skill installation. A 6-task preference count cannot distinguish a real effect
from chance unless it is lopsided.

## Run 3: after adding creative direction (skill v0.2.0)

Run 2 showed the skill removing bad choices and adding nothing: the user's
verdict on the result was that the skill "prevents agents from being creative
at all", and the outputs supported that. v0.2.0 adds `references/craft.md`
(ambition levels, starting from an idea, a signature move, expressive levers,
"timid is also generic"), an Ambition section and a "conviction over timidity"
principle in `SKILL.md`, a tune / reinvent-the-visual-layer split in
`workflows/refine.md`, and a "timid default" entry in the slop catalog.

Reruns on v0.2.0, one each, viewed rendered:

| Case | With Anti-Slop 0.2.0 |
|---|---|
| REFINE-01, landing page | Reinvented the visual layer. Idea: "the invoice that chases itself", with tally strokes from the product's name. A sample invoice rendered in the hero with its sent / overdue / reminder / paid timeline, serif display headline with one red italic word, paper ground, mono details. Copy from the two given facts only, marked as draft; invented stats removed; sample invoice labelled as sample. All accessibility defects fixed; ids, routes, and form contract kept. |
| PRES-01, form | Reinvented the visual layer. Idea: a workshop job tag: kraft-paper ground, a tag sheet with a punched hole, dashed tear-lines, mono section numbers, large heavy title. All ids, names, ARIA, handlers, copy, and prices kept; mechanical preservation check passes. |
| CTX-02, article | Idea: the page is built around a section drawing of the wall the essay is about. Headline at about ten times body size, mono credits, marginalia column, full-bleed pull quote. Clearly different from the baseline and from the v0.1.0 output. |
| NOOP-02, dense admin table, "more modern" | Changed nothing; classed it as a low-ambition work surface with a real token system. |

**Contamination, disclosed.** The first v0.2.0 reruns of the landing page and
the form are discarded: `craft.md` at that point contained example ideas for
"an invoicing tool" (a ledger with a paid stamp) and "a bike repair shop" (a
work-order ticket), which are the two fixture products, and both agents
reproduced those examples. The examples were replaced with unrelated products
and a "never reuse one" instruction, and both cases were rerun; the table above
reports the clean reruns. The landing rerun still arrived at "a real invoice in
the hero", which is also the obvious idea for an invoicing product, so that
result cannot be fully separated from the generic "show the thing" guidance.

**Still true:** one run each, judged unblinded by the skill's author, no human
rater. The dashboard and habit-tracker outputs in the gallery are from v0.1.0
and were not rerun. Whether v0.2.0 now over-reaches on pages that have a real
but undocumented brand has not been tested, and is the most likely new failure.

## Run 2: before/after on refine and create (skill v0.1.0, then v0.1.1)

Outputs are saved in [`runs/2026-11-10/`](runs/2026-11-10/index.html): open
`index.html` there (serve the folder over HTTP, or open the files directly) to
see original, without-skill, and with-skill side by side.

| Case | Without skill | With Anti-Slop |
|---|---|---|
| REFINE-01, poor landing page | Rewrote the whole page: new dark theme, new headline, new three-step section, new feature cards. Fixed the accessibility failures. Wrote product claims the user never gave ("in a minute", "polite reminders", reusable invoices, payment status). Looks the most designed of the three. | **v0.1.0 failed this case.** It fixed accessibility and button hierarchy but kept "Supercharge Your Workflow", the invented "10k+ / 99.9% / 24/7" stats, and the purple gradient, treating them as content and brand to preserve. **v0.1.1** (after the fix below): replaced copy using only the two facts given and marked it as a draft, removed the stats, removed gradient text, glass, pill radii and hover scaling, fixed accessibility. Plainer than the baseline; invents nothing. |
| PRES-01, accessible plain form | Restyled into a centred card on a tinted background with a new system font, uppercase accent section labels, green primary button, highlighted radio rows, and a dark theme nobody asked for. All behaviour and ARIA preserved. | CSS-only: heading sizes, label-to-field spacing, 34rem column, one filled primary button with reset demoted. Kept Arial, colours, and markup; listed what it left alone. Same result on v0.1.0 and v0.1.1. |
| CTX-01, API usage dashboard | Four equal stat cards, a stacked bar chart card, a quota card, an endpoint table card. Competent and conventional. | No cards. Opens with a computed sentence naming the endpoint causing most failures; error rate is the largest figure; per-endpoint latency budgets; table sorted worst-first with text status; quota projected to a run-out date. |
| CTX-02, architecture article | Serif text, paper background, rust accent, drop cap, large headline, full-width drawing. | Serif text, paper background, terracotta accent, drop cap, large headline, margin notes, data table; placeholder names labelled as such. **The two are very similar.** |
| CTX-03, teen habit tracker | Purple accent, one rounded card per habit with an emoji tile, progress ring, week strip, floating add button. | One lime block with a large "4 habits left today" and a segment per habit; habits as plain rows grouped Morning / After school / Evening; no cards, no emoji. |

Mechanical checks: every output passed `preserved`; the v0.1.0 landing output
fails the `absent` check added afterwards (placeholder headline and stats still
present); all others pass. No output loads an external resource. No console
errors on the two script-heavy skill outputs.

**What this suggests, with one run each**

- **Create is where the skill changed the outcome.** In two of three create
  tasks the baseline produced the familiar template for its category and the
  skill run produced a structure derived from the task. In the third (the
  article) there was no meaningful difference.
- **The three skill-built pages do not share a look**: dense neutral dashboard,
  serif editorial page, loud lime phone screen. That is the negative-transfer
  check passing once; it needs many more products to mean anything.
- **On refine, the skill is more conservative than the baseline**, which is the
  intent: the baseline replaced the form's typeface, palette, and layout and
  added a dark theme for a request to tidy it; the skill run changed spacing
  and hierarchy only. Whether a user prefers that is a judgment this run cannot
  make. Some will prefer the baseline's bolder restyle.
- **The baseline invents content.** On the landing page it wrote product
  claims and features from nothing. The skill run did not.

**What it exposed in the skill**

- **v0.1.0's preservation contract was too timid** and protected template
  defaults as if they were brand and real copy. Fixed in v0.1.1 by a new
  section in `references/core-contract.md` ("Preservation protects intent, not
  accidents") and two lines in `workflows/refine.md`. After the fix, the
  landing case behaved as intended, and the no-op case (NOOP-02) and the form
  case were rerun to check the fix had not caused over-editing: both were
  unchanged in behaviour. Each of those is a single rerun.
- **The v0.1.1 landing page is honest but bland**: still a centred hero over
  two feature blurbs. The skill removed what was wrong without adding much that
  is specific, because it had only two product facts to work with. A user
  comparing screenshots may well prefer the baseline.
- **Cost:** skill runs read 6 to 13 skill files and took roughly two to four
  times as long as baseline runs, with about 1.4 to 2 times the tokens.
- One skill output (habit tracker) shows a small stray bar above the tab bar at
  phone width; not investigated.

## Run 1: audit, no-op, and scope cases (skill v0.1.0)

**Purpose:** check that the skill routes, loads, and behaves as specified, and
get a first look at whether the cases separate an agent with the skill from the
same agent without it.

5 of 16 cases, source-only judging. The fixtures then still used the skill's earlier name in prompts.

**Outcomes**

| Case | Mechanical checks | Treatment | Baseline |
|---|---|---|---|
| AUDIT-01 (mixed dashboard) | Both pass: fixture unchanged | Found 8 of 8 seeded defects; flagged 0 of 4 decoys as defects | Found 8 of 8 seeded defects; flagged 0 of 4 decoys as defects |
| NOOP-01 (good editorial, "refine") | Both pass: 0 lines changed | Declared no-op with reasons | Declared no-op with reasons |
| NOOP-02 (dense admin table, "more modern") | Both pass: 0 lines changed | Declined to restyle; explained density | Declined to restyle; explained density |
| NOOP-02 rerun, hint comment removed from fixture | Both pass: 0 lines changed | Same | Same |
| PRES-02 (playful brand, "tidy streak spacing") | Both pass: all preserved strings present | Edited only streak spacing, onto existing tokens | Edited only streak spacing, onto existing tokens |

**What this shows**

- **No difference in what happened to the files.** On every case run, the
  baseline agent already behaved well: it left good interfaces alone, stayed in
  scope, kept the brand, and found every seeded defect. On these cases, with
  this model, the skill did not change the outcome.
- **A difference in the audit report's form.** The treatment report followed
  the schema: each finding carried a classification, a confidence level, and an
  evidence class; taste items were in a separate "Preferences" section; there
  were "Could not assess" and "Working well" sections; contrast figures were
  computed (2.7:1 and 3.0:1, matching the fixture's seeded values). The
  baseline report was a flat ranked list of 15 items that mixed defects with
  preferences (for example, card borders being "heavy", and 28px buttons as a
  touch-target issue on a desktop tool) with no confidence levels, and proposed
  a replacement colour with an unverified contrast estimate. Whether the
  structured form is more useful to a reader was not tested.
- **Progressive disclosure worked as intended.** Treatment runs read
  `SKILL.md`, the core contract, one workflow, and one to three references,
  never the whole library.

**Problems the run exposed**

- *In the fixtures:* two fixtures carried CSS comments that gave away the
  answer ("density is deliberate", "do not neutralise"). They were removed
  after the first pass and NOOP-02 was rerun; the result did not change.
- *In the cases:* the no-op and scope cases are too easy for this baseline and
  do not discriminate. Harder cases are needed: larger multi-file projects,
  vaguer and pushier prompts, weaker models, and above all the create cases,
  where default templates are most likely to appear.
- *In the skill's output:* the treatment audit labelled one convention-level
  rule as `[empirical]` and rated an unlabelled icon button "blocker" where
  "major" fits the severity definitions. `workflows/audit.md` was tightened
  afterwards to say the evidence tag must be copied from the rule. That change
  has not been re-tested.
- *Unseeded findings:* both arms reported real issues outside the seeded list
  (no `<main>` landmark, fixed grid columns with no breakpoints). The fixture
  is not as clean as its seeded list implies.

## Not yet run

- Repeat runs of anything. Every result above is n = 1.
- Any human rater or blind comparison.
- Any other model or agent, or a real skill installation.
- `AUDIT-02`, `AUDIT-03`, and the routing-only cases `ROUTE-01` to `ROUTE-05`.
- Larger, multi-file projects with a real design system, which is where the
  design-systems guidance would matter.

## Run 13: ten fresh screens, v0.10.0 against the other skill

**What changed in v0.10.0.** A house standard for small details
(`references/details.md`, adapted in part from the other skill under its
licence), read on every create and refine. Interface
microcopy (punctuation, case, number formats, greeting titles, badges) is now
presentation and may be cleaned. Create no longer asks for two defaults to be
replaced; it asks for the product's own identity on a quiet base.

**Setup.** Ten AI-looking screens written for this run by the smallest model
from short briefs (five landing heroes, five app screens), so neither skill
had seen them and none was tuned against. Each was fixed twice by the same
smallest model with one identical request ("This screen looks AI-generated.
Fix it with the skill. Just do it, don't ask me anything."), once per skill.
Both arms had the same headless screenshot command and no image generation.
One run per arm, no retries, no outputs discarded. Blind page:
`evals/runs/2026-11-10-fresh-round1/`.

**Bar, set before judging.** The owner picks the better fix per screen, blind.
Anti-Slop is "at least level" at 5 or more of 10, counting "same" as half.
Below that, one more round of changes is allowed; if the second round is also
below, the head-to-head is dropped as a goal.

**Result.** The other skill 9, Anti-Slop 1 (Pingly hero). Far below the bar.
The rulebook closed the checklist gaps (no emoji, exclamation marks, or
greeting titles in either arm) and did not close the preference gap.

## Run 14: ten more fresh screens, v0.11.0 against the other skill (result pending)

**Diagnosis after Run 13.** Side by side, the two arms had converged on the
same structure. The owner's picks tracked finish: warmer tinted surfaces,
weights of 400 and 500, a serif headline in warm products, line icons kept in
navigation, a small logo mark, and one carefully drawn object. Anti-Slop's
output was colder (white cards on grey), bolder (600 headings), sometimes
stripped to bare text, and used the accent on every repeated link.

**What changed in v0.11.0.** `references/details.md` gained starting values
(neutral ramps with hex values, typeface pairings, a type scale with weights,
layout, radius, icon, depth, and button values; adapted from the other skill's
token reference under its licence) and a "one drawn thing" rule. Repeated links are
no longer accent-coloured; navigation keeps icons; nothing is weight 600.

**Setup.** As Run 13, with ten new screens (five heroes, five app screens)
written after the skill changes were made, so the changes were not tuned on
them. Blind page: `evals/runs/2026-11-10-fresh-round2/`.

**Bar.** Unchanged: 5 of 10 with "same" as half. This is the second and last
round under the stop rule set before Run 13.

**Result.** The other skill 8, Anti-Slop 2 (Loomdesk hero, Readwell
analytics). Below the bar for the second time, so the stop rule applies: no
further head-to-head tuning. The owner asked instead for the other skill's
method to be brought in directly under its licence (v0.12.0, below). That version
has not been blind-tested.


## v0.12.0: the other skill's method adopted for refine (not tested)

After Runs 13 and 14 the owner asked for the other skill to be used directly.
A copy was included under its licence, with the notice that licence requires.
The
refine workflow now runs that method and keeps Anti-Slop's own steps around
it: checking that the page works first, the mode decision, the preservation
and accessibility rules, verification, and the report. Create and audit are
unchanged from v0.11.0.

No blind test was run on v0.12.0. The expectation that refine output now
matches the other skill's is an inference from using the same method, not a
measured result. Across all head-to-head runs recorded here, Anti-Slop's own
refine method lost to it: preferred on 3 of the 20 fresh screens in Runs 13
and 14, and on neither example screen in Run 12 or its rerun.

## Run 15: v0.12.0 against the other skill, same ten screens as Run 14 (result pending)

**Setup.** The ten source screens from Run 14, with both arms run again from
scratch (new outputs on both sides; Run 14's outputs are not reused). Same
smallest model, same request, same screenshot command, one run per arm,
nothing discarded. Anti-Slop's refine now runs the other skill's method, so
the expected result is rough parity, not a win. Blind page:
`evals/runs/2026-11-10-fresh-round3/`.

**Caveat.** The owner has seen these source screens before, though not these
outputs.

**Result.** Anti-Slop 7, the other skill 3 (the other skill preferred on
Brightside hero, Vetline appointments, Stockroom inventory). Above the bar for
the first time.

**How to read it.** Both arms ran the same visual method, so this mainly shows
that Anti-Slop's wrapper no longer costs anything. Seven of ten from one judge
and one run per side is not evidence that it is better: a coin would give 7 or
more about one time in six. The honest summary is "level, possibly ahead".

**Owner's notes.** Where the other skill was better: font choice on
dashboards; a stronger choice of drawn object (a worked calculation on the
maths tutoring hero, where Anti-Slop drew a chart); on Vetline, Anti-Slop's
active-state colours and contrast were wrong; on Stockroom the other skill
was softer and better in type, colour, contrast, and motion. Where Anti-Slop
was better: the Brightside background.


## v0.12.1: finish checks from the Run 15 notes (not tested)

`workflows/refine.md` gained a short list of finish checks taken from the
owner's notes and from looking at the two app screens Anti-Slop lost:
contrast of rendered pairs, quiet and consistent selected states, status
colours kept to dots (Anti-Slop had drawn a schedule strip in five status
hues), accent on the items needing attention, a tinted ramp on dark themes,
a chosen typeface with a mono partner and a logo mark, a drawn object that
shows the product's own act, and motion that is soft rather than absent.
These were written after seeing Run 15's outputs and have not been tested.

## Run 16: v0.12.1 against the other skill, the ten Run 13 screens (result pending)

**Setup.** The ten source screens from Run 13, with both arms run again from
scratch. These were chosen because the v0.12.1 finish checks were written
from Run 15's outputs, which came from the other ten screens. Same smallest
model, same request, same screenshot command, one run per arm, nothing
discarded. Blind page: `evals/runs/2026-11-10-fresh-round4/`.

**Caveat.** The owner has seen these source screens before, though not these
outputs. Both arms use the same visual method, so rough parity is the
expected result.

**Result.** Anti-Slop 7, the other skill 2 (Pingly hero, Sprintly board),
same 1 (Shoply dashboard; the owner clarified this meant "both good, could
not choose", not identical). Above the bar again (7.5 of 10 with "same" as
half).

**Runs 15 and 16 together.** Twenty screens, one fresh run per side each:
Anti-Slop preferred on 14, the other skill on 5, same on 1. With one judge and
both sides using the same visual method, a split this lopsided would come up
by chance about 3 times in 100 if there were no real difference, so it is
suggestive that the wrapper and finish checks help a little, and it is not
proof. It was one model size, one kind of request, and screens the judge had
seen in their unfixed form.

**Things noted in the outputs, not judged.** On Deskwise the Anti-Slop run
edited the text of customer and agent messages (removed emoji and "!!",
reworded a greeting), which goes further than "real content keeps its
meaning" intends. On Stackhost it changed a dark screen to light.


## v0.12.2: two guard rules after Run 16 (not tested)

`workflows/refine.md` now says that text shown as written by a person stays
exactly as written, and that a screen keeps its light or dark theme unless
asked. Both come from the outputs noted under Run 16. Not tested.

## v0.12.3: accent restraint and compactness, after the two Run 16 losses

The owner said the two losses were about how the screens looked, not their
wording. Side by side: on Pingly, Anti-Slop used two loud amber buttons and
an amber chart on a cool ink page, a product panel that ran off the first
screen, and a category label as the headline; the other skill used an
off-white button, almost no accent, a compact panel with a 90-day uptime
strip, and a headline with a point. On Sprintly, Anti-Slop filled a row of
large tiles, the button, and the logo with saturated blue on blue-tinted
greys, with an oversized percentage; the other skill used neutral greys, a
slim one-line progress strip, and small outlined tags.

Two v0.12.1 finish checks had pushed the wrong way ("accent on the primary
action as well", "keep the tint") and were rewritten: the accent is small and
fits the product's temperature, dark themes use an off-white primary button,
work tools use the neutral graphite ramp, meters are thin, tags are outlined,
a hero panel fits the first screen, and the headline makes a point.

## Run 17: v0.12.3 against the other skill, ten new screens (result pending)

**Setup.** Ten screens written for this run after the v0.12.3 changes (five
heroes, five app screens), so nothing was tuned on them and the owner has not
seen them. Same smallest model, same request, same screenshot command, one
run per arm, nothing discarded. Blind page:
`evals/runs/2026-11-10-fresh-round5/`.

**Result.** Anti-Slop 6, the other skill 4 (Notewell hero, Harbor hero,
Innkeeper bookings, Ferry API keys). At the bar, and on its own no different
from a coin toss.

**Runs 15 to 17 together.** Thirty screens: Anti-Slop 20, the other skill 9,
same 1. If the two were equal, a split at least this lopsided would come up
about 3 times in 100. Run 17 is the only one of the three on screens the
owner had never seen, and it is the closest, so the fair summary is: level
with the other skill, probably slightly ahead, and the v0.12.3 changes did
not visibly add to that. The four losses in Run 17 have not been examined.


## v0.12.4: after looking at the four Run 17 losses (not tested)

Side by side:

- **Notewell hero.** Anti-Slop chose cool grey and a plain sans for a product
  about people, centred the hero vertically with empty bands above and below,
  and dropped the page's feature row. The other skill used the warm ramp, a
  serif headline, and kept the three features under the hero.
- **Harbor hero.** Very close. The other skill put a soft mint accent on the
  primary button and gave each feature a title and a sentence; Anti-Slop used
  an off-white button (as v0.12.3 told it to) and label-and-value fragments.
- **Innkeeper bookings.** Nearly the same layout. The other skill had the
  accent on the primary button and on held slots, and set dates and money in
  the interface face; Anti-Slop used an off-white button and set most of the
  table in mono. Anti-Slop also kept a wrong weekday the other skill fixed.
- **Ferry API keys.** Anti-Slop added an invented deliveries chart that
  pushed the real webhook list off the first screen, and its screenshot shows
  content cut off near the bottom (possibly a capture artefact; not confirmed
  in a browser).

So the v0.12.3 rule "dark themes use an off-white primary button" was wrong
for this judge: in two of the four losses the preferred screen had a soft
accent button. What hurt on Pingly in Run 16 was a loud, saturated accent
used three times, not the accent on a button. The rule now says: accent on
the primary button plus a few small marks, in a muted tone on dark themes.
Also added: warm ramp and serif for products about people; mono only for
codes; a hero that starts under the navigation and keeps its supporting row;
a drawn object that never displaces real content; a scroll-to-bottom check
for clipping and a weekday check. None of this is tested.

## Run 18: v0.12.4 against the other skill, ten new screens (result pending)

**Setup.** Ten screens written for this run after the v0.12.4 changes (five
heroes, five app screens), not seen by the owner. Same smallest model, same
request, same screenshot command, one run per arm, nothing discarded. Blind
page: `evals/runs/2026-11-10-fresh-round6/`.

**Result.** Anti-Slop 6, the other skill 4 (Pocketbook hero, Northstar
roadmap, Crewboard notifications, Margin reading list). Same score as Run 17.

**A second judge.** The owner also gave the ten pairs, as left/right
screenshots, to a general-purpose AI model and pasted its verdicts. It did not
know which side was which. It picked Anti-Slop on 5 and the other skill on 5,
agreeing with the owner on 9 of 10 (it preferred the other skill's Hearth &
Pine hero; the owner preferred Anti-Slop's). This is a model's opinion of
screenshots, not a usability test, and it is one more judge, not a panel.

**Runs 15 to 18 together (owner's picks).** Forty screens: Anti-Slop 26, the
other skill 13, same 1. On the twenty screens the owner had never seen (Runs
17 and 18): 12 to 8, which on its own is within chance. The score has not
moved with the changes made since v0.12.0 (7, 7, 6, 6), so the finish checks
added after each round are not shown to help; what the runs support is that
Anti-Slop's refine is level with the other skill, perhaps a little ahead.

**What the second judge said about the four losses.** Pocketbook: Anti-Slop
turned a bright page dark, showed two floating panels where one would do, and
wrote a functional headline where the other named the user's frustration.
Northstar: the other skill added a one-line status bar built from numbers
already on the page; Anti-Slop had declined to add anything. Crewboard: the
other skill grouped the three channel switches in one section and used the
accent for switches that are on; Anti-Slop used three cards and white
switches (its quiet-hours strip was preferred). Margin: the other skill used
the full height with even spacing; Anti-Slop packed the top and left the
bottom empty. On two of Anti-Slop's wins the judge still noted its secondary
text was too faint.


## v0.12.5: small fixes from the Run 18 notes (not tested)

Theme rule tightened (no dark default, no following the system theme);
switches that are on use the accent and related settings share one section; a
one-line drawn element built from existing numbers is expected on app screens
rather than skipped; one panel per hero; sections spaced down the full height;
muted text must still be readable; consumer headlines name the annoyance
removed. Given that four rounds of such changes have not moved the score,
these are recorded as reasonable fixes to observed faults, not as expected
gains.

## v0.13.0: third-party material removed; refine and rulebook rebuilt (not yet tested)

Versions 0.10.0 to 0.12.5 contained material from the other skill, used under
its licence. All of it was removed in v0.13.0: the copied method and its
reference files, and the adapted rulebook. Nothing from it is distributed
with this skill any more.

In its place:

- `references/details.md` was written again from published sources (the
  Tailwind CSS default theme for spacing, colour, type, radius, shadow, and
  timing; Heroicons for icon weight; WCAG 2.2 for contrast and target size)
  and from this project's own blind-test findings in Runs 13 to 18.
- `workflows/refine.md` is Anti-Slop's own procedure again: check that it
  works, choose a mode, audit against `tells.md`, write a brief, rebuild in
  nine layers, verify, report.

**What the earlier results do and do not cover.** Runs 15 to 18 measured a
version that ran the other skill's method. They say nothing about v0.13.0.
Before it is tested, the only head-to-head evidence for Anti-Slop's own
refine method is Runs 13 and 14, which it lost 3 to 17. Run 19 below tests
the rebuild.

## Run 19: v0.13.0 (rebuilt, no third-party material) against the other skill (result pending)

**Setup.** Ten screens written for this run after the rebuild (five heroes,
five app screens), not seen by the owner. Same smallest model, same request,
same screenshot command, one run per arm, nothing discarded. Blind page:
`evals/runs/2026-11-11-fresh-round7/`.

**What it tests.** Whether Anti-Slop's own refine procedure and rebuilt
rulebook hold up against the other skill without borrowing from it. The
earlier own-method runs (13 and 14) were 3 of 20.

**Result.** The other skill 9, Anti-Slop 1 (Tempo hero). The rebuild is
clearly weaker than the other skill for this judge, and no better than
Anti-Slop's own method was in Runs 13 and 14 (3 of 20). Rebuilding the
rulebook from published values and the project's own findings did not
recover what the borrowed method provided.


**What the pairs showed.** Looked at four of the nine losses side by side.
Structure and content were close on both sides. The differences were in
exact values and finish: Anti-Slop's Tailwind-derived greys read colder and
harder (near-black zinc), its 300-step accents read loud on dark, its "paper"
mix came out yellowish, its status dots were more saturated, and its serif
headline was set heavier. The other skill's surfaces, accent tones, and type
weights were softer in each case, and on one hero it drew an illustration
where Anti-Slop drew a data panel. In short, the gap is in tuned values, not
in procedure, and published defaults did not supply them.

## v0.14.0: rebuild withdrawn; the v0.12.5 method restored

After Run 19 the owner chose to go back to the version that had tested well.
v0.14.0 is v0.12.5 again: the refine workflow runs the other skill's method,
which is included in `references/unslop/` under its licence with the notice
that licence requires, and `references/details.md` is the version adapted
from it. The only change from v0.12.5 is that the acknowledgement is kept to
what the licence needs (the notice in that folder, the note at the foot of
`details.md`, and one sentence in the README's licence section) and is no
longer repeated elsewhere.

Runs 15 to 18 describe this version. Run 19 describes the withdrawn rebuild,
which is kept outside the repository for reference.
