from transformers import pipeline
import os
import requests
from dotenv import load_dotenv

load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")




def generate_answer(query: str, retrieved_chunks: list):
    context = "\n\n".join([c["text"] for c in retrieved_chunks])

    prompt = f"""
        Answer the question using ONLY the context below.

        Context:
        {context}

        Question:
        {query}
        """
    
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": "openai/gpt-oss-120b:free",
            "messages": [
                {"role": "user", "content": prompt}
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