# Project: test-project

<!-- Brief description of the project -->

## Docs Index

| Topic | File | When to read |
|-------|------|-------------|
| Architecture & schema | `docs/ARCHITECTURE.md` | Before writing any code |
| Decision records | `docs/decisions/` | When you need "why" context |

## Rules

- Use type hints on all function signatures
- Run tests: pytest
<!-- Project-specific rules the Agent must follow -->
- Rule 1
- Rule 2
- Every change must have tests

## HANDOFF Protocol

When working on an Issue:
1. Update Issue body status → 🟡 In Progress
2. Implement + test
3. Update Issue body → 🟢 Complete (fill Completed, Decisions Made, Gotchas, Next Session Start Here)

After completing an Issue, update project docs if needed:
- `docs/ARCHITECTURE.md` — new files, commands, schema fields
- `docs/decisions/NNN-topic.md` — new architectural decision (add index row below)
- Known Gotchas below — new pitfalls

## Key Decisions

| # | Topic | File |
|---|-------|------|
<!-- Add rows as decisions are made -->

## Known Gotchas

<!-- Add gotchas discovered during development -->
