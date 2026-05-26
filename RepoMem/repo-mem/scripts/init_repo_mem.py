#!/usr/bin/env python3
"""Initialize RepoMem layout in a target repository."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def config_doc(default_language: str, secondary_languages: list[str], policy: str) -> str:
    secondary = "[]"
    if secondary_languages:
        secondary = "\n" + "\n".join(f"  - {lang}" for lang in secondary_languages)
    return f"""---
default_language: {default_language}
secondary_languages: {secondary}
translation_sync_policy: {policy}
---

# RepoMem Config

This file stores repository-memory configuration facts.
"""


def architecture_index(language: str) -> str:
    if language.startswith("zh"):
        return """---
domain: global
last_reviewed_at:
---

# 架构索引

## Purpose

这份文档是仓库架构的全局导航层，只保留整体结构、domain 导航和跨域关系。

## System Overview

- 在这里描述系统做什么
- 在这里描述主要能力域
- 在这里描述整体组织方式

## Architecture Diagram

```mermaid
flowchart LR
    A[Domain A] --> B[Domain B]
    B --> C[Domain C]
```

## Domain Map

| Domain | Purpose | Related Code Paths | Doc |
| --- | --- | --- | --- |
| example-domain | 描述该 domain 的职责 | `src/example/` | [example-domain](./example-domain.md) |

## Cross-Domain Relationships

- 记录重要跨域依赖、共享抽象和边界关系

## Read Order

- 先读本文件，再读最相关的 domain 文档

## Split Policy

- 全局结构留在这里
- 细节下沉到具体 domain 文档
"""
    return """---
domain: global
last_reviewed_at:
---

# Architecture Index

## Purpose

This file is the global navigation layer for repository architecture.

## System Overview

- Describe what the system does
- Describe the main capability areas
- Describe the overall structure

## Architecture Diagram

```mermaid
flowchart LR
    A[Domain A] --> B[Domain B]
    B --> C[Domain C]
```

## Domain Map

| Domain | Purpose | Related Code Paths | Doc |
| --- | --- | --- | --- |
| example-domain | Describe the domain responsibility | `src/example/` | [example-domain](./example-domain.md) |

## Cross-Domain Relationships

- Record important cross-domain dependencies and boundaries

## Read Order

- Read this file first, then the most relevant domain docs

## Split Policy

- Keep global structure here
- Move details into domain docs
"""


def memory_index(language: str) -> str:
    if language.startswith("zh"):
        return """---
domain: global
last_reviewed_at:
---

# 记忆索引

## Purpose

这份文档是长期记忆的全局导航层，记录跨 domain 的隐性知识、约束和常见误区。

## Global Constraints And Invariants

- 记录跨 domain 有效的全局约束

## Domain Memory Map

| Domain | Focus | Doc |
| --- | --- | --- |
| example-domain | 记录该 domain 的长期记忆 | [example-domain](./example-domain.md) |

## Common Pitfalls And Decisions

- 记录跨 domain 的通用坑和关键决策原因

## Read Order

- 先读本文件，再读最相关的 domain 记忆文档

## Prune And Split Guidance

- 失效内容通过 `prune` 进入建议流程
- 大段混合主题内容通过 `split` 进入建议流程
"""
    return """---
domain: global
last_reviewed_at:
---

# Memory Index

## Purpose

This file is the global navigation layer for long-term repository memory.

## Global Constraints And Invariants

- Record cross-domain constraints here

## Domain Memory Map

| Domain | Focus | Doc |
| --- | --- | --- |
| example-domain | Long-term memory for the domain | [example-domain](./example-domain.md) |

## Common Pitfalls And Decisions

- Record cross-domain pitfalls and key rationale here

## Read Order

- Read this file first, then the most relevant domain memory docs

## Prune And Split Guidance

- Use `prune` for invalid or redundant memory
- Use `split` when one doc mixes too many themes
"""


def version_plan(language: str) -> str:
    if language.startswith("zh"):
        return """# 版本计划

