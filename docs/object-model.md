# PHYX Object Model

The Object model represents an identifiable physical-world object without coupling the PHYX core to a simulator, ROS 2, vendor SDK, or hardware driver.

## Core types

- `Object`: identity, pose, semantic type, and enabled state.
- `ObjectType`: small, extensible semantic categories for core reasoning.
- `Pose`: the existing PHYX position/orientation value object.

## Identity and lifecycle

An object identifier must be a non-empty string. Object state can be enabled or disabled, while pose updates replace the current domain pose.

Environment-level uniqueness is enforced by the Environment aggregate when objects are integrated into it. The Object itself remains independent and reusable by adapters.
