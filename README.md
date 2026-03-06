## FastAPI Items API

Proyek ini adalah **API sederhana menggunakan FastAPI dan SQLite** untuk mengelola data items.  
Mendukung operasi **Read (GET)**  melalui dua endpoint utama:  

| Endpoint         | Method | Deskripsi                                           | Response Model     |
| ---------------- | ------ | --------------------------------------------------- | ------------------ |
| /items/          | GET    | Mengambil semua item                                | List[ItemResponse] |
| /items/{item_id} | GET    | mengambil satu item berdasarkan ID                  | ItemResponse       |

### Tujuan Proyek
Proyek ini bertujuan untuk membuat **API sederhana menggunakan FastAPI dan SQLite** untuk mengelola data items.  
Hands-on ini mengimplementasikan **FastAPI + SQLAlchemy + SQLite** dengan **validasi Pydantic** untuk memastikan data output sesuai format, serta membiasakan penggunaan **Swagger UI** untuk dokumentasi interaktif.

📁 Struktur Project

```bash
fastapi-items-sqlite/
├── database.py      # Database config & session
├── main.py          # FastAPI app & endpoints  
├── models.py        # SQLAlchemy ORM models
├── schemas.py       # Pydantic schemas (validation)   
└── requirements.txt # Dependencies
```

### Installation & Run
**Clone repo** 

1. git clone https://github.com/Mirnafebriasari/fastapi-items-sqlite.git
2. cd fastapi-items-sqlite

**Virtual environment**
```bash
1. python -m venv .venv
2. source .venv/bin/activate  # Linux/Mac
3. .venv\Scripts\activate   # Windows
```
**Install dependencies**
```bash
pip install -r requirements.txt
```
**Jalankan di terminal**
```bash
uvicorn main:app --reload
```
**Jalankan di server**
```bash
http://127.0.0.1:8000/docs
```
### Swagger UI

