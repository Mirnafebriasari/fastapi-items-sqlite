Hands-on: Implementasi 2 endpoint GET dengan FastAPI + SQLAlchemy + SQLite + Pydantic validation
Fitur
| Endpoint         | Method | Deskripsi                     | Response Model     |
| ---------------- | ------ | ----------------------------- | ------------------ |
| /items/          | GET    | List semua items (pagination) | List[ItemResponse] |
| /items/{item_id} | GET    | Get item by ID                | ItemResponse       |

📁 Struktur Project
fastapi-items-sqlite/
├── database.py      # Database config & session
├── main.py          # FastAPI app & endpoints  
├── models.py        # SQLAlchemy ORM models
├── schemas.py       # Pydantic schemas (validation)   
└── requirements.txt # Dependencies

Installation & Run
# Clone repo
git clone https://github.com/Mirnafebriasari/fastapi-items-sqlite.git
cd fastapi-items-sqlite

# Virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Jalankan di terminal
uvicorn main:app --reload

# Jalankan di server
http://127.0.0.1:8000/docs

# Swagger UI

