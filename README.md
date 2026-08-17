# PHYX

**Open-source intelligence infrastructure for physical machines.**

PHYX is an open-source framework for building intelligent robots and physical systems that can perceive, reason, plan, and act in the real world.

> **Perceive → Understand → Plan → Act**

## Vision

Make Physical AI accessible to every robotics developer.

## Mission

Build an open, modular, and developer-friendly intelligence layer for physical machines.

## Project Status

PHYX is in early-stage development. The current goal is to establish the core architecture and deliver a first end-to-end simulation before expanding to physical hardware.

## Initial Scope

PHYX v0.1 focuses on:

- A structured environment model
- Task representation
- Perception interfaces
- Task planning interfaces
- ROS 2 integration
- Simulation-first development
- A Python SDK foundation

## Core Architecture

```text
Natural Language
       ↓
   Task Parser
       ↓
 Structured Task
       ↓
     Planner
       ↓
 Validated Actions
       ↓
      ROS 2
       ↓
 Simulation / Robot
```

PHYX is designed so that language models are not directly connected to low-level motor control. Planning and execution should pass through explicit, testable, and safety-aware interfaces.

## Roadmap

- [ ] Define PHYX Core architecture
- [ ] Implement environment model
- [ ] Implement task model
- [ ] Create Python package
- [ ] Create ROS 2 workspace
- [ ] Add sensor abstractions
- [ ] Add basic perception pipeline
- [ ] Add task planning
- [ ] Add simulation environment
- [ ] Build first end-to-end demo
- [ ] Add hardware deployment support

See [ROADMAP.md](ROADMAP.md) for the development plan.

## Repository Structure

```text
core/          Core PHYX abstractions
ros2/          ROS 2 integration
simulation/    Simulation environments and scenarios
sdk/           Developer SDKs
examples/      End-to-end examples
datasets/      Dataset documentation and metadata
tests/         Automated tests
docs/          Technical documentation
tools/         Development utilities
```

## Open Source

PHYX Core is intended to be released under the Apache License 2.0.

## Contributing

Contributions will be welcome as the project reaches its first public development milestones. Please read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting changes.

## Safety

PHYX is intended for research and development. Real-world robot deployment must include appropriate hardware-level safety controls, limits, emergency stops, testing, and human oversight.

## License

Apache License 2.0. See [LICENSE](LICENSE).
