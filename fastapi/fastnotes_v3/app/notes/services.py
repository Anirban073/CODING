from app.db.config import async_session
from app.notes.models import Note
from sqlalchemy import select
from fastapi import HTTPException
from app.notes.schemas import NoteCreate, NoteUpdate, NotePatch, NooteOut
from sqlalchemy.ext.asyncio import AsyncSession

# async def create_note(new_note: NoteCreate, session:AsyncSession)-> NooteOut:

# create note
async def create_note(session: AsyncSession, new_note: NoteCreate) -> NooteOut:
        note = Note(title=new_note.title, content=new_note.content)
        session.add(note)
        await session.commit()
        await session.refresh(note)
        return note
    
# get node
async def get_note(session: AsyncSession, note_id: int) -> NooteOut:
        note = await session.get(Note, note_id)
        if note is None:
            raise HTTPException(status_code=404, detail="note not found")
        return note
    

# get all notes
async def get_all_notes(session: AsyncSession, ) -> list[NooteOut]:
        stmt = select(Note)
        notes = await session.scalars(stmt)
        return notes.all()
    

# update notes
async def update_note(session: AsyncSession, note_id:int, new_note: NoteUpdate) -> NooteOut:
        note = await session.get(Note, note_id)
        if note is None:
            raise HTTPException(status_code=404, detail="Note not found")
        note.title = new_note.title
        note.content = new_note.content

        await session.commit()
        await session.refresh(note)
        return note
    

# patch notes
async def patch_note(session: AsyncSession, note_id:int, new_note: NotePatch) -> NooteOut:
        note = await session.get(Note, note_id)
        if note is None:
            raise HTTPException(status_code=404, detail="Note not found")
        if new_note.title:
            note.title =new_note.title
        if new_note.content:
            note.content = new_note.content

        await session.commit()
        await session.refresh(note)
        return note
    

# delete note
async def delete_note(session: AsyncSession, note_id: int):
        note = await session.get(Note, note_id)
        if note is None:
            raise HTTPException(status_code=404, detail="Note not found")
        await session.delete(note)
        await session.commit()
        return {"message" : "note successfully deleted"}