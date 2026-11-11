# Evidence ledger

Where Anti-Slop's rules come from, how strong each source is, and what was and was
not verified. The skill's references carry short evidence tags; this file is the
long form. It is documentation for maintainers and is not loaded by the agent
during normal use.

The starting point was a commissioned research blueprint (a synthesis with a
source list, an evidence-to-rule table, a draft slop taxonomy, and an evaluation
plan). Its findings were distilled into the references; this ledger records the
sources it named plus the standard HCI sources used to fill gaps.

## Evidence classes

| Tag in references | Class | Meaning |
|---|---|---|
| `[standard]` | Normative standard | WCAG 2.2 success criteria. Binding as accessibility requirements; not themselves empirical claims. |
| `[empirical]` | Peer-reviewed research | Supported by published studies. Scope is limited to what was studied. |
| `[convention]` | Design-system, platform, or craft convention | Widely adopted practice with good rationale. Not proof. |
| `[judgment]` | Engineering hypothesis or preference | Anti-Slop's own heuristics, including the entire slop catalog. |

## Verification status

"Checked" means the source page was fetched during development (November 2026)
and the cited content confirmed. "Not fetched" means the claim rests on the
research blueprint and general knowledge of a well-known source; treat exact
figures with care.

| Source | Class | Used for | Status |
|---|---|---|---|
| W3C, *WCAG 2.2* (Recommendation). https://www.w3.org/TR/WCAG22/ | standard | All `[standard]` rules | **Checked verbatim:** 1.4.1, 1.4.3 (4.5:1; 3:1 large; large = 18pt or 14pt bold), 1.4.8 (80 characters, AAA), 1.4.10 (320 CSS px), 1.4.11 (3:1), 1.4.12 (1.5 / 2 / 0.12 / 0.16). **Checked via summary of the page, not verbatim:** 2.4.7, 2.4.11, 2.4.13 (AAA), 2.5.5 (44px, AAA), 2.5.8 (24px, AA, with exceptions). Other criteria cited by number (1.1.1, 1.3.x, 2.1.x, 2.2.2, 2.3.1, 2.4.x, 2.5.3, 2.5.7, 3.x, 4.1.x) were not individually re-fetched. |
| Agent Skills specification. https://agentskills.io/specification | standard (for packaging) | `SKILL.md` structure, frontmatter, progressive disclosure, size guidance | Checked |
| Si et al., *Design2Code*, NAACL 2025. https://aclanthology.org/2025.naacl-long.199/ | empirical | Models lag in recalling visual elements and generating layout; motivates explicit design guidance | Checked (abstract) |
| Jung, Garcinuno & Mateega, *UI-Bench*, arXiv:2508.20410 | preprint | Precedent for expert pairwise comparison in the eval protocol | Checked (abstract). Preprint, not peer-reviewed. |
| Nielsen, *Response Times: The 3 Important Limits* (from *Usability Engineering*, 1993; citing Miller 1968, Card et al. 1991). https://www.nngroup.com/articles/response-times-3-important-limits/ | convention (with empirical roots) | 0.1 s / 1 s / 10 s guidance in interaction.md | Checked |
| Reinecke et al., *Predicting Users' First Impressions of Website Aesthetics…*, CHI 2013. doi:10.1145/2470654.2481281 | empirical | Visual complexity and colourfulness shape first impressions | **Not fetched** (publisher blocked access). The references therefore state the finding qualitatively and quote no percentage. |
| Abu Doush & Kassem, *Can generative AI create accessible web code?*, 2025. doi:10.1007/s10209-025-01250-2 | empirical | Generated front-end code should not be assumed accessible | **Not fetched** (publisher login wall). Cited from the blueprint only; Anti-Slop relies on it for a cautious stance, not for any figure. |
| Tractinsky, Katz & Ikar, *What is beautiful is usable*, Interacting with Computers, 2000. doi:10.1016/S0953-5438(00)00031-X | empirical | Perceived aesthetics correlates with perceived usability | Not fetched. Well-established; note it concerns *perceived* usability. |
| Lavie & Tractinsky, *Assessing dimensions of perceived visual aesthetics of web sites*, IJHCS, 2004. doi:10.1016/j.ijhcs.2003.09.002 | empirical | Aesthetics is multi-dimensional (classical vs expressive): basis for refusing a single aesthetic score | Not fetched |
| Lindgaard et al., *Attention web designers: You have 50 milliseconds…*, Behaviour & IT, 2006 | empirical | Speed of first impressions | Not fetched; added from general HCI knowledge |
| Gestalt grouping: Wertheimer (1923); Palmer (1992) on common region; Palmer & Rock (1994) on connectedness | empirical | Proximity, similarity, common region rules | Not fetched; textbook material |
| Treisman & Gelade (1980); Ware, *Information Visualization: Perception for Design* (4th ed.) | empirical / expert book | Pre-attentive features, salience, emphasis budget | Not fetched |
| Hick (1952), Hyman (1953); Fitts (1954); Miller (1956) | empirical | Choice and pointing time; the note that "7±2" is about memory span | Not fetched; textbook material |
| Norman, *The Design of Everyday Things* (rev. ed.) | expert book | Signifiers, feedback, mapping | Not fetched |
| Nielsen, *10 Usability Heuristics*; NN/g eye-tracking on F-pattern scanning | convention / empirical | Recognition over recall; scanning | Not fetched |
| Bringhurst, *The Elements of Typographic Style*; Lupton, *Thinking with Type* | expert craft | Measure (45–75 characters), leading, hierarchy | Not fetched. Print-era guidance, applied as ranges. |
| Albers, *Interaction of Color* | expert pedagogy | Colour is relative to context | Not fetched |
| W3C, *CSS Color Module Level 4*. https://www.w3.org/TR/css-color-4/ | web standard | OKLab/OKLCH availability | Not fetched |
| CIE 015:2018 *Colorimetry* | scientific standard | Background for colour-science claims | Not consulted directly; no rule depends on its specifics |
| Ngo, Teo & Byrne, *Modelling interface aesthetics*, 2003 | empirical (limited) | Historical attempt to quantify balance and unity | Not used for any rule: such metrics are not universal, which is why Anti-Slop computes no aesthetic score |
| Apple HIG; Material Design 3; Atlassian Design System; IBM Carbon | convention | Semantic colour, type roles, spacing scales, touch target sizes (44pt / 48dp), dark-theme elevation | Not fetched. Conventions of specific systems, not human constants. |
| WAI-ARIA Authoring Practices Guide | convention | Dialog and widget keyboard patterns | Not fetched |
| Colour vision deficiency prevalence (about 8% of men, 0.5% of women of Northern European descent) | empirical | Motivation for non-colour cues | Not fetched; widely reported figure |

