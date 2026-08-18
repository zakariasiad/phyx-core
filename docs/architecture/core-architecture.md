# PHYX Core Architecture v0.1

Status: Proposed for v0.1-alpha

## 1. Purpose

PHYX Core is the hardware-independent domain and orchestration layer for physical AI systems. It defines stable concepts and contracts without requiring a specific robot, simulator, middleware, sensor stack, or AI provider.

The core architectural pipeline is:

**Perception → Understanding → Planning → Validation → Execution**

Adapters connect this pipeline to external systems such as ROS 2, simulators, cameras, robot controllers, and future cloud services.

## 2. Layer boundaries

### Domain

Owns the canonical representation of the physical world and task state.

- `environment`: world/container state, spatial primitives, coordinate-independent domain concepts.
- `objects`: identifiable physical objects and observations.
- `robot`: robot identity, pose, and high-level lifecycle state.
- `tasks`: user or system goals and task lifecycle.
- `actions`: structured actions that a planner can produce and an executor can consume.

Domain modules must not depend on ROS 2, simulator SDKs, vendor robot SDKs, LLM providers, or network services.

### Intelligence

Responsible for turning observations and goals into structured plans.

- `perception`: converts sensor observations into structured world observations.
- `understanding`: maintains or derives semantic/world-state representations.
- `planner`: decomposes a validated task into ordered or partially ordered actions.

Intelligence components may depend on Domain contracts, but Domain must never depend on Intelligence implementations.

### Safety

Provides a mandatory validation boundary between planning and execution.

- `safety`: checks actions/plans against domain-level safety policies before execution.

Safety is not an authorization to bypass hardware safety systems. Physical robot controllers, emergency stops, and hardware interlocks remain independent safety layers.

### Execution

Owns the lifecycle of approved actions and translates them into executable operations.

- `execution`: action dispatch, execution state, cancellation, timeout, and failure reporting.

Execution depends on Domain and Safety contracts. It must not embed a specific robot vendor or middleware.

### Adapters

Adapters translate PHYX contracts to external technologies.

- `ros2`: ROS 2 nodes, topics, services, actions, and message translation.
- `simulation`: simulator-specific integration.
- `hardware`: vendor/controller-specific integration.
- `sdk`: public developer-facing interfaces.

Adapters may depend on Core contracts. Core must not import adapter packages.

## 3. Dependency direction

The allowed dependency direction is:

```text
External Systems
      │
      ▼
   Adapters
      │
      ▼
 Execution ← Safety
      │       ▲
      ▼       │
 Intelligence ┘
      │
      ▼
    Domain
```

A simpler rule is:

```text
Domain ← Intelligence ← Safety ← Execution ← Adapters
```

Imports must flow toward the stable Domain contracts. Reverse dependencies are architectural violations.

## 4. Runtime flow

A typical PHYX task follows this lifecycle:

```text
Sensor / User Input
        ↓
    Perception
        ↓
   Understanding
        ↓
      Task
        ↓
     Planner
        ↓
  Action / Plan
        ↓
 Safety Validator
        ↓
    Execution
        ↓
   ROS 2 / Simulator / Hardware
        ↓
    Observations
        └──────────────→ World State update
```

No planner output is executed directly. All executable actions must pass through the safety boundary and the execution layer.

## 5. Core API principles

1. Domain objects should remain serializable and deterministic where practical.
2. Public interfaces should use explicit typed contracts rather than framework-specific objects.
3. External dependencies are introduced through adapters or optional packages.
4. Hardware-specific behavior must never leak into Domain models.
5. Safety validation is explicit and observable.
6. Failures must be represented as structured state/results rather than hidden exceptions at system boundaries.
7. The architecture must support simulation without requiring physical hardware.

## 6. ROS 2 policy

ROS 2 is a first-class integration target, but it is **not a Core dependency**.

The `ros2/` package will translate between PHYX contracts and ROS 2 interfaces. This allows the same Core and Planner logic to run in a simulator, a non-ROS environment, or another middleware stack.

## 7. AI provider policy

PHYX Core does not require a specific LLM, vision model, or AI vendor. AI providers are integration choices behind explicit interfaces.

A future LLM/agent component may propose or refine tasks and plans, but it must produce PHYX-native structured contracts before anything reaches Safety or Execution.

## 8. v0.1 scope boundaries

Included:

- Domain models for environment, robot, object, task, and action.
- Planner and safety boundaries.
- Hardware-independent execution boundary.
- Adapter boundary for ROS 2 and simulation.
- Initial Python package layout.

Deferred:

- Full 3D world model.
- Motion planning algorithms.
- Real-time control loops.
- Computer vision implementation.
- LLM provider integrations.
- Distributed/cloud execution.
- Production-grade hardware safety certification.

## 9. Architecture decision

For v0.1, PHYX prioritizes **stable domain contracts and hardware independence over feature breadth**. This makes the Core reusable across different robots and simulators while allowing specialized capabilities to evolve independently.