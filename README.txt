===================================================
SANBA BEHAVIORAL SDK v1.0 - INTEGRATION NOTES
===================================================

STATUS
This is an early prototype. See README.md ("Current limitations").

USAGE
1. Add `core_engine/behavioral_engine_sdk.py` to your project.
2. Create the engine:    engine = BehavioralEngineSDK()
3. Add directives to a prompt before sending it to your LLM:
                         engine.inject_behavior_directives(prompt, persona="CO_ARCHITECT")
4. Check a model answer: engine.evaluate_output_compliance(text)
   (basic placeholder check, not a content-safety filter)

OPTIONAL
- `adapters/sdk_adapter.py` wraps an incoming payload in a dict
  (SDKAdapter.adapt_payload). It does not change prompts.
- `license_guard.py` checks a licence key file. The engine does not
  call it automatically; call CommercialLicenseGuard(key_path).validate_license()
  yourself if you want a licence check.

LICENCE
This software is proprietary. See LICENSE_AGREEMENT.txt.
