from groq import Groq
from app.core.config import settings

client = Groq(api_key=settings.GROQ_API_KEY)


def generate_sql(prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system",
                    "content": "You are a SQL expert. Return ONLY valid PostgreSQL SQL. No explanation."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0
        )

        if not response or not response.choices:
            raise ValueError("Empty response from Groq")

        content = response.choices[0].message.content

        if not content:
            raise ValueError("No SQL returned from model")

        return content.strip()

    except Exception as e:
        raise RuntimeError(f"LLM generation failed: {e}")


def generate_insight(prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system",
                    "content": "You are a data analyst. Explain insights clearly and concisely."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3
        )

        if not response or not response.choices:
            raise ValueError("Empty response from Groq")

        content = response.choices[0].message.content

        if not content:
            raise ValueError("No insight returned from model")

        return content.strip()

    except Exception as e:
        raise RuntimeError(f"Insight generation failed: {e}")