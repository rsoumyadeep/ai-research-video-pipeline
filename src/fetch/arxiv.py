import feedparser
import requests

ARXIV_API_URL = "http://export.arxiv.org/api/query"



def fetch_papers(topic: str, max_results: int = 5):
    """
    Fetch latest papers from arXiv for a given topic.
    """

    # Use category for robustness
    topic_map = {
    "machine learning": "cat:cs.LG",
    "active learning": "cat:cs.LG AND all:active+learning",
    }

    topic_lower = topic.lower()

    if topic_lower in topic_map:
        search_query = topic_map[topic_lower]
    else:
        query_topic = "+".join(topic.strip().split())
        search_query = f"all:{query_topic}"

    query = (
        f"search_query={search_query}"
        f"&start=0"
        f"&max_results={max_results}"
        f"&sortBy=submittedDate"
        f"&sortOrder=descending"
    )

    url = f"{ARXIV_API_URL}?{query}"

    headers = {
        "User-Agent": "ai-research-pipeline/1.0 (your_email@example.com)"
    }

    response = requests.get(url, headers=headers)

    feed = feedparser.parse(response.text)

    papers = []

    for entry in feed.entries:
        paper = {
            "id": entry.id,
            "title": entry.title.strip(),
            "summary": entry.summary.strip(),
            "published": entry.published,
            "link": entry.link,
        }
        papers.append(paper)

    return papers


def print_papers(papers):
    """
    Pretty print papers (for debugging)
    """
    if not papers:
        print("⚠️ No papers found.")
        return

    for i, p in enumerate(papers, 1):
        print(f"\n📄 Paper {i}")
        print(f"Title: {p['title']}")
        print(f"Published: {p['published']}")
        print(f"Link: {p['link']}")
        print("-" * 50)


if __name__ == "__main__":
    topic = "offline reinforcement learning"
    papers = fetch_papers(topic)

    print_papers(papers)