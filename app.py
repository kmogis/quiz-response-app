from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

app = FastAPI()

class Submission(BaseModel):
    name: str
    answer: str

@app.post("/submit")
def submit_response(submission: Submission):
    conn = sqlite3.connect("responses.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS responses (name TEXT, answer TEXT)")
    cursor.execute("INSERT INTO responses (name, answer) VALUES (?, ?)", (submission.name, submission.answer))
    conn.commit()
    conn.close()
    return {"message": "Response recorded"}
