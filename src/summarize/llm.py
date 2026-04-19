import requests

OLLAMA_URL = "http://localhost:11434/api/generate"


def generate_summary(title, abstract):
    prompt = f"""
You are explaining a research paper for a 60-second YouTube video.

Paper Title:
{title}

Abstract:
{abstract}

Give output in this format:

1. Hook (1 sentence)
2. Problem (1–2 sentences)
3. Key Idea (intuitive explanation)
4. Why it matters (1 sentence)
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