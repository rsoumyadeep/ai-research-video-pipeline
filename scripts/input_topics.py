import json
import os

CONFIG_PATH = "config/topics.json"


def get_user_topics():
    print("📌 Enter topics you care about (comma separated):")
    user_input = input("👉 ")

    topics = [t.strip() for t in user_input.split(",") if t.strip()]
    return topics


def save_topics(topics):
    data = {
        "topics": topics
    }

    os.makedirs("config", exist_ok=True)

    with open(CONFIG_PATH, "w") as f:
        json.dump(data, f, indent=4)

    print("\n✅ Topics saved successfully!")
    print("📂 Saved to:", CONFIG_PATH)


if __name__ == "__main__":
    topics = get_user_topics()

    if not topics:
        print("⚠️ No topics entered. Exiting.")
    else:
        save_topics(topics)