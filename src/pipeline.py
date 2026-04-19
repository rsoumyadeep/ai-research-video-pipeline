import json
import os
from datetime import datetime

from fetch.arxiv import fetch_papers
from utils.storage import save_papers
from summarize.llm import generate_summary
from summarize.script import generate_script
from tts.generate_audio import generate_audio
from video.generate_video import generate_video
from upload.youtube import upload_video


CONFIG_PATH = "config/topics.json"


def load_topics():
    """
    Load topics from config file
    """
    if not os.path.exists(CONFIG_PATH):
        print("⚠️ topics.json not found. Run input_topics.py first.")
        return []

    with open(CONFIG_PATH, "r") as f:
        data = json.load(f)

    return data.get("topics", [])


def get_top_paper(papers):
    """
    Select the top paper (currently first one)
    """
    if not papers:
        return None
    return papers[0]


def run_pipeline():
    """
    Main pipeline
    """
    print("🚀 Starting pipeline...\n")

    topics = load_topics()

    if not topics:
        print("⚠️ No topics available.")
        return

    print(f"📌 Topics: {topics}\n")

    all_results = []

    for topic in topics:
        print(f"\n🔍 Fetching papers for: {topic}")

        papers = fetch_papers(topic)

        if not papers:
            print("⚠️ No papers found.")
            continue

        top_paper = get_top_paper(papers)

        if top_paper:
            print("\n🧠 Generating summary...")
            summary = generate_summary(
                top_paper["title"],
                top_paper["summary"]
            )
            print("✅ Summary generated")

            print("\n🎬 Generating script...")
            script = generate_script(
                top_paper["title"],
                summary
            )
            print("✅ Script generated")

            print("\n🎬 Script:")
            print(script)

            # 🔊 Generate audio
            print("\n🔊 Generating audio...")
            today = datetime.now().strftime("%Y-%m-%d")
            audio_folder = os.path.join("data", today)

            audio_path = os.path.join(
                audio_folder,
                f"{topic.replace(' ', '_')}.wav"
            )

            generate_audio(script, audio_path)

            print("✅ Audio generated")
            print(f"📁 Saved at: {audio_path}")

            video_path=audio_path.replace(".wav", ".mp4")

            generate_video(audio_path,video_path,
                           image_path="assets/avatar.jpg")
            print("\n🎬 Video saved at:")
            print(video_path)
            upload_video(video_path,
                         title=top_paper["title"],
                        description=summary)


            # Store results
            all_results.append({
                "topic": topic,
                "paper": top_paper,
                "summary": summary,
                "script": script,
                "audio_path": audio_path,
                "video_path":video_path
            })

            # Print paper info
            print("\n🏆 Top Paper:")
            print(f"Title: {top_paper['title']}")
            print(f"Published: {top_paper['published']}")
            print(f"Link: {top_paper['link']}")

            print("\n🧠 Summary:")
            print(summary)

            print("-" * 60)

    # Save results
    if all_results:
        save_papers(all_results)
    else:
        print("⚠️ No results to save.")


if __name__ == "__main__":
    run_pipeline()