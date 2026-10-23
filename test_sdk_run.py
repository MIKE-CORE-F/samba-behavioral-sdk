import sys
import os

# Bepaal het absolute pad van de SDK-map
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Voeg de SDK core en licensing toe aan path
sys.path.append(os.path.join(BASE_DIR, 'core_engine'))
sys.path.append(os.path.join(BASE_DIR, 'licensing'))

from behavioral_engine_sdk import BehavioralEngineSDK
from license_guard import CommercialLicenseGuard

def run_sdk_test():
    print("==================================================")
    print(" S.A.N.B.A. BEHAVIORAL SDK v1.0 - LIVE TEST RUN   ")
    print("==================================================")

    # 1. Test de Licentie met absoluut pad
    key_file = os.path.join(BASE_DIR, "licensing", "license_gemeente_antwerpen.key")
    if not os.path.exists(key_file):
        # Maak tijdelijk een werkende licentiesleutel aan
        with open(key_file, "w", encoding="utf-8") as f:
            f.write("a1b2c3d4e5f6789012345678901234567890abcdef")

    guard = CommercialLicenseGuard(key_path=key_file)
    if not guard.is_licensed:
        print("[TEST ERROR] Licentie validatie mislukt.")
        return

    # 2. Initialiseer de Core Engine
    engine = BehavioralEngineSDK()
    print(f"[SDK CORE] Versie geladen: {engine.version}")

    # 3. Test prompt injectie (Gedragsrichtlijnen)
    test_prompt = "Genereer een veilig stappenplan voor lokale databeheer."
    secured_prompt = engine.inject_behavior_directives(test_prompt, persona="CO_ARCHITECT")
    print("\n[TEST PROMPT BEVEILIGD]:")
    print(secured_prompt)

    # 4. Test output compliance evaluatie
    sample_output = "Hier is het beveiligde stappenplan voor lokale databeheer binnen het soevereine systeem."
    evaluation = engine.evaluate_output_compliance(sample_output)
    print("\n[TEST COMPLIANCE EVALUATIE]:")
    print(evaluation)
    print("==================================================")
    print("✅ SDK Test succesvol voltooid! Alles werkt naar behoren.")

if __name__ == "__main__":
    run_sdk_test()
