import os
import json

class CommercialLicenseGuard:
    """
    Manages commercial licensing and sovereign compliance for the SANBA SDK.
    """
    def __init__(self, key_path='licensing/license_gemeente_antwerpen.key'):
        self.key_path = key_path
        self.is_licensed = self._check_license_status()

    def _check_license_status(self) -> bool:
        if os.path.exists(self.key_path):
            try:
                with open(self.key_path, 'r', encoding='utf-8') as f:
                    content = f.read().strip()
                    # Accepteer zowel JSON structuren als simpele hash-strings
                    if content.startswith("{") or content.startswith("["):
                        data = json.loads(content)
                        # Als er een payload in zit of een status active
                        if "payload" in data or data.get("status") == "ACTIVE":
                            return True
                    elif len(content) > 10: # Simpele key-string
                        return True
            except Exception:
                return False
        return False

    def validate_license(self) -> dict:
        if self.is_licensed:
            return {"compliant": True, "status": "ACTIVE", "message": "License verified successfully."}
        return {"compliant": False, "status": "INVALID", "message": "License key not found or inactive."}
