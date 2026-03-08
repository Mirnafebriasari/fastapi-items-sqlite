# main.py
from fastapi import FastAPI, Depends, HTTPException  # Mengimpor FastAPI untuk membuat API, Depends untuk dependency, HTTPException untuk menangani error
from sqlalchemy.orm import Session  # Mengimpor Session untuk mengakses database
import models  # Mengimpor file models yang berisi struktur tabel
import schemas  # Mengimpor file schemas yang berisi validasi data Pydantic
from database import SessionLocal, engine  # Mengimpor koneksi database dan session

models.Base.metadata.create_all(bind=engine)  # Membuat tabel di database jika belum ada

app = FastAPI()  # Membuat objek aplikasi FastAPI


# Dependency Injection
def get_db():
    db = SessionLocal()  # Membuat session database
    try:
        yield db  # Mengirim session database ke endpoint
    finally:
        db.close()  # Menutup koneksi database setelah selesai digunakan


# GET ALL ITEMS
@app.get("/items/", response_model=list[schemas.ItemResponse])  # Endpoint untuk mengambil semua data item
def get_items(db: Session = Depends(get_db)):  # Mengambil session database menggunakan dependency
    items = db.query(models.Item).all()  # Mengambil semua data dari tabel items
    return items  # Mengembalikan data item sebagai response


# GET ITEM BY ID
@app.get("/items/{item_id}", response_model=schemas.ItemResponse)  # Endpoint untuk mengambil item berdasarkan id
def get_item(item_id: int, db: Session = Depends(get_db)):  # Parameter item_id untuk mencari item
    item = db.query(models.Item).filter(models.Item.id == item_id).first()  # Mencari item berdasarkan id

    if item is None:  # Jika item tidak ditemukan
        raise HTTPException(status_code=404, detail="Item not found")  # Mengirim error 404

    return item  # Mengembalikan data item jika ditemukan
