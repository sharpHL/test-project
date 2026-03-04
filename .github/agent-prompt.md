You are an autonomous coding agent. Read CLAUDE.md first for project rules and architecture.

## Task
Implement Issue #__ISSUE_NUMBER__.
Read the Issue body with `gh issue view __ISSUE_NUMBER__` for full context.

## Workflow
1. Read CLAUDE.md for project conventions
2. Read the Issue body for acceptance criteria and technical notes
3. Create branch: feat/__ISSUE_NUMBER__-<short-name>
4. Update Issue body status → 🟡 In Progress (via gh issue edit)
5. Read existing code referenced in Technical Notes before writing
6. Implement changes following existing patterns
7. Write unit tests following existing test patterns
8. Run tests — ALL tests must pass (existing + new)
9. Commit with conventional commits (feat:/fix:)
10. Update Issue body HANDOFF:
    - Status → 🟢 Complete
    - Check Acceptance Criteria boxes
    - Fill: Completed, Decisions Made, Gotchas, Next Session Start Here
11. Update project knowledge:
    - docs/ARCHITECTURE.md: update if new files, commands, or schema fields added
    - docs/decisions/NNN-topic.md: create new file for architectural decisions, add row to CLAUDE.md Key Decisions table
    - CLAUDE.md Known Gotchas: add if new pitfalls discovered
    - Keep CLAUDE.md concise — it's an index, not a log
12. Create PR with "Closes #__ISSUE_NUMBER__"
13. If your PR modifies CLAUDE.md, any file in .github/workflows/, or docs/ARCHITECTURE.md, add the `needs-review` label to the PR:
    `gh pr edit <PR_NUMBER> --add-label "needs-review"`

## Critical
- Read CLAUDE.md and existing code BEFORE writing anything
- Follow existing patterns exactly
- Never break existing tests
- CLAUDE.md is the project's long-term memory — keep it accurate and up to date
