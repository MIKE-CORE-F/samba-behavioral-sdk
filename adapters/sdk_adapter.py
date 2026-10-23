# [SANBA BEHAVIORAL SDK] API & LLM Adapter
import json

class BehavioralSDKAdapter:
    def __init__(self, sdk_engine):
        self.engine = sdk_engine

    def wrap_ollama_request(self, payload: dict) -> dict:
        prompt = payload.get("prompt", "")
        payload["prompt"] = self.engine.inject_behavior_directives(prompt)
        return payload

    def wrap_openai_request(self, messages: list) -> list:
        system_directive = {"role": "system", "content": "SANBA Behavioral Governance SDK Active."}
        return [system_directive] + messages
