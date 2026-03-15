from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.meeting_router import router as meeting_router
from routers.zoom_router import router as zoom_router

app = FastAPI(
    title="Meeting AI",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(meeting_router)
app.include_router(zoom_router)

@app.get("/")
def root():
    return {"message": "Meeting AI API"}