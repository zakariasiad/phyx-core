# PHYX Robot Model

The Robot model defines the hardware-independent identity, state, and capabilities of a robot.

## Lifecycle

The initial state is `idle`.

Allowed transitions are:

- `idle` → `ready` or `error`
- `ready` → `running`, `idle`, or `error`
- `running` → `paused`, `ready`, or `error`
- `paused` → `running`, `ready`, or `error`
- `error` → `idle`

Invalid transitions are rejected deterministically.

## Domain boundary

The core model stores capabilities, sensor identifiers, and actuator identifiers, but it does not control hardware or depend on ROS 2, a simulator, or a specific driver implementation.
