# Proposed PR: Specify and Commission Effective BMS HMI Graphics

**Suggested title:** `feat(standard): add BMS HMI graphics specifications and acceptance procedures`

**Destination:** `ACE-IoT-Solutions/corona-digital-cx`.

**Change type:** normative content and reusable evidence templates. Tracking issue: [#1](https://github.com/ACE-IoT-Solutions/corona-digital-cx/issues/1). The proposed requirements are submitted for review and iteration before adoption.

## Problem and Resulting Behavior

Section 5.4 specifies graphics response times but does not establish whether a graphic identifies the correct equipment, communicates trustworthy state, or enables operators to complete their work. A quickly rendered AHU page can still show a stale temperature as current or a fan command as proof.

The new Section 7 requires a controlled task/design basis, instance binding checks, quality and failure indications, command/feedback distinctions, alarm and schedule context, and installed operator task evidence. Acceptance becomes a traceable decision backed by tests, rather than visual preference or a successful screenshot.

## Review of the Reference Material

Reviewed the local `../ace-hmi-primer` README, lessons, glossary, question-bank review material, project checklist, design lab, and browser tests, alongside the enclosed `ANSI+ISA+101.01-2015.pdf`. The primary reference was read locally; its PDF, extracts, and illustrations are excluded from this change. The following observations concern suitability as commissioning evidence, rather than defects in the teaching application's stated scope.

| Finding | Existing evidence | Proposed resolution |
| --- | --- | --- |
| Sound distinction between requirements, guidance, and BMS examples | Primer README; `docs/content-maintenance.md`; `src/data/lessons.ts` | Preserve edition-specific locators and clearly label applied commissioning requirements. |
| Lifecycle/tasks covered, but checklist lacks an executable acceptance package | Primer `src/App.vue` checklist and validation lesson | Stable HMI IDs, acceptance plan, hold points, responsibility assignments, and evidence traceability. |
| Lab distinguishes stale observations and target changes from measured response | Primer `src/lib/lab.ts`, `src/components/DesignLab.vue`, and browser tests | Test actual source bindings, priority arbitration, independent proof, full failure paths, and recovery. |
| Lab uses fixed teaching data and limited scenarios | Primer README and DesignLab | Add reproducible state/failure injections and six task families across in-scope equipment. |
| Application tests exercise teaching behavior | Primer `tests/browser/app.spec.ts` | Keep application regression evidence distinct from installed BMS verification and validation. |
| Graphics performance is already normative here | Corona Section 5.4 | Reuse existing limits; define measurement events and require approved limits for uncovered cases. |

The 2015 ISA edition is the reviewed basis, not a claim about the latest edition. Clauses 4, 5, and 9 contain requirements; clauses 6–8 provide recommendations. Specific BMS stale-data policies, coverage rules, operator sample sizes, timing repetitions, and acceptance criteria are original applied commissioning choices. The proposal does not claim comprehensive ISA conformity.

## Files and Integration

- `standard/sections/07-hmi-graphics-validation/01-overview.md`: scope, basis, verification/validation definitions, roles, and cross-section precedence.
- `standard/sections/07-hmi-graphics-validation/02-specifications.md`: eleven requirements, clause/test matrix, and original AHU example.
- `standard/sections/07-hmi-graphics-validation/03-verification-validation.md`: coverage, ten verification families, six operator scenarios, evidence, defect closure, and acceptance.
- `templates/hmi-test-record.csv` and `templates/hmi-operator-scorecard.csv`: reusable evidence field sets. These are templates, not completed acceptance records.
- Introduction, README, Section 5.4, and template index: scope and discoverability links. Section 5.4's graphics example now uses the Section 7 repetition protocol and illustrative maxima instead of accepting averages; its numeric limits are unchanged.

Numeric-prefix discovery includes Section 7 automatically in the standard build. Contributor proposal notes and CSV templates are outside the compiled normative text; Section 7 itself defines the required record fields.

## Decisions Proposed for Maintainer Review

1. Adopt 100% inventory/configuration/binding inspection, with witnessed source-to-screen checks for all critical/custom cases and representative remaining equipment/template/integration combinations. Common defects expand coverage across affected instances.
2. Require at least two primary operators in total and coverage of every distinct role/context, with a documented staffing concession route. This is practical commissioning coverage, not statistical usability certification.
3. Require at least ten timing runs per applicable configuration/metric, raw results, maximum/median, and no averaging away failed runs. Existing Section 5.4 absolute and load limits remain in force.
4. Require project approval of write/readback, freshness, task, and uncovered graphics-class limits before testing. Section 5.4 currently specifies small graphics up to 20 points and large graphics at 50+ points; 21–49 needs an explicit project limit.
5. Block acceptance for misleading states, wrong destinations, unauthorized writes, failed required tasks, and adopted performance-limit violations. Only nonblocking items may carry a written Owner concession.

These choices should receive independent commissioning/operator review before adoption. The reviewed ISA guidance alone does not establish their universality.

## Validation of This Proposed Change

Checks completed for this local proposal on 2026-11-25:

- `uv run mdoc-validate`: passed; 28 source Markdown files, no reported issues.
- `uv run mdoc-build --pdf --html`: passed; Section 7 follows metadata validation in both outputs.
- HTML and extracted-PDF checks: found all three Section 7 titles, the requirement/test matrix, the final requirement/test/scenario IDs, and the schedule example.
- PDF visual inspection: the requirement matrix and operator-scenario table render within the page and remain readable (pages 88 and 97 of this build).
- Identifier checks: eleven unique requirements, ten verification families, and six scenarios, with matrix references present.
- CSV parsing: both header-only templates parse successfully with 25 distinct fields each.
- `git diff --check`: passed.

On this macOS workstation, the validation/build commands required `DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib` so WeasyPrint could locate already-installed native libraries. No build-tool changes were needed. These checks validate publication structure; they do not execute the proposed field procedures, constitute an independent subject-matter review, or validate an installed BMS.

The tracking issue follows `CONTRIBUTING.md`; publication-check results accompany the PR. Independent clause/commissioning review and operator feedback remain part of review before adoption, including the coverage and sampling decisions above.
