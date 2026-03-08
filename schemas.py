# schemas.py
from pydantic import BaseModel  # Mengimpor BaseModel dari Pydantic untuk membuat schema data

class ItemBase(BaseModel):  # Membuat schema dasar untuk data item
    name: str  # Field name bertipe string
    description: str  # Field description bertipe string
    price: float  # Field price bertipe angka desimal

class ItemResponse(ItemBase):  # Schema untuk response API yang mewarisi ItemBase
    id: int  # Menambahkan field id sebagai identitas item

    class Config:  # Konfigurasi tambahan untuk schema
        orm_mode = True  # Mengizinkan Pydantic membaca data dari objek ORM (SQLAlchemy)
