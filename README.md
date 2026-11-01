# S.A.N.B.A. Behavioral SDK (v1.0)

Welcome to the official public open-source release of the **S.A.N.B.A. Behavioral SDK**. This toolkit provides developers with the essential components, modular interfaces, and protocol adapters required to seamlessly integrate external applications and subsystems with the advanced core behavioral architectures.

## Core Features & Architecture

*   **Modular Architecture:** Easily expand behavioral capabilities through standard interfaces.
*   **High Performance:** Includes native C++ source files and headers optimized for low-latency operational environments.
*   **Plug-and-Play Integration:** Pre-configured components designed for immediate connectivity.

## Repository Structure

*   `adapters/` : Essential communication and protocol adapters for cross-system interfacing.
*   `core_engine/` : Core logical framework driving the behavioral SDK runtime engine (`behavioral_engine_sdk.py`).
*   `cpp_src/` : C++ source code, headers, and specific adapters tailored for fast native compile-time integration.
*   `docs/` : Technical manuals, architectural overviews, and functional specifications.

## Quick Start Guide

To initialize and verify the behavioral framework within your local environment, run the provided verification suite:

```bash
python test_sdk_run.py
```

To compile and pack the distribution-ready binaries for production deployment, execute the automated build script:

```bash
python build_complete_sdk.py
```

## Licensing

This project is distributed under the proprietary commercial terms outlined in the accompanying `LICENSE_AGREEMENT.txt` file. Please ensure compliance regarding redistribution and commercial utilization.
