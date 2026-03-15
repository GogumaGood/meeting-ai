from fastapi import APIRouter, Request

router = APIRouter(prefix="/zoom")

@router.post("/webhook")
async def zoom_webhook(request: Request):

    payload = await request.json()

    event = payload.get("event")

    if event == "recording.completed":

        recording_files = payload["payload"]["object"]["recording_files"]

        download_url = recording_files[0]["download_url"]

        return {
            "message": "Recording received",
            "url": download_url
        }

    return {"message": "ignored"}