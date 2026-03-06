# schemas.py
from pydantic import BaseModel

class ItemBase(BaseModel):
    name: str
    description: str
    price: float

class ItemResponse(ItemBase):
    id: int

    class Config:
        orm_mode = True