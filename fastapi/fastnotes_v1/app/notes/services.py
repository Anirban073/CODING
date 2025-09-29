from app.db.config import async_session
from app.notes.models import Note
from sqlalchemy import select
from fastapi import HTTPException

# create note
async def create_note(title: str, content: str):
    async with async_session() as session:
        note = Note(title=title, content=content)
        session.add(note)
        await session.commit()
        await session.refresh(note)
        return note
    
# get node
async def get_note(note_id: int):
    async with async_session() as session:
        note = await session.get(Note, note_id)
        if note is None:
            raise HTTPException(status_code=404, detail="note not found")
        return note
    

# get all notes
async def get_all_notes():
    async with async_session() as session:
        stmt = select(Note)
        notes = await session.scalars(stmt)
        return notes.all()
    

# update notes
async def update_note(note_id:int, new_title:str, new_content:str):
    async with async_session() as session:
        note = await session.get(Note, note_id)
        if note is None:
            raise HTTPException(status_code=404, detail="Note not found")
        note.title = new_title
        note.content = new_content

        await session.commit()
        await session.refresh(note)
        return note
    

# patch notes
async def patch_note(note_id:int, new_title:str | None=None, new_content:str | None=None):
    async with async_session() as session:
        note = await session.get(Note, note_id)
        if note is None:
            raise HTTPException(status_code=404, detail="Note not found")
        if new_title:
            note.title = new_title
        if new_content:
            note.content = new_content

        await session.commit()
        await session.refresh(note)
        return note
    

# delete note
async def delete_note(note_id: int):
    async with async_session() as session:
        note = await session.get(Note, note_id)
        if note is None:
            raise HTTPException(status_code=404, detail="Note not found")
        await session.delete(note)
        await session.commit()
        return {"message" : "note successfully deleted"}