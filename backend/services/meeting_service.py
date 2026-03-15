from models.meeting import Meeting
from services.openai_service import summarize_meeting

async def create_meeting(db, file):

    transcript, summary = await summarize_meeting(file)

    meeting = Meeting(
        filename=file.filename,
        transcript=transcript,
        summary=summary
    )

    db.add(meeting)

    db.commit()

    db.refresh(meeting)

    return meeting


def get_meetings(db):

    return db.query(Meeting).order_by(
        Meeting.id.desc()
    ).all()