## Current Version

- 当前版本目标写在这里

## Planned Versions

### vNext

- 在这里记录未来版本计划

## Backlog Candidates

- 在这里记录候选项

## Completed Versions Archive Policy

- 已完成版本移入归档，不阻塞当前和未来计划
"""
    return """# Version Plan

## Current Version

- Describe the current active version focus here

## Planned Versions

### vNext

- Record future version plans here

## Backlog Candidates

- Record candidate items here

## Completed Versions Archive Policy

- Move completed versions into archive instead of crowding active planning
"""


def init_frontmatter(slug: str) -> str:
    return "\n".join(
        [
            "---",
            f"slug: {slug}",
            "status: active",
            "updated_at:",
            "task_type: init",
            "---",
        ]
    )


def detect_documentation_sources(repo_root: Path) -> list[str]:
    candidates = [
        repo_root / "README.md",
        *sorted(repo_root.glob("workflow*.md")),
        *sorted(repo_root.glob("analysis*.md")),
        repo_root / "docs" / "RepoMem" / "persist" / "architecture" / "index.md",
        repo_root / "docs" / "RepoMem" / "persist" / "memory" / "index.md",
        repo_root / "docs" / "RepoMem" / "persist" / "version-plan.md",
        repo_root / "docs" / "self" / "persist" / "architecture" / "index.md",
        repo_root / "docs" / "self" / "persist" / "memory" / "index.md",
        repo_root / "docs" / "self" / "persist" / "version-plan.md",
        repo_root / "repo-mem" / "SKILL.md",
    ]
    seen: set[str] = set()
    result: list[str] = []
    for path in candidates:
        if path.exists():
            rel = str(path.relative_to(repo_root))
            if rel not in seen:
                seen.add(rel)
                result.append(rel)
    return result


def init_proposal_doc(language: str, slug: str, doc_sources: list[str]) -> str:
    if language.startswith("zh"):
        summary = [
            init_frontmatter(slug),
            "",
            "# Init Proposal",
            "",
            "## Repository Summary",
            "",
            "- 在这里总结仓库当前目标、主要能力域和文档现状。",
            "",
            "## Detected Documentation Sources",
            "",
        ]
        if doc_sources:
            summary.extend(f"- `{source}`" for source in doc_sources)
        else:
            summary.append("- 未检测到明显的现有文档源。")
        summary.extend(
            [
                "",
                "## Candidate Domains",
                "",
                "- 在这里列出建议初始化的 domain 及理由。",
                "",
                "## Suggested Persistent Layout",
                "",
                "- 在这里列出建议创建的 persist 文档。",
                "",
                "## Migration Suggestions",
                "",
                "- 在这里说明哪些现有文档内容适合迁入长期层。",
                "",
                "## Open Questions",
                "",
                "- 在这里记录需要人确认的问题。",
                "",
                "## Recommended Next Step",
                "",
                "- 在这里给出下一步建议。",
            ]
        )
        return "\n".join(summary) + "\n"
    summary = [
        init_frontmatter(slug),
        "",
        "# Init Proposal",
        "",
        "## Repository Summary",
        "",
        "- Summarize the repository purpose, major capability areas, and current documentation shape here.",
        "",
        "## Detected Documentation Sources",
        "",
    ]
    if doc_sources:
        summary.extend(f"- `{source}`" for source in doc_sources)
    else:
        summary.append("- No obvious documentation sources detected.")
    summary.extend(
        [
            "",
            "## Candidate Domains",
            "",
            "- List suggested initial domains and short reasons here.",
            "",
            "## Suggested Persistent Layout",
            "",
            "- List the suggested persistent docs here.",
            "",
            "## Migration Suggestions",
            "",
            "- Explain which existing content could move into long-term docs.",
            "",
            "## Open Questions",
            "",
            "- Record unresolved questions here.",
            "",
            "## Recommended Next Step",
            "",
            "- Recommend the next human decision or action here.",
        ]
    )
    return "\n".join(summary) + "\n"


def init_conflicts_doc(language: str, slug: str, conflicts: list[dict[str, str]]) -> str:
    lines = [init_frontmatter(slug), "", "# Init Conflicts", ""]
    if language.startswith("zh"):
        lines.extend(
            [
                "## Summary",
                "",
                f"- 本次初始化发现 {len(conflicts)} 项冲突。",
                "",
                "## Conflict Items",
                "",
            ]
        )
        for item in conflicts:
            lines.extend(
                [
                    f"### {item['conflict_id']}",
                    "",
                    f"- target_file: `{item['target_file']}`",
                    f"- conflict_type: `{item['conflict_type']}`",
                    f"- existing_content_summary: {item['existing_content_summary']}",
                    f"- proposed_content_summary: {item['proposed_content_summary']}",
                    "",
                ]
            )
        lines.extend(
            [
                "## Suggested Resolution Options",
                "",
                "- keep existing",
                "- replace with proposed",
                "- merge both",
                "- rewrite manually",
                "",
                "## Human Decisions",
                "",
                "- 逐条按 conflict_id 记录处理意见。",
                "",
                "## Execution Notes",
                "",
                "- AI 根据确认结果执行冲突处理，并在完成后展示 git diff。",
            ]
        )
        return "\n".join(lines) + "\n"
    lines.extend(
        [
            "## Summary",
            "",
            f"- {len(conflicts)} conflicts detected during init apply.",
            "",
            "## Conflict Items",
            "",
        ]
    )
    for item in conflicts:
        lines.extend(
            [
                f"### {item['conflict_id']}",
                "",
                f"- target_file: `{item['target_file']}`",
                f"- conflict_type: `{item['conflict_type']}`",
                f"- existing_content_summary: {item['existing_content_summary']}",
                f"- proposed_content_summary: {item['proposed_content_summary']}",
                "",
            ]
        )
    lines.extend(
        [
            "## Suggested Resolution Options",
            "",
            "- keep existing",
            "- replace with proposed",
            "- merge both",
            "- rewrite manually",
            "",
            "## Human Decisions",
            "",
            "- Record a decision for each conflict_id.",
            "",
            "## Execution Notes",
            "",
            "- Apply confirmed resolutions and then show git diff.",
        ]
    )
    return "\n".join(lines) + "\n"


def temp_doc(kind: str, language: str) -> str:
    is_requirements = kind == "requirements"
    if language.startswith("zh"):
        body = {
            "requirements": "# 需求文档\n\n## 背景\n\n## 目标\n\n## 范围\n\n## 验收标准\n",
            "architecture": "# 临时架构文档\n\n## 当前任务架构变化\n\n## 受影响模块\n\n## 关键结构或流程\n",
            "memory": "# 临时记忆文档\n\n## 新发现的约束\n\n## 新发现的坑\n\n## 决策原因\n",
            "proposal": "# 维护建议\n\n## Summary\n\n## Why This Maintenance Is Needed\n\n## Scope\n\n## Suggested Changes\n\n## Human Review Paths\n\n## Execution Notes\n",
        }[kind]
    else:
        body = {
            "requirements": "# Requirements\n\n## Background\n\n## Goals\n\n## Scope\n\n## Acceptance Criteria\n",
            "architecture": "# Temp Architecture\n\n## Task-Level Architecture Changes\n\n## Affected Areas\n\n## Key Structures Or Flows\n",
            "memory": "# Temp Memory\n\n## New Constraints\n\n## New Pitfalls\n\n## Decision Rationale\n",
            "proposal": "# Maintenance Proposal\n\n## Summary\n\n## Why This Maintenance Is Needed\n\n## Scope\n\n## Suggested Changes\n\n## Human Review Paths\n\n## Execution Notes\n",
        }[kind]
    if kind == "proposal":
        return body
    frontmatter = [
        "---",
        "slug: example-task",
        "status: active",
        "domains:",
        "  - example-domain",
        "updated_at:",
    ]
    if is_requirements:
        frontmatter.append("task_type: feature")
    frontmatter.append("---")
    return "\n".join(frontmatter) + "\n\n" + body


def initialize_standard_layout(base: Path, language: str, secondary_languages: list[str], policy: str) -> None:
    write(base / "persist" / "config.md", config_doc(language, secondary_languages, policy))
    write(base / "persist" / "version-plan.md", version_plan(language))
    write(base / "persist" / "architecture" / "index.md", architecture_index(language))
    write(base / "persist" / "memory" / "index.md", memory_index(language))
    write(base / "temp" / "_template" / "requirements.md", temp_doc("requirements", language))
    write(base / "temp" / "_template" / "architecture.md", temp_doc("architecture", language))
    write(base / "temp" / "_template" / "memory.md", temp_doc("memory", language))
    write(base / "temp" / "_maintenance-template" / "proposal.md", temp_doc("proposal", language))


def analyze_existing_repo(base: Path, repo_root: Path, slug: str, language: str) -> Path:
    proposal_path = base / "temp" / slug / "init-proposal.md"
    doc_sources = detect_documentation_sources(repo_root)
    write(proposal_path, init_proposal_doc(language, slug, doc_sources))
    return proposal_path


def apply_existing_repo(base: Path, slug: str, language: str, secondary_languages: list[str], policy: str) -> tuple[list[Path], list[dict[str, str]], Path | None]:
    slug_dir = base / "temp" / slug
    proposal_path = slug_dir / "init-proposal.md"
    if not proposal_path.exists():
        raise FileNotFoundError(f"Missing init proposal: {proposal_path}")

    targets = {
        base / "persist" / "config.md": config_doc(language, secondary_languages, policy),
        base / "persist" / "version-plan.md": version_plan(language),
        base / "persist" / "architecture" / "index.md": architecture_index(language),
        base / "persist" / "memory" / "index.md": memory_index(language),
    }
    created: list[Path] = []
    conflicts: list[dict[str, str]] = []
    for idx, (path, content) in enumerate(targets.items(), start=1):
        if path.exists():
            conflicts.append(
                {
                    "conflict_id": f"conflict-{idx}",
                    "target_file": str(path.relative_to(base)),
                    "conflict_type": "existing-persistent-doc",
                    "existing_content_summary": "existing persistent content already present",
                    "proposed_content_summary": "init apply would add or reshape baseline RepoMem content",
                }
            )
            continue
        write(path, content)
        created.append(path)

    conflicts_path = None
    if conflicts:
        conflicts_path = slug_dir / "init-conflicts.md"
        write(conflicts_path, init_conflicts_doc(language, slug, conflicts))
    return created, conflicts, conflicts_path


def proposed_persistent_content(base: Path, language: str, secondary_languages: list[str], policy: str) -> dict[str, str]:
    return {
        "persist/config.md": config_doc(language, secondary_languages, policy),
        "persist/version-plan.md": version_plan(language),
        "persist/architecture/index.md": architecture_index(language),
        "persist/memory/index.md": memory_index(language),
    }


def parse_conflict_decisions(conflicts_path: Path) -> dict[str, str]:
    decisions: dict[str, str] = {}
    in_human_decisions = False
    for raw_line in conflicts_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if line.startswith("## "):
            in_human_decisions = line == "## Human Decisions"
            continue
        if not in_human_decisions or not line.startswith("-"):
            continue
        match = re.match(r"-\s*`?(conflict-\d+)`?\s*:\s*(.+)$", line)
        if match:
            decisions[match.group(1)] = match.group(2).strip()
    return decisions


def resolve_existing_conflicts(base: Path, slug: str, language: str, secondary_languages: list[str], policy: str) -> tuple[list[Path], list[str]]:
    slug_dir = base / "temp" / slug
    conflicts_path = slug_dir / "init-conflicts.md"
    if not conflicts_path.exists():
        raise FileNotFoundError(f"Missing init conflicts: {conflicts_path}")

    decisions = parse_conflict_decisions(conflicts_path)
    proposed = proposed_persistent_content(base, language, secondary_languages, policy)
    updated: list[Path] = []
    skipped: list[str] = []

    for conflict_id, decision in decisions.items():
        match = re.match(r"(keep existing|replace with proposed|merge both|rewrite manually)", decision)
        normalized = match.group(1) if match else decision
        # Find target file by scanning conflict section lines.
        target_file = None
        lines = conflicts_path.read_text(encoding="utf-8").splitlines()
        for idx, line in enumerate(lines):
            if line.strip() == f"### {conflict_id}":
                for candidate in lines[idx + 1 : idx + 6]:
                    candidate = candidate.strip()
                    if candidate.startswith("- target_file:"):
                        target_file = candidate.split("`", 2)[1]
                        break
                break
        if target_file is None:
            skipped.append(conflict_id)
            continue

        target_path = base / target_file
        if normalized == "keep existing":
            skipped.append(conflict_id)
            continue
        if normalized == "replace with proposed":
            proposed_content = proposed.get(target_file)
            if proposed_content is None:
                skipped.append(conflict_id)
                continue
            write(target_path, proposed_content)
            updated.append(target_path)
            continue
        if normalized == "merge both":
            proposed_content = proposed.get(target_file)
            if proposed_content is None:
                skipped.append(conflict_id)
                continue
            existing = target_path.read_text(encoding="utf-8") if target_path.exists() else ""
            merged = existing.rstrip() + "\n\n## RepoMem Proposed Merge\n\n" + proposed_content.rstrip() + "\n"
            write(target_path, merged)
            updated.append(target_path)
            continue
        skipped.append(conflict_id)

    return updated, skipped


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("repo_root")
    parser.add_argument("--default-language", default="en")
    parser.add_argument("--secondary-language", action="append", default=[])
    parser.add_argument("--translation-sync-policy", default="ask-after-persist-change")
    parser.add_argument("--existing-slug")
    parser.add_argument("--analyze-existing", action="store_true")
    parser.add_argument("--apply-existing", action="store_true")
    parser.add_argument("--resolve-conflicts", action="store_true")
    args = parser.parse_args()

    repo_root = Path(args.repo_root).expanduser().resolve()
    base = repo_root / "docs" / "RepoMem"

    selected_modes = [args.analyze_existing, args.apply_existing, args.resolve_conflicts]
    if sum(1 for item in selected_modes if item) > 1:
        parser.error("use only one of --analyze-existing, --apply-existing, or --resolve-conflicts")
    if (args.analyze_existing or args.apply_existing or args.resolve_conflicts) and not args.existing_slug:
        parser.error("--existing-slug is required for existing repository init flows")

    if args.analyze_existing:
        proposal_path = analyze_existing_repo(base, repo_root, args.existing_slug, args.default_language)
        print(f"Generated init proposal at {proposal_path}")
        return 0

    if args.apply_existing:
        created, conflicts, conflicts_path = apply_existing_repo(
            base,
            args.existing_slug,
            args.default_language,
            args.secondary_language,
            args.translation_sync_policy,
        )
        if created:
            print(f"Created {len(created)} persistent docs")
        if conflicts_path is not None:
            print(f"Generated init conflicts at {conflicts_path}")
        else:
            print("Applied init proposal without conflicts")
        return 0

    if args.resolve_conflicts:
        updated, skipped = resolve_existing_conflicts(
            base,
            args.existing_slug,
            args.default_language,
            args.secondary_language,
            args.translation_sync_policy,
        )
        if updated:
            print(f"Resolved {len(updated)} conflicts by writing confirmed changes")
        if skipped:
            print(f"Left {len(skipped)} conflicts unchanged")
        return 0

    initialize_standard_layout(base, args.default_language, args.secondary_language, args.translation_sync_policy)
    print(f"Initialized RepoMem at {base}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
