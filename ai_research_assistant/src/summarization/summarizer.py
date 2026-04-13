import os
import requests
from .prompts import SUMMARY_PROMPT

OPENROUTER_API_KEY = "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"

def summarize_chunk(chunk: str, prompt: str = SUMMARY_PROMPT) -> str:
    input_text = prompt.format(chunk=chunk)

    print(input_text)
    print("--------------------------------")

    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": "openai/gpt-oss-120b:free",
            "messages": [
                {"role": "user", "content": input_text}
            ],
            "temperature": 0.0,
            "top_p": 1.0,
            "max_tokens": 300,
        },
        timeout=60,
    )

    response.raise_for_status()
    data = response.json()

    return data["choices"][0]["message"]["content"]