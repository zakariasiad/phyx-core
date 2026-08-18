# PHYX Environment Model

The Environment model is hardware- and simulator-independent. It represents a world container and the poses of uniquely identified entities.

## Coordinate convention

PHYX uses a right-handed Cartesian coordinate frame. Positions are expressed in metres. Orientations use unit quaternions in `(x, y, z, w)` order.

The Environment model does not prescribe a particular robot middleware, simulator, sensor, or hardware platform. Adapters may translate these domain types to ROS 2, simulators, or physical devices.

## Core types

- `Vector3`: three-dimensional position or displacement.
- `Pose`: position plus orientation.
- `Environment`: uniquely identified environment containing uniquely identified entities and their poses.

## Validation

- Environment and entity identifiers must be non-empty strings.
- Entity identifiers must be unique within an environment.
- Orientation must contain four values and cannot be a zero quaternion.
