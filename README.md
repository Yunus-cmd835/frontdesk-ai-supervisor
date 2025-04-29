# Frontdesk – Human-in-the-Loop AI Supervisor (Assessment Submission)

## 🔍 Overview
This project is built as a submission for the Frontdesk Engineering Assessment.  
It simulates a human-in-the-loop system where an AI agent handles customer queries and escalates to a supervisor when needed. The system auto-learns from supervisor responses to improve over time.

---

## 🎯 Features

- 🤖 AI Agent simulation via terminal
- 📞 AI escalates unknown questions to supervisor
- 👤 Simple supervisor dashboard to:
  - View pending requests
  - Submit answers
  - View history
- 🧠 Knowledge base auto-updates on new answers
- 🪄 Agent becomes smarter with each interaction

---

## 🛠 Tech Stack

| Layer       | Technology  |
|-------------|-------------|
| Backend     | Python + FastAPI |
| DB          | SQLite (local) |
| Frontend    | HTML (Jinja2 Templates) |
| Agent Sim   | Python script (`ai_agent.py`) |
| Others      | Requests, JSON |

---

## 🗂 Folder Structure

frontdesk_project/
 ├── main.py # FastAPI backend
 ├── database.py # SQLite DB setup 
 ├── ai_agent.py # AI agent simulator
 ├── knowledge_base.json # Learned answers
 ├── templates/
 │ └── supervisor.html # Supervisor dashboard
 ├── requirements.txt # Dependencies 
 └── README.md # You're here!


---

## ⚙️ Setup Instructions

1. Clone the repo:
```bash
git clone https://github.com/Yunus-cmd835/frontdesk-ai-supervisor.git
cd frontdesk-ai-supervisor

2. Install dependencies

pip install -r requirements.txt

3.Run the FastAPI server:

uvicorn main:app --reload

4.Access the app in browser:

-> Docs: http://127.0.0.1:8000/docs
-> Supervisor UI: http://127.0.0.1:8000/supervisor

5.Run the AI agent:

python ai_agent.py

📹 Demo Video

https://drive.google.com/file/d/1g8PI1xG52GJ3QRL_6hs7aoVTXvCFwDk5/view?usp=sharing

🙏 Thanks
Thanks to the Frontdesk team for this great opportunity!
Excited to contribute and grow together.


