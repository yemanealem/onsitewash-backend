# OnsiteWash Backend

FastAPI backend for OnsiteWash quote and email system.

## Features

- Quote submission API
- Email confirmation to customer
- Clean architecture
- Email templates
- Documentation
- PostgreSQL ready

## Tech Stack

- FastAPI
- PostgreSQL
- SQLAlchemy
- Jinja2 (templates)
- SMTP email
- Python

## Setup

### 1. Clone Repository

```bash
git clone https://github.com/yemanealem/onsitewash-backend.git
cd onsitewash-backend
```

python -m venv venv

venv\Scripts\Activate [Window]
source venv/bin/activate [Linux/Mac]

pip install -r requirements.txt

DATABASE_URL=postgresql://user:password@localhost/onsitewash
EMAIL_FROM=info@onsitewash.se
OWNER_EMAIL=owner@onsitewash.se

SMTP_HOST=smtp.gmail.com
SMTP_USER=your_email@gmail.com
SMTP_PASS=your_app_password

uvicorn app.main:app --reload

Server
http://127.0.0.1:8000/docs

API DOC
http://127.0.0.1:8000/docs

onsitewash-backend/
│
├── app/
│ ├── api/
│ │ └── v1/
│ ├── core/
│ ├── db/
│ ├── models/
│ ├── schemas/
│ ├── services/
│ ├── templates/
│ │ └── email/
│ └── utils/
│
├── tests/
├── docs/
├── .env
├── requirements.txt
└── README.md
