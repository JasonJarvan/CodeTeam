---
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
