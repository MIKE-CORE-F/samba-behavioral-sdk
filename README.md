# S.A.N.B.A. Behavioral SDK (v1.0)

A small toolkit for attaching behavioural directives to prompts sent to an LLM, with a Python core, a payload adapter and C++ interface headers.

> **Status: early prototype (v1.0).** The structure and interfaces are in place, but several components are placeholders. See [Current limitations](#current-limitations) before relying on this code.

## Repository structure

| Path | Purpose |
|---|---|
| `core_engine/behavioral_engine_sdk.py` | `BehavioralEngineSDK`: appends a behavioural directive to a prompt (`inject_behavior_directives`) and runs a basic output check (`evaluate_output_compliance`). |
| `adapters/sdk_adapter.py` | `SDKAdapter.adapt_payload()`: wraps an incoming payload in a dict marked `READY_FOR_ENGINE`. |
| `license_guard.py` | `CommercialLicenseGuard`: checks whether a licence key file exists and looks plausible. |
| `cpp_src/` | C++ headers and a stub implementation (`SANBA_BEHAVIORAL_SDK_GEDRAGS`). |
| `docs/` | Short integration notes. |
| `test_sdk_run.py` | Smoke test of the Python components. |
| `build_complete_sdk.py` | Helper that writes a set of template files to a local folder (see limitations). |

## Quick start

Requires Python 3.10 or newer.

```bash
python test_sdk_run.py
```

The smoke test creates a local `licensing/` folder with a test key if none exists, then exercises the licence guard, the prompt injection and the compliance check. The folder is listed in `.gitignore`.

Minimal usage:

```python
from core_engine.behavioral_engine_sdk import BehavioralEngineSDK

engine = BehavioralEngineSDK()
prompt = engine.inject_behavior_directives("Write a data-management plan.", persona="CO_ARCHITECT")
result = engine.evaluate_output_compliance("Some model output")
print(result)  # {'compliant': True, 'status': 'APPROVED', 'score': 0.98}
```

## Current limitations

These are known and should be addressed before production use:

- **Compliance check is a placeholder.** `evaluate_output_compliance` approves any text longer than 5 characters that does not contain the word `ERROR`. The score is a fixed value (0.98 or 0.0). It does not detect unsafe, sensitive or policy-violating content.
- **Licence check is not enforced.** `CommercialLicenseGuard` accepts any key file with more than 10 characters or JSON containing a `payload` or `status: ACTIVE`. Signatures and expiry dates are not verified, and the engine does not call the guard.
- **Adapter is minimal.** `SDKAdapter` does not modify prompts or call any LLM API.
- **C++ code consists of stubs.** The methods in `SANBA_BEHAVIORAL_SDK_GEDRAGS.cpp` (including `Licentiecontrole` and `Gebruikerauthenticatie`) always return `true`. `SANBA_BEHAVIORAL_SDK_ADAPTER_Application` is declared in a header but has no implementation.
- **`build_complete_sdk.py` is out of sync.** It writes template versions of some files to a hard-coded local path and does not compile or package binaries.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## Licensing

This repository is **proprietary**. See `LICENSE_AGREEMENT.txt` for the terms. It is publicly readable but is not open source.
