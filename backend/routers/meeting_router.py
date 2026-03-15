from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session

from database.database import get_db
from schemas.meeting_schema import MeetingCreate
from services.meeting_service import create_meeting, get_meetings

router = APIRouter(prefix="")

@router.post("/uploadMeeting")
async def create(file: UploadFile = File(...), db: Session = Depends(get_db)):

    return await create_meeting(db, file)


@router.get("/loadMeeting")
def list_meetings(db: Session = Depends(get_db)):

    return get_meetings(db)