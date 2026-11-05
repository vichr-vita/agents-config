---
name: handoff
description: Compact the current conversation into a handoff document for another agent to pick up.
argument-hint: "What will the next session be used for?"
disable-model-invocation: true
---

# Handoff

Write a handoff document summarising the current conversation so a fresh agent can continue the work. Save it to the operating system's temporary directory (`$TMPDIR`, else `/tmp`), not the workspace.

Include a `Suggested skills` section listing only relevant skills known to be installed. Omit the section when none apply.

Do not duplicate content already captured in specs, plans, ADRs, issues, commits, or diffs. Reference each artifact by path or URL.

Include current objective, completed work, remaining work, decisions, constraints, blockers, relevant file paths, and verification status.

Redact API keys, passwords, tokens, personally identifiable information, and other sensitive values.

If the user passed arguments, treat them as the next session's focus and tailor the document accordingly.
