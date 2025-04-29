from fastapi import FastAPI, HTTPException, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from database import create_connection
import json, os

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# 🛠 Define HelpRequest model
class HelpRequest(BaseModel):
    customer_name: str
    question: str

# 🛠 Request Help Endpoint
@app.post("/request_help/")
def request_help(help_request: HelpRequest):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO help_requests (customer_name, question, status, answer)
        VALUES (?, ?, 'pending', NULL)
    ''', (help_request.customer_name, help_request.question))
    conn.commit()
    conn.close()
    return {"message": "Help request submitted successfully!"}

# 🛠 Supervisor UI Endpoint
@app.get("/supervisor", response_class=HTMLResponse)
def supervisor_ui(request: Request):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id, customer_name, question FROM help_requests WHERE status = "pending"')
    pending_requests = cursor.fetchall()
    cursor.execute('SELECT id, customer_name, question, status, answer FROM help_requests WHERE status != "pending"')
    history = cursor.fetchall()
    conn.close()
    return templates.TemplateResponse("supervisor.html", {
        "request": request,
        "pending_requests": pending_requests,
        "history": history
    })

# 🛠 Supervisor Submit Answer Endpoint
@app.post("/submit_answer")
def submit_answer(request_id: int = Form(...), answer: str = Form(...)):
    conn = create_connection()
    cursor = conn.cursor()
    # Get the question first
    cursor.execute('SELECT question FROM help_requests WHERE id = ?', (request_id,))
    row = cursor.fetchone()
    if not row:
        conn.close()
        raise HTTPException(status_code=404, detail="Request not found")
    
    question = row[0]
    
    # Update DB
    cursor.execute('''
        UPDATE help_requests
        SET status = 'resolved', answer = ?
        WHERE id = ? AND status = 'pending'
    ''', (answer, request_id))
    conn.commit()
    conn.close()

    # ✅ Update local knowledge base
    kb_file = "knowledge_base.json"
    if os.path.exists(kb_file):
        with open(kb_file, "r") as f:
            kb = json.load(f)
    else:
        kb = {}

    kb[question] = answer

    with open(kb_file, "w") as f:
        json.dump(kb, f, indent=4)

    return RedirectResponse("/supervisor", status_code=303)