## What people report about AI-made UI (added in v0.5.0)

Used for `references/tells.md`. This is a different kind of evidence from the
table above: mostly practitioner and community reporting, plus one measurement
of prevalence and one perception study. None of it measures harm to users.

| Source | Kind | Used for | Status |
|---|---|---|---|
| Krebs, *Scoring Show HN submissions for AI design patterns*, 20 Apr 2026. https://adriankrebs.ch/blog/design-slop/ | Measurement (blog post, not peer-reviewed) | Prevalence: deterministic CSS/DOM checks via headless browser over 1,590 Show HN landing pages; 22% (347) showed 4+ of 16 patterns, 32% (508) showed 2–3, 46% (735) showed 0–1 | **Checked.** Author estimates 5–10% false positives and says one pattern alone proves nothing. The post does not publish a per-pattern breakdown, so tells.md cites only the totals. |
| Romero, Wiese, Balancieiri, Leal & Guerino, *Usable but Conventional: An Empirical Study on the UX of AI-Generated Interface Prototypes*, arXiv:2605.15124, May 2026 | Empirical study, preprint (accepted for SEMISH 2026) | AI-generated prototypes rated positively on pragmatic quality and neutral to negative on hedonic quality, including originality; 92 participants, UEQ-S, authorship not disclosed to raters | **Checked (abstract only).** No numeric scores in the abstract; prototypes, not shipped products. |
| Practitioner write-ups of "AI tells", including The Fountain Institute's *7 Signs a UI Has Been Vibe Coded*, 925 Studios' *AI Slop Fonts and Gradients*, and similar articles | Reported (practitioner) | The individual signs in tells.md, and the observation that the dominant tell is shifting toward a cream, serif, earthy-accent "tasteful default" | **Seen as search results and summaries, not read in full.** Treated as reports that people notice these signs, nothing more. |
| The origin of the indigo/purple default in a popular UI kit's button colour, and its author's public comment on it (2025) | Reported (widely repeated anecdote) | The "why it happens" note in tells.md | **Not verified against the original post.** Stated in tells.md without names or figures. |
| Sortlist, *AI web design opinion* survey | Survey (vendor) | Not used | **Could not be fetched (403).** Search summaries say respondents often could not tell AI-made from human-made sites; no claim in the skill depends on it. |

What this evidence supports: these signs are common in recent AI-assisted
front ends, people recognise them, and the measured weakness of AI-generated
interfaces is sameness, not unusability. What it does not support: that any
single sign harms users, or that removing them makes a design good.

