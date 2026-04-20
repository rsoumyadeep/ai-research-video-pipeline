# 🎥 AI Research → YouTube Automation Pipeline

An end-to-end automated system that transforms the latest research papers into narrated videos and uploads them to YouTube.

---

## 🚀 Overview

This project builds a **fully automated content generation pipeline**:

```
Topics → arXiv → LLM → Script → Audio → Video → YouTube
```

Given a set of topics, the system:

1. Fetches latest research papers from arXiv
2. Summarizes them using a local LLM
3. Converts summaries into engaging scripts
4. Generates audio narration (TTS)
5. Creates videos using FFmpeg
6. Uploads videos to YouTube automatically

---

## 🧠 Key Features

* 🔍 **Automated Research Discovery** (arXiv API)
* 🤖 **Local LLM Summarization** (Ollama + LLaMA3)
* ✍️ **Script Generation for Content Creation**
* 🔊 **Offline Text-to-Speech (TTS)**
* 🎬 **Video Generation using FFmpeg**
* 📺 **Automated YouTube Upload (OAuth 2.0)**
* 🧱 Modular and extensible pipeline architecture

---

## 📁 Project Structure

```
ai-research-video-pipeline/
│
├── config/
│   ├── topics.json
│   └── client_secret.json   # (ignored in git)
│
├── data/
│   └── YYYY-MM-DD/
│       ├── audio.wav
│       ├── video.mp4
│       └── papers.json
│
├── scripts/
│   └── input_topics.py
│
├── src/
│   ├── fetch/
│   │   └── arxiv.py
│   ├── summarize/
│   │   ├── llm.py
│   │   └── script.py
│   ├── tts/
│   │   └── generate_audio.py
│   ├── video/
│   │   └── generate_video.py
│   ├── upload/
│   │   └── youtube.py
│   ├── utils/
│   │   └── storage.py
│   └── pipeline.py
│
├── assets/
│   └── avatar.jpg
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone repository

```bash
git clone https://github.com/your-username/ai-research-video-pipeline.git
cd ai-research-video-pipeline
```

---

### 2️⃣ Create virtual environment

```bash
python -m venv venv
source venv/Scripts/activate   # Windows
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Install Ollama (Local LLM)

* Install Ollama
* Pull model:

```bash
ollama pull llama3
ollama serve
```

---

### 5️⃣ Install FFmpeg

* Download and add to PATH
* Verify:

```bash
ffmpeg -version
```

---

### 6️⃣ Setup YouTube API

* Create project in Google Cloud
* Enable **YouTube Data API v3**
* Create OAuth client (Desktop App)
* Download credentials

👉 Place file here:

```
config/client_secret.json
```

⚠️ Do NOT commit this file (already in `.gitignore`)

---

## ▶️ Running the Pipeline

### Step 1: Input topics

```bash
python scripts/input_topics.py
```

Example:

```
offline reinforcement learning, POMDP
```

---

### Step 2: Run pipeline

```bash
python src/pipeline.py
```

---

## 📺 Output

Generated files:

```
data/YYYY-MM-DD/
├── audio.wav
├── video.mp4
└── papers.json
```

Uploaded video appears in:

👉 YouTube Studio → Content

---

## 🧠 Technical Highlights

* Local inference using LLM (no API cost)
* Modular pipeline design
* API integrations:

  * arXiv API
  * YouTube Data API
* OAuth 2.0 authentication flow
* Media processing using FFmpeg

---

## ⚠️ Common Issues & Fixes

### ❌ `ModuleNotFoundError`

👉 Activate virtual environment

---

### ❌ `ffmpeg not found`

👉 Add FFmpeg to system PATH

---

### ❌ OAuth 403 error

👉 Add your email as **Test User**

---

### ❌ GitHub push blocked

👉 Remove `client_secret.json` and update `.gitignore`

---

## 🔮 Future Extensions (High Impact 🚀)

### 🎯 Content Quality

* Automatic catchy title generation (CTR optimization)
* Thumbnail generation (using diffusion models)
* Subtitle generation (SRT + timestamps)

---

### 🧠 ML / Research Extensions

* Paper ranking using citation/recency
* Topic clustering (unsupervised learning)
* Personalized recommendations
* RL-based topic selection (exploration vs exploitation)

---

### 🎥 Video Improvements

* Lip-sync avatars (Wav2Lip)
* Dynamic animations & overlays
* Multi-image/video clips per section

---

### ⚙️ Automation

* Daily scheduled runs (cron jobs)
* Email/WhatsApp notifications
* Batch processing of multiple topics

---

### ☁️ Scaling

* Deploy on cloud (AWS/GCP)
* Dockerize pipeline
* Parallel processing for faster generation

---



---

## 🤝 Contributing

Feel free to fork, improve, and extend the system!

---

## ⭐ Acknowledgements

* arXiv API
* Ollama
* FFmpeg
* Google YouTube Data API

---

## 📌 License

MIT License


## 👨‍💻 Author

Soumyadeep Roy,Depart. of CSA,IISc Bangalore