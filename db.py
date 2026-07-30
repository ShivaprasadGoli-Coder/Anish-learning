"""db.py — Database layer using Supabase (Postgres)."""
import os
import psycopg2
import psycopg2.extras
from datetime import date

SCHEMA = """
CREATE TABLE IF NOT EXISTS topics (
    id SERIAL PRIMARY KEY,
    subject TEXT NOT NULL DEFAULT 'Maths',
    section TEXT NOT NULL,
    title TEXT NOT NULL,
    lesson_html TEXT,
    source TEXT,
    created_at DATE NOT NULL,
    archived INTEGER NOT NULL DEFAULT 0
);
CREATE TABLE IF NOT EXISTS questions (
    id SERIAL PRIMARY KEY,
    topic_id INTEGER NOT NULL REFERENCES topics(id),
    question_text TEXT NOT NULL,
    question_type TEXT NOT NULL,
    option_a TEXT, option_b TEXT, option_c TEXT, option_d TEXT, option_e TEXT,
    correct_answer TEXT NOT NULL,
    explanation TEXT,
    difficulty INTEGER DEFAULT 1
);
ALTER TABLE questions ADD COLUMN IF NOT EXISTS option_e TEXT;
CREATE TABLE IF NOT EXISTS sessions (
    id SERIAL PRIMARY KEY,
    topic_id INTEGER NOT NULL REFERENCES topics(id),
    session_date DATE NOT NULL,
    session_type TEXT NOT NULL,
    review_stage INTEGER DEFAULT 0,
    rating TEXT,
    score INTEGER DEFAULT 0,
    total_questions INTEGER DEFAULT 0,
    notes TEXT,
    next_review_date DATE,
    created_at DATE NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_sessions_topic ON sessions(topic_id);
CREATE INDEX IF NOT EXISTS idx_sessions_next_review ON sessions(next_review_date);
CREATE INDEX IF NOT EXISTS idx_questions_topic ON questions(topic_id);
"""

def get_connection_string():
    url = os.environ.get('DATABASE_URL')
    if url:
        return url
    try:
        import config
        return config.DATABASE_URL
    except (ImportError, AttributeError):
        raise RuntimeError("No database connection! Copy config.example.py to config.py")

def get_db():
    return psycopg2.connect(get_connection_string(), cursor_factory=psycopg2.extras.RealDictCursor)

def init_schema():
    conn = get_db()
    cur = conn.cursor()
    cur.execute(SCHEMA)
    conn.commit()
    cur.close()
    conn.close()

def test_connection():
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT 1")
        cur.fetchone()
        cur.close()
        conn.close()
        return True, "Connection successful!"
    except Exception as e:
        return False, str(e)
