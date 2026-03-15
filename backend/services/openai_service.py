from openai import OpenAI
from core.config import OPENAI_API_KEY
import os
import tempfile

client = OpenAI(api_key=OPENAI_API_KEY)

async def summarize_meeting(file):

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

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system", 
                "content": "회의 내용을 요약하고 Action Items와 Decisions를 정리해라"
            },
            {
                "role": "user",
                "content": text
            }
        ]
    )

    return text, response.choices[0].message.content