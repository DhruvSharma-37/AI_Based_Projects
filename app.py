from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models, schemas, crud
from database import SessionLocal, engine
from llm import summarize_text
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ✅ Create Note
@app.post("/notes", response_model=schemas.NoteResponse)
def create_note(note: schemas.NoteCreate, db: Session = Depends(get_db)):
    return crud.create_note(db, note.title, note.content)


# ✅ Get All Notes
@app.get("/notes", response_model=list[schemas.NoteResponse])
def read_notes(db: Session = Depends(get_db)):
    return crud.get_notes(db)


# ✅ Delete Note
@app.post("/delete/{note_id}")
def delete_note(note_id: int, db: Session = Depends(get_db)):
    return crud.delete_note(db, note_id)


# ✅ Summarize Note (LLM)
@app.post("/summarize")
def summarize(note: schemas.NoteCreate):
    summary = summarize_text(note.content)
    return {"summary": summary}