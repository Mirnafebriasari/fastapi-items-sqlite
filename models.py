# models.py
from sqlalchemy import Column, Integer, String, Float  # Mengimpor tipe data kolom dari SQLAlchemy
from database import Base  # Mengimpor Base sebagai dasar pembuatan tabel

class Item(Base):  # Membuat class Item yang akan menjadi tabel di database
    __tablename__ = "items"  # Menentukan nama tabel di database yaitu "items"

    id = Column(Integer, primary_key=True, index=True)  # Kolom id sebagai primary key
    name = Column(String, index=True)  # Kolom name untuk menyimpan nama item
    description = Column(String)  # Kolom description untuk menyimpan deskripsi item
    price = Column(Float)  # Kolom price untuk menyimpan harga item
