from pydantic import BaseModel, ConfigDict

# shared base field
class NoteBase(BaseModel):
    title: str
    content: str

# for creation
class NoteCreate(NoteBase):
    pass

# for full update(put)
class NoteUpdate(NoteBase):
    pass

# for partial update(patch)
class NotePatch(BaseModel):
    title: str | None = None
    content: str | None = None


# for response serialization
class NooteOut(NoteBase):
    id: int
    model_config = ConfigDict(from_attributes=True)