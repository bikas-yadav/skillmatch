SkillMatch — AI-Powered Resume → Job Description Matcher (FastAPI + NLP)

SkillMatch is an intelligent resume-to-job description matching engine built with Python, FastAPI, scikit-learn, and TF-IDF.
It analyzes a candidate’s resume and compares it with multiple job descriptions, then returns:

🔥 Top matching jobs

🎯 Similarity scores

🧠 Matched skills

❗ Missing keywords

This is designed for:

Job seekers optimizing their resumes

Recruiters quickly filtering top candidates

Developers showcasing backend + NLP skills


Run locally:

uvicorn app.main:app --reload --port 8000


Then open Swagger interactive docs:

👉 http://127.0.0.1:8000/docs

✨ Features

✔ Upload or paste resume text
✔ Add multiple job descriptions
✔ Computes TF-IDF vectors
✔ Ranks jobs by cosine similarity
✔ Extracts & highlights matched keywords
✔ API built with FastAPI
✔ Auto-generated Swagger UI
✔ Fully dockerized
✔ Unit tests (pytest)
✔ Clean modular structure

🧠 Tech Stack

Backend:

Python 3.10+

FastAPI

Uvicorn

scikit-learn

NumPy

Pydantic

Testing:

pytest

Tools:

Docker

GitHub Actions (optional CI)

VS Code

📁 Project Structure
skillmatch/
├── app/
│   ├── main.py           # FastAPI entry point
│   ├── matcher.py        # NLP & matching logic
│   ├── schemas.py        # Pydantic models
│   └── __init__.py
├── tests/
│   └── test_matcher.py   # Unit tests
├── requirements.txt
├── Dockerfile
├── .gitignore
└── README.md

🚀 Quick Start (Local Development)
1) Clone repository
git clone https://github.com/bikas-yadav/skillmatch.git
cd skillmatch

2) Create & activate virtual environment

Windows

python -m venv .venv
.venv\Scripts\activate


macOS/Linux

python3 -m venv .venv
source .venv/bin/activate

3) Install dependencies
pip install -r requirements.txt

4) Run server
uvicorn app.main:app --reload --port 8000


Open interactive API docs:
👉 http://127.0.0.1:8000/docs

🧪 Run Tests
pytest -q

🐳 Run with Docker
Build image:
docker build -t skillmatch .

Run container:
docker run -p 8000:8000 skillmatch


Open: http://127.0.0.1:8000/docs

📌 Example API Request

POST /match

Request Body:
{
  "resume_text": "Experienced Python developer with FastAPI, Docker, and SQL experience.",
  "job_descriptions": [
    {
      "id": "job1",
      "title": "Backend Python Developer",
      "description": "Python, FastAPI, Docker, PostgreSQL, REST APIs"
    },
    {
      "id": "job2",
      "title": "Data Engineer",
      "description": "Python, ETL, Spark, Hadoop"
    }
  ],
  "top_n": 2
}

🔍 API Response Example
{
  "matches": [
    {
      "id": "job1",
      "title": "Backend Python Developer",
      "score": 0.7231,
      "matched_keywords": ["python", "fastapi", "docker", "sql"],
      "missing_keywords": ["postgresql", "rest"]
    },
    {
      "id": "job2",
      "title": "Data Engineer",
      "score": 0.3419,
      "matched_keywords": ["python"],
      "missing_keywords": ["spark", "hadoop", "etl"]
    }
  ]
}

🧭 Future Enhancements (Roadmap)

📄 PDF resume parsing (PyPDF2 / pdfminer)

🧬 Upgrade TF-IDF → spaCy or BERT embeddings

🌐 Web UI (React / Next.js)

🔐 User authentication

📊 Dashboard with match analytics
