from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS 설정
origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Meeting(BaseModel):
    text: str

@app.post("/summarize")
def summarize(meeting: Meeting):

    return {
        "summary": "회의 요약: " + meeting.text
    }