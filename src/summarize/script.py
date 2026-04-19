import requests

OLLAMA_URL = "http://localhost:11434/api/generate"


def generate_script(title, summary):
    prompt = f"""
You are creating a YouTube short (60 seconds) explaining a research paper.

Paper Title:
{title}

Summary:
{summary}

Convert this into a smooth, engaging script:
- conversational tone
- easy to understand
- no bullet points
- no numbering
- ~100–150 words

Make it sound like a human explaining.
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    result = response.json()
    return result.get("response", "").strip()