# database.py
from sqlalchemy import create_engine  # Mengimpor fungsi untuk membuat koneksi ke database
from sqlalchemy.ext.declarative import declarative_base  # Mengimpor Base untuk membuat model tabel
from sqlalchemy.orm import sessionmaker  # Mengimpor sessionmaker untuk membuat session database

DATABASE_URL = "sqlite:///./items.db"  # Menentukan database yang digunakan yaitu SQLite dengan file items.db

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)  # Membuat engine atau koneksi utama ke database SQLite

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)  # Membuat session database yang digunakan untuk menjalankan query (insert, update, select)

Base = declarative_base()  # Base class yang digunakan sebagai dasar untuk membuat tabel di models.py
