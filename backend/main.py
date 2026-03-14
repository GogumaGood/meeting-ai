from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI
import os
from dotenv import load_dotenv
import tempfile
from meeting_service import save_meeting
from db import cursor

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI()

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

@app.get("/loadMeeting")
def get_meetings():

    cursor.execute("SELECT * FROM meetings ORDER BY id DESC")

    rows = cursor.fetchall()

    meetings = []

    for r in rows:
        meetings.append({
            "id": r[0],
            "filename": r[1],
            "transcript": r[2],
            "summary": r[3],
            "created_at": str(r[4])
        })

    return meetings

@app.post("/uploadMeeting")
async def meeting_summary(file: UploadFile = File(...)):
    # 임시 파일 생성
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp:
        content = await file.read()
        temp.write(content)
        temp_path = temp.name

    # Whisper 호출
    with open(temp_path, "rb") as audio:
        # 1️⃣ 음성 → 텍스트
        transcript = client.audio.transcriptions.create(
            model="gpt-4o-transcribe",
            file=audio
        )

    os.remove(temp_path)

    text = transcript.text

    print("file.filename", file.filename)
    print("file.content_type", file.content_type)
    print("text", text)

    # 2️⃣ 텍스트 → 요약
    completion = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "회의 내용을 요약하고 Action Items와 Decisions를 정리해라"},
            {"role": "user", "content": text}
        ]
    )

    summary = completion.choices[0].message.content

    # 3️⃣ DB 저장
    save_meeting(
        file.filename,
        text,
        summary
    )

    return {
        "transcript": text,
        "summary": summary
    }