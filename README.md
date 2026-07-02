# 🤖 AI YouTube Video Analyzer

## 📖 Description
An AI-powered YouTube Video Analyzer built using Python, Streamlit, and Groq LLM. It analyzes YouTube videos and generates intelligent summaries using AI.

## 🚀 Features
- Analyze YouTube videos using URL
- AI-generated summary
- Video overview
- Fast response using Groq LLM
- Simple Streamlit interface

## 🛠 Technologies Used
- Python
- Streamlit
- Groq API
- YouTube Transcript API
- python-dotenv
- Requests

## 📂 Workflow
1. User enters a YouTube URL.
2. Transcript is extracted.
3. Transcript is sent to Groq LLM.
4. AI generates the summary.
5. Results are displayed in Streamlit.

## ▶️ How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
