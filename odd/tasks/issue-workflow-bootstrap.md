# GitHub Issue Workflow Bootstrap

## Objective

Add a repository-native YAML Issue Form and the missing labels required to create the approved portfolio issue and submit its PR through the repository's issue-first workflow.

## Problem and Why

The user authorized creating the issue and PR, then explicitly authorized a direct configuration update to `main`. The confirmed GitHub target has no YAML Issue Form and its label inventory lacks `status:approved` and `type:feature`, so the required issue cannot yet be created through the approved workflow.

## Scope and Constraints

- Target: `github.com/antoniodavid/antoniodavid.github.io`, default branch `main`.
- Direct-main authorization: add one `.github/ISSUE_TEMPLATE/portfolio-improvement.yml` file and create labels `status:approved` and `type:feature`.
- Use the `type:feature` default in the form; do not auto-approve all future issues from the form.
- Apply `status:approved` only to the exact user-authorized issue after it is created and read back, following the protected-label action contract.
- Do not change source/UI, CI, PR templates, unrelated labels, or other repository policy. Do not push the portfolio feature branch, open its PR, or merge it as part of this configuration step.
- If direct push is blocked by current target policy, stop; do not bypass protection.

## Route and Checks

- **Route:** delegated direct for the non-mechanical YAML authoring; parent handles target-bound label creation, main-branch update, and read-back.
- **TDD:** strict mode is configured, but this is repository workflow metadata, not application behavior. Validate YAML syntax, GitHub Issue Form schema/required controls, target-host file read-back, and label read-back. No application test or new dependency is planned unless the writer finds an existing relevant harness.
- **Delivery:** explicitly authorized direct update to `main`; Conventional Commit required. This task does not create a PR for the workflow configuration itself.

## Acceptance Criteria

- A valid GitHub YAML Issue Form exists on `main`, with required fields sufficient to describe the portfolio improvement and a default `type:feature` label.
- Labels `status:approved` and `type:feature` exist on the exact target; unrelated labels remain untouched.
- The selected form does not auto-apply `status:approved` to future submissions.
- Target-host read-back confirms the pushed form and labels; no protection bypass is used.

## Tasks

- [x] **POL-01 — Author and validate the Issue Form.** Added the portfolio improvement form with four required textareas and only the `type:feature` label; omitted a title default and `status:approved`. Ruby YAML parsing and independent structural verification passed.
- [ ] **POL-02 — Create the required labels and publish configuration.** Create the two explicitly authorized labels, commit the form/task record to local `main`, push via the authorized SSH remote, and read back both form and labels without bypassing protection.
- [ ] **POL-03 — Resume issue and PR workflow.** Re-run duplicate search, create/read back the authorized issue using the selected YAML form, apply `status:approved` under the exact-number protected-label gate, then resolve issue-link intent and the PR size strategy before publishing.

## Work Unit Evidence

- **POL-01 focused check:** `ruby -e 'require "yaml"; abort unless YAML.load_file(".github/ISSUE_TEMPLATE/portfolio-improvement.yml").is_a?(Hash)'` — passed; independent structural verification — passed. `git diff --check -- .github/ISSUE_TEMPLATE/portfolio-improvement.yml` had no diagnostics (the file was untracked at that time).
- **Runtime harness:** N/A — this change adds GitHub issue metadata, not application behavior or a local runtime boundary.
- **Rollback boundary:** remove `.github/ISSUE_TEMPLATE/portfolio-improvement.yml` and this task record; remove the created labels only if no published issue depends on them.

## Progress and Next Step

Local branch is `main`, tracking `origin/main`. The form exists at `.github/ISSUE_TEMPLATE/portfolio-improvement.yml`; the author and independent read-only verifier confirmed its supported controls, unique IDs, intended label, and no automatic approval/title. Ruby YAML parse passed; `git diff --check` had no diagnostics, though the file was untracked at that point. The two explicitly authorized labels were created and read back with their expected descriptions/colors. No commit or configuration push has occurred yet. Next: commit only the form and task record to local `main`, recheck protection, push over the explicitly authorized SSH remote without bypass, and verify target form/label readback. Latest branch-protection read showed admin enforcement enabled but no required checks, approvals, restrictions, or rulesets; recheck before push.
