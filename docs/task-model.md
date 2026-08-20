# PHYX Task Model

The Task model represents a natural-language or programmatic goal without coupling the PHYX core to an LLM provider, robot middleware, simulator, or hardware platform.

## Core fields

- `task_id`: unique identifier supplied by the integrating aggregate.
- `goal`: non-empty human- or machine-readable goal description.
- `status`: explicit lifecycle state.
- `metadata`: extensible application metadata.

## Lifecycle

```text
PENDING -> RUNNING -> COMPLETED
PENDING -> CANCELLED
RUNNING -> FAILED
RUNNING -> CANCELLED
```

Terminal states cannot transition to another state. Planning and execution engines are responsible for interpreting the goal and producing actions; the Task domain object only owns task intent and lifecycle state.
