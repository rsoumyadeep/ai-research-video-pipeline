import os
import json
from datetime import datetime


def get_today_folder():
    today = datetime.now().strftime("%Y-%m-%d")
    folder_path = os.path.join("data", today)

    os.makedirs(folder_path, exist_ok=True)
    return folder_path


def save_papers(papers, filename="papers.json"):
    folder = get_today_folder()
    file_path = os.path.join(folder, filename)

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(papers, f, indent=4)

    print(f"💾 Saved papers to {file_path}")