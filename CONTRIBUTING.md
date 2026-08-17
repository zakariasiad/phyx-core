# Contributing to PHYX

Thank you for your interest in contributing to PHYX.

PHYX is an open-source project focused on Physical AI and robotics. We welcome code contributions, research ideas, documentation improvements, simulation scenarios, hardware integrations, testing, and technical discussions.

## Before You Start

1. Read the README.
2. Check the roadmap.
3. Search existing issues before opening a new one.
4. For significant architectural changes, open an issue first and discuss the proposal.

## Development Principles

- Prefer simple, modular designs.
- Keep interfaces explicit and testable.
- Separate high-level AI reasoning from low-level robot control.
- Treat safety as a first-class engineering requirement.
- Prefer reproducible experiments.
- Document public APIs and important design decisions.
- Avoid unnecessary dependencies.

## Pull Requests

A good pull request should:

- Have a clear purpose.
- Include tests where appropriate.
- Update documentation when behavior or APIs change.
- Keep unrelated changes out of the PR.
- Explain important design decisions.

## Commit Messages

Use concise, descriptive commit messages. Conventional Commit style is recommended:

- `feat:` for new functionality
- `fix:` for bug fixes
- `docs:` for documentation
- `test:` for tests
- `refactor:` for internal changes
- `build:` for build and dependency changes
- `ci:` for CI changes

## Robotics Safety

Never assume that simulated behavior is safe on physical hardware. Hardware deployments must use appropriate limits, emergency stops, isolation, supervision, and validation procedures.

## Research Contributions

Research proposals should include:

- Problem statement
- Motivation
- Proposed approach
- Experimental setup
- Evaluation criteria
- Reproducibility notes

## Code of Conduct

All contributors are expected to follow the project's Code of Conduct.
