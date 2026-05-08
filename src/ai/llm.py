import os
import requests


class LLMClient:
    def __init__(self, providers=None):
        self.providers = providers or [
            {
                "name": "openrouter",
                "model": "openai/gpt-4o-mini",
                "api_key": os.getenv("OPENROUTER_API_KEY"),
                "url": "https://openrouter.ai/api/v1/chat/completions",
            },
            {
                "name": "groq",
                "model": "llama-3.1-8b-instant",
                "api_key": os.getenv("GROQ_API_KEY"),
                "url": "https://api.groq.com/openai/v1/chat/completions",
            },
        ]

    def _call_provider(self, provider, prompt):
        headers = {
            "Authorization": f"Bearer {provider['api_key']}",
            "Content-Type": "application/json",
        }

        payload = {
            "model": provider["model"],
            "messages": [
                {"role": "system", "content": "You are a data analyst."},
                {"role": "user", "content": prompt},
            ],
        }

        response = requests.post(provider["url"], json=payload, headers=headers, timeout=20)

        if response.status_code != 200:
            raise Exception(f"{provider['name']} failed: {response.text}")

        return response.json()["choices"][0]["message"]["content"]

    def generate(self, prompt: str):
        last_error = None

        for provider in self.providers:
            try:
                return self._call_provider(provider, prompt)
            except Exception as e:
                last_error = e
                continue

        raise Exception(f"All LLM providers failed. Last error: {last_error}")