One finding applies to this skill itself. Reports that the newer tell is a
cream background, serif headline, and earthy accent match what Anti-Slop's own
test outputs looked like in several runs (see `evals/RESULTS.md`). tells.md and
craft.md now warn against it; whether that changes behaviour is untested.

## Aesthetics and creativity research (added in v0.6.0)

Used for `references/striking-or-odd.md`. Status "search summary" means the
finding was confirmed from abstracts, publisher or institutional summaries, or
secondary summaries returned by a search during development; the full text was
not read. Specific figures from these sources are therefore not quoted in the
skill unless noted.

| Source | Class | Used for | Status |
|---|---|---|---|
| Runco & Jaeger, *The Standard Definition of Creativity*, Creativity Research Journal 24(1), 2012 (tracing to Stein, 1953) | empirical (definitional consensus) | Creative = original and effective; "odd" as novelty without fit | Search summary. The definition is widely used and has critics. |
| Reber, Schwarz & Winkielman, *Processing Fluency and Aesthetic Pleasure*, Personality and Social Psychology Review 8(4), 2004 | empirical (review and theory) | Ease of processing feels pleasant; contrast, symmetry, repetition, prototypicality as levers | Search summary. The authors note the theory does not explain the appeal of challenging art. |
| Zajonc, *Attitudinal effects of mere exposure*, 1968 | empirical | Liking grows with exposure; basis for favouring the typical in daily-use tools | Not fetched; textbook material |
| Berlyne, *Aesthetics and Psychobiology*, 1971 | empirical, contested | Preference peaking at moderate novelty and complexity | Search summary. Later work finds the inverted U is not universal. |
| Meyers-Levy & Tybout, *Schema Congruity as a Basis for Product Evaluation*, Journal of Consumer Research 16(1), 1989 | empirical | Moderate mismatch with category expectations rated above exact match and extreme mismatch | Search summary |
| Hekkert, Snelders & van Wieringen, *"Most advanced, yet acceptable"*, British Journal of Psychology 94, 2003 | empirical | Typicality and novelty jointly predict preference and suppress each other; balance differs by product | Search summary. A secondary summary gives 56% of variance explained jointly; not quoted in the skill because the full text was not read. Replications are mixed. |
| Hekkert, *Aesthetic responses to design: a battle of impulses* (Unified Model of Aesthetics), 2014, and follow-up studies | empirical / theory | Unity-in-variety; the reported finding that it is more robust than typicality-novelty | Search summary |
| Tuch, Presslaber, Stöcklin, Opwis & Bargas-Avila, *The role of visual complexity and prototypicality regarding first impression of websites*, IJHCS 70(11), 2012 | empirical | Low complexity and high prototypicality rated most appealing; effects present at 17ms | Search summary (publisher abstract and the authors' institutional summary). 119 screenshots; exposure 17 to 1000ms. |
| Miniukovich, Figl & Ernst, eye-tracking study of prototypicality, aesthetics and complexity, 2024 | empirical, small sample (n = 32) | Typical layouts judged more competent | Search summary |
| Owens et al., Journal of Usability Studies, 2014 | empirical | Non-standard navigation placement: users adapt, gaze does not fully normalise | Search summary |
| von Restorff, 1933 (isolation effect) and later work | empirical | One distinctive item is remembered better | Search summary; later work finds boundary conditions |
| Hassenzahl, *The Thing and I* and related papers, 2003 onward | empirical / model | Pragmatic and hedonic quality as separate dimensions | Search summary |
| Norman, *Emotional Design*, 2004 | expert book | Visceral, behavioural, reflective levels | Not fetched |
| Rams, Tufte, the International Typographic Style, Hara, and other schools named under "lenses" | expert tradition | Offered as positions to borrow, tagged `[judgment]` | Not fetched; no factual claim depends on them |

How this was turned into rules: the eight rules in striking-or-odd.md are this
project's synthesis. No study tests those rules as written, and none of the
underlying research measures outcomes for shipped products. The first rule
(conventional structure and controls, novelty in the focal layer) is an
inference from combining the prototypicality findings with the
typicality-novelty and schema-congruity findings.

## Further findings (added in v0.7.0)

Used for `references/findings.md`. "Search summary" has the same meaning as in
the previous section: confirmed from abstracts, institutional pages, or
secondary summaries returned by a search; full text not read.

| Source | Class | Used for | Status |
|---|---|---|---|
| Reinecke & Gajos, *Quantifying Visual Preferences Around the World*, CHI 2014 | empirical, very large sample | Preferred colourfulness and complexity vary by country, education, gender | Search summary (authors' page). About 2.4 million ratings, nearly 40,000 participants, 430 websites. An age effect reported by a secondary blog was not confirmed and is not used. |
| Fogg et al., *How Do People Evaluate a Web Site's Credibility?*, Stanford / Consumer WebWatch, 2002 | empirical (comment analysis) | "Design look" in 46.1% of credibility comments; experts cite design far less | Search summary (Consumer WebWatch page and press coverage). 2,684 participants. Often cited as 2003 and often misquoted as "75% of users". |
| Bar & Neta, *Humans Prefer Curved Visual Objects*, Psychological Science, 2006; Palumbo et al., 2015 | empirical | Curved contours rated more likeable; threat explanation disputed | Search summary |
| Piepenbrock, Mayr, Mund & Buchner, 2013–2014; Buchner, Mayr & Brandt, 2009; Dobres et al. | empirical | Positive polarity advantage for reading small text; lighting moderates it | Search summary. A claim linking polarity to myopia appeared in one secondary source and is not used. |
| Cleveland & McGill, *Graphical Perception*, JASA, 1984 | empirical, foundational | Accuracy ordering of chart encodings | Search summary; textbook material |
| Bateman et al., *Useful Junk?*, CHI 2010 | empirical, small | Embellished charts: accuracy no worse, recall better | Search summary |
| Borkin et al., *What Makes a Visualization Memorable?*, InfoVis 2013 | empirical, large | Colour, recognisable objects, unusual types raise memorability | Search summary. A secondary source gives 5,693 visualisations; not quoted. Critiqued for equating memorable with effective. |
| Penzo, *Label Placement in Forms*, 2006; later small eye-tracking study | empirical, weak | Top-aligned labels as default | Search summary. Informal method; partly contradicted. Presented in the skill as thin. |
| Pracejus, Olsen & O'Guinn, JCR 2006; follow-ups 2012, 2013 | empirical | Whitespace as a learned, culturally variable signal of prestige | Search summary |
| Larson & Picard, *The Aesthetics of Reading*, 2006 | empirical, small | Typography affects mood and perceived time, not speed | Search summary |
| Doshi & Hauser, *Generative AI enhances individual creativity but reduces the collective diversity of novel content*, Science Advances 10(28), 2024 | empirical | AI assistance and homogenisation | Search summary (dataset record and press release) |
| Jansson & Smith, *Design fixation*, Design Studies 12(1), 1991; Purcell & Gero, 1996 | empirical, mixed | Examples are copied, including flawed features | Search summary of later papers describing the study |
| The golden ratio as an aesthetic preference | claim | Listed under "claims to avoid" | **Not verified in either direction.** Searches returned nothing usable; the skill says only that support was not found. |

## Known limits of the evidence

- **First-impression research is about first impressions.** It does not show
  what serves a daily expert user, and it does not show that less complexity is
  always better.
- **Aesthetics–usability findings are correlations in perception.** They justify
  caring about visual quality; they do not show that polish causes usability.
- **Typographic numbers are ranges from craft tradition**, with mixed
  experimental support for exact optima. The references present them as ranges
  with exceptions.
- **Design-system values are system-specific.** An 8px grid is one system's
  choice, not a perceptual constant.
- **WCAG contrast is a luminance formula**, an imperfect proxy for perceived
  legibility. It is the requirement; it is not a quality measure.
- **The slop catalog has no empirical basis as a taxonomy.** It is a set of
  hypotheses about recurring failure patterns. No study establishes that
  gradients, cards, or rounded corners are harmful in themselves, and the
  catalog does not claim so.
- **No evidence yet shows that this skill improves agent output.** There is
  little published research on text-only design guidance for coding agents;
  most front-end generation benchmarks rely on rendered output, which Anti-Slop
  does not require. Anti-Slop is a testable intervention. See
  [`evals/README.md`](../../evals/README.md) and
  [`evals/RESULTS.md`](../../evals/RESULTS.md).

## Claims deliberately softened or excluded

- A specific share of variance explained by complexity and colourfulness:
  omitted because the paper could not be re-read.
- "Optimal" line length as a single number: replaced by a range and a list of
  text types it does not apply to.
- The "60-30-10" colour split: labelled a folk heuristic.
- "Seven plus or minus two" as a limit on navigation items: named as a
  misapplication.
- All-caps and reading speed, pure-black backgrounds and eye strain: presented
  as conventions, not findings.
- APCA and other alternative contrast models: mentioned as non-normative.
- Any numeric aesthetic score: excluded.

## Licensing

The references are original syntheses. Standards and design-system
documentation are cited and linked, not copied. No book or paper text is
reproduced.
