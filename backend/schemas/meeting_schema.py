from pydantic import BaseModel

class MeetingCreate(BaseModel):

    filename: str
    transcript: str
    summary: str


class MeetingResponse(MeetingCreate):

    id: int

    class Config:
        from_attributes = True