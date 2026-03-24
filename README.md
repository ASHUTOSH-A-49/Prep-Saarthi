# 🧠PrepSaarthi (Multimodal AI Companion)

> **An Autonomous Multimodal AI Learning Companion featuring distraction-free video processing, Indic language dubbing, and mathematically rigorous exam proctoring.**

[![Built with React](https://img.shields.io/badge/Built_with-React-61DAFB?style=for-the-badge&logo=react&logoColor=black)](https://reactjs.org/)
[![Powered by FastAPI](https://img.shields.io/badge/Powered_by-FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![AI by Groq](https://img.shields.io/badge/AI_by-Groq-F55036?style=for-the-badge&logo=groq&logoColor=white)](https://groq.com/)
[![Database MongoDB](https://img.shields.io/badge/Database-MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)](https://www.mongodb.com/)

---

## 🌟 The Vision
In a world of short attention spans and passive consumption, we built a platform that forces active learning. This platform takes standard educational content (like YouTube videos) and transforms it into a highly structured, distraction-free, and accessible learning environment. Furthermore, it tests that knowledge using an uncompromising, AI-powered proctoring engine.

## ✨ Key Features

### 🎬 1. Multimodal Content Processor (The Smart Player)
* **Distraction-Free UX:** Strips YouTube videos of comments, recommendations, and algorithmic traps using custom iframe parameters.
* **Instant Knowledge Extraction:** Bypasses manual note-taking by utilizing `youtube-transcript-api` to instantly extract video text.
* **Groq Llama-3 AI Engine:** Generates highly structured Markdown notes and interactive `Mermaid.js` mindmaps from the transcript at 800+ tokens per second.
* **On-the-Fly Indic Dubbing:** Translates the entire lecture to Hindi using Groq, synthesizes it into audio using `gTTS`, and perfectly synchronizes playback with the user's video controls.

### 👁️ 2. The Uncompromising Proctor (Zero-Trust Exam Engine)
* **Head-Pose Tracking:** Utilizes `@vladmandic/face-api` (TinyFaceDetector) running entirely client-side to detect if a student drops their gaze to look at a phone.
* **Environment Locking:** Native Browser APIs strictly enforce Fullscreen mode and track Page Visibility to instantly catch tab-switching or Googling attempts.
* **Merciless Flagging:** A built-in tolerance window catches micro-flickers, issuing UI warnings and automatically submitting the exam upon repeated violations.

### 🧠 3. The SRS Data Loop (Spaced Repetition)
* Mistakes made during proctored mock tests are not forgotten. They are logged into a MongoDB Vault and rescheduled based on the Ebbinghaus Forgetting Curve to optimize daily revisions.

---

## 🏗️ System Architecture

We utilized a robust microservice approach to ensure fault tolerance during the live demo:

* **Frontend:** React + Vite + Tailwind CSS.
* **Backend:** Python FastAPI for heavy asynchronous AI processing and data routing.
* **Database:** MongoDB (Motor Async Driver).
* **AI Routing:** * **Groq API (Llama 3 70B):** Dedicated exclusively to the heavy Multimodal Content Processor for blazing-fast text generation and translation.
  * **Google Gemini 2.5 Flash:** Powers the dynamic Quiz Generation and Vault summarization.

---

## 🚀 Local Installation & Setup

### Prerequisites
* Node.js (v18+)
* Python (3.10+)
* MongoDB (Local or Atlas URI)

### 1. Clone the Repository
\`\`\`bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
\`\`\`

### 2. Backend Setup (FastAPI)
Open a terminal and navigate to the backend folder:
\`\`\`bash
cd backend

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install fastapi uvicorn groq google-generativeai youtube-transcript-api gTTS motor pydantic

# Set up environment variables
cp .env.example .env
\`\`\`
**Configure your `.env` file:**
\`\`\`env
MONGO_URI=mongodb://localhost:27017
GROQ_API_KEY=your_groq_key_here
GEMINI_API_KEY=your_gemini_key_here
\`\`\`
**Start the Server:**
\`\`\`bash
uvicorn main:app --reload --port 8000
\`\`\`

### 3. Frontend Setup (React/Vite)
Open a terminal and navigate to the frontend folder:
\`\`\`bash
cd frontend

# Install dependencies
npm install

# Start the development server
npm run dev
\`\`\`

### 4. Face-API Models Configuration
Ensure the TinyFaceDetector neural network weights are present.
Download `tiny_face_detector_model-weights_manifest.json` and `tiny_face_detector_model.weights.bin` and place them inside the frontend's `public/models` directory.

---

## 🛠️ Challenges We Ran Into (Hackathon Realities)
* **The WASM Bundler War:** We initially attempted to build our proctoring engine using WebGazer.js. However, modern Vite bundlers clashed violently with Google's MediaPipe WASM binaries, throwing continuous 404 errors. We engineered a hard pivot to `@vladmandic/face-api`, trading exact pupil-tracking for highly accurate head-pose (phone-checking) tracking, which integrated flawlessly with React.
* **Audio-Video Synchronization:** Making an AI-generated `.mp3` file pause, play, and seek perfectly in sync with a third-party YouTube Iframe required writing custom React `useRef` hooks to forcefully tether the HTML5 audio element's clock to the Iframe's emitted progress events.

---

## 👥 Team
Built with late nights and a lot of caffeine by **Team kaala khatta**.

* **Rahul Sahu** 
* **Shourya Sinha**
* **Ashutosh Behera** 

---
*Note: The backend is currently configured to use an instant-text testing route via `youtube-transcript-api` to avoid live stage-demo timeout risks associated with downloading raw YouTube audio.*
