from pydantic import BaseModel

class PostCreate(BaseModel):
    text: str

class PostResponse(BaseModel):
    id: int
    text: str
    owner_id: int

    class Config:
        orm_mode = True
