# 🎬 AI Research Video Pipeline

An end-to-end automated system that transforms research papers into narrated videos and uploads them to YouTube.

---

## 🚀 Features

* 🔍 Fetch latest research papers from arXiv
* 🧠 Generate summaries using local LLM (Ollama)
* ✍️ Convert summaries into engaging scripts
* 🔊 Generate audio using TTS
* 🎥 Create videos with avatar + narration
* 📺 Upload videos to YouTube automatically

---

## 🧱 Pipeline

```text
Topics → arXiv → LLM Summary → Script → Audio → Video → YouTube
```

---

## 🛠️ Tech Stack

* Python
* Ollama (LLM)
* FFmpeg (video processing)
* pyttsx3 (TTS)
* YouTube Data API

---

## 📁 Project Structure

```
src/
├── fetch/        # arXiv fetching
├── summarize/    # LLM + script generation
├── tts/          # audio generation
├── video/        # video creation
├── upload/       # YouTube upload
├── utils/        # storage utilities
└── pipeline.py   # main pipeline

config/
├── topics.json
└── client_secret.json (not tracked)

data/
├── YYYY-MM-DD/
```

---

## ⚙️ Setup

### 1. Clone repo

```bash
git clone <your-repo>
cd ai-research-video-pipeline
```

---

### 2. Create virtual environment

```bash
python -m venv venv
source venv/Scripts/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Start Ollama

```bash
ollama serve
```

---

### 5. Run pipeline

```bash
python src/pipeline.py
```

---

## 📺 Output

* JSON summaries
* Audio files (.wav)
* Video files (.mp4)
* (Optional) Uploaded YouTube videos

---

## 🔒 Notes

* `client_secret.json` is required for YouTube upload
* Not included in repo for security reasons

---

## 🚀 Future Improvements

* Lip-synced avatar (Wav2Lip)
* Subtitle timing (SRT)
* Thumbnail generation
* Scheduled uploads
* Better paper ranking

---

## 👨‍💻 Author

Soumyadeep Roy,CSA,IISc Bangalore