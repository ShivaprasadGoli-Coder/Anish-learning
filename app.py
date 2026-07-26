"""
app.py — Anish's 11+ Learning App v2
Complete learning platform: Lesson → Practice → Review
"""
import os, random
from datetime import date, timedelta
from flask import Flask, render_template, request, redirect, url_for, abort, session as flask_session

from db import get_db, init_schema, test_connection

app = Flask(__name__)
app.secret_key = 'anish-11plus-2027-v2'
PARENT_MODE = os.environ.get('PARENT_MODE','0') == '1'
REVIEW_GAPS = [0, 2, 6, 13, 29]
REVIEW_LABELS = ["Learn","Day 3","Day 7","Day 14","Day 30"]
SUBJECT_COLORS = {'Maths':'#4F46E5','English':'#059669','Verbal Reasoning':'#DC2626'}
SUBJECT_EMOJIS = {'Maths':'🔢','English':'📚','Verbal Reasoning':'🧠'}

def next_review_date(session_date_str, stage, struggled=False):
    if struggled:
        return (date.fromisoformat(str(session_date_str)) + timedelta(days=2)).isoformat()
    if stage >= len(REVIEW_GAPS)-1:
        return None
    sd = date.fromisoformat(str(session_date_str))
    learn = sd - timedelta(days=REVIEW_GAPS[stage])
    return (learn + timedelta(days=REVIEW_GAPS[stage+1])).isoformat()

@app.context_processor
def inject_globals():
    return dict(parent_mode=PARENT_MODE, COLORS=SUBJECT_COLORS, EMOJIS=SUBJECT_EMOJIS)

# ── HOME ──────────────────────────────────────────────────────
@app.route('/')
def home():
    conn = get_db(); cur = conn.cursor()
    today = date.today().isoformat()
    cur.execute("SELECT COUNT(*) as c FROM topics WHERE archived=0")
    total = cur.fetchone()['c']
    cur.execute("SELECT COUNT(DISTINCT topic_id) as c FROM sessions")
    started = cur.fetchone()['c']
    cur.execute("SELECT COUNT(*) as c FROM (SELECT topic_id FROM sessions WHERE review_stage=4 GROUP BY topic_id) x")
    mastered = cur.fetchone()['c']
    cur.execute("""
        SELECT s.topic_id, s.next_review_date, t.title, t.subject, t.section, t.id as tid, s.review_stage
        FROM sessions s JOIN topics t ON t.id=s.topic_id
        WHERE s.id IN (SELECT MAX(id) FROM sessions GROUP BY topic_id)
        AND s.next_review_date <= %s ORDER BY s.next_review_date ASC LIMIT 6
    """, (today,))
    due = cur.fetchall()
    cur.execute("""
        SELECT s.*, t.title, t.subject FROM sessions s JOIN topics t ON t.id=s.topic_id
        ORDER BY s.id DESC LIMIT 6
    """)
    recent = cur.fetchall()
    cur.close(); conn.close()
    return render_template('home.html', total=total, started=started, mastered=mastered,
        due=due, recent=recent, today=today, REVIEW_LABELS=REVIEW_LABELS)

# ── SUBJECT ───────────────────────────────────────────────────
@app.route('/subject/<subject>')
def subject_view(subject):
    conn = get_db(); cur = conn.cursor()
    cur.execute("""
        SELECT t.*,
            (SELECT COUNT(*) FROM sessions s WHERE s.topic_id=t.id) as sessions_done,
            (SELECT MAX(review_stage) FROM sessions s WHERE s.topic_id=t.id) as max_stage,
            (SELECT next_review_date FROM sessions s WHERE s.topic_id=t.id ORDER BY id DESC LIMIT 1) as next_review,
            (SELECT score FROM sessions s WHERE s.topic_id=t.id ORDER BY id DESC LIMIT 1) as last_score,
            (SELECT total_questions FROM sessions s WHERE s.topic_id=t.id ORDER BY id DESC LIMIT 1) as last_total
        FROM topics t WHERE t.subject=%s AND t.archived=0 ORDER BY t.section, t.id
    """, (subject,))
    topics = cur.fetchall()
    sections = {}
    for t in topics:
        sections.setdefault(t['section'], []).append(t)
    cur.close(); conn.close()
    return render_template('subject.html', subject=subject, sections=sections,
        color=SUBJECT_COLORS.get(subject,'#4F46E5'), emoji=SUBJECT_EMOJIS.get(subject,'📖'),
        REVIEW_LABELS=REVIEW_LABELS)

# ── LEARN (lesson page) ───────────────────────────────────────
@app.route('/learn/<int:topic_id>')
def learn(topic_id):
    conn = get_db(); cur = conn.cursor()
    cur.execute("SELECT * FROM topics WHERE id=%s", (topic_id,))
    topic = cur.fetchone()
    if not topic: abort(404)
    cur.execute("SELECT COUNT(*) as c FROM questions WHERE topic_id=%s", (topic_id,))
    q_count = cur.fetchone()['c']
    cur.execute("SELECT * FROM sessions WHERE topic_id=%s ORDER BY id DESC LIMIT 1", (topic_id,))
    latest = cur.fetchone()
    cur.close(); conn.close()
    current_stage = latest['review_stage'] if latest else None
    return render_template('learn.html', topic=topic, q_count=q_count,
        current_stage=current_stage, REVIEW_LABELS=REVIEW_LABELS,
        color=SUBJECT_COLORS.get(topic['subject'],'#4F46E5'))

# ── QUIZ ──────────────────────────────────────────────────────
@app.route('/quiz/<int:topic_id>')
def quiz(topic_id):
    if PARENT_MODE: return redirect(url_for('learn', topic_id=topic_id))
    conn = get_db(); cur = conn.cursor()
    cur.execute("SELECT * FROM topics WHERE id=%s", (topic_id,))
    topic = cur.fetchone()
    if not topic: abort(404)
    cur.execute("SELECT * FROM questions WHERE topic_id=%s ORDER BY difficulty ASC", (topic_id,))
    all_qs = list(cur.fetchall())
    cur.execute("SELECT * FROM sessions WHERE topic_id=%s ORDER BY id DESC LIMIT 1", (topic_id,))
    latest = cur.fetchone()
    cur.close(); conn.close()
    if not all_qs: return redirect(url_for('learn', topic_id=topic_id))
    # Mix difficulties: 2 easy, 2 medium, 1 hard
    easy = [q for q in all_qs if q['difficulty']==1]
    med  = [q for q in all_qs if q['difficulty']==2]
    hard = [q for q in all_qs if q['difficulty']==3]
    random.shuffle(easy); random.shuffle(med); random.shuffle(hard)
    questions = (easy[:7] + med[:7] + hard[:6]) or all_qs[:10]
    current_stage = latest['review_stage'] if latest else None
    next_stage = 0 if current_stage is None else (min(current_stage+1, 4))
    return render_template('quiz.html', topic=topic, questions=questions, next_stage=next_stage, COLORS=COLORS, EMOJIS=EMOJIS, parent_mode=PARENT_MODE)

@app.route('/quiz/<int:topic_id>/submit', methods=['POST'])
def quiz_submit(topic_id):
    if PARENT_MODE: abort(403)
    conn = get_db(); cur = conn.cursor()
    cur.execute("SELECT * FROM topics WHERE id=%s", (topic_id,))
    topic = cur.fetchone()
    data = request.form
    qids = data.getlist('question_ids')
    score = 0; results = []
    for qid in qids:
        cur.execute("SELECT * FROM questions WHERE id=%s", (int(qid),))
        q = cur.fetchone()
        if not q: continue
        user_ans = data.get(f'answer_{qid}','').strip()
        is_correct = user_ans.lower() == q['correct_answer'].strip().lower()
        if is_correct: score += 1
        results.append({'question':q,'user_answer':user_ans,'correct':is_correct})
    total = len(results)
    next_stage = int(data.get('next_stage',0))
    today = date.today().isoformat()
    pct = int((score/total*100)) if total>0 else 0
    rating = 'great' if pct>=80 else ('ok' if pct>=50 else 'struggled')
    nrd = next_review_date(today, next_stage, rating=='struggled')
    cur.execute("""
        INSERT INTO sessions (topic_id, session_date, session_type, review_stage,
            rating, score, total_questions, next_review_date, created_at)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """, (topic_id, today, 'learn' if next_stage==0 else 'review',
          next_stage, rating, score, total, nrd, today))
    conn.commit(); cur.close(); conn.close()
    return render_template('results.html', topic=topic, results=results,
        score=score, total=total, pct=pct, rating=rating, next_review=nrd,
        REVIEW_LABELS=REVIEW_LABELS,
        color=SUBJECT_COLORS.get(topic['subject'],'#4F46E5'))

# ── PROGRESS ──────────────────────────────────────────────────
@app.route('/progress')
def progress():
    conn = get_db(); cur = conn.cursor()
    cur.execute("SELECT COUNT(*) as c FROM topics WHERE archived=0")
    total = cur.fetchone()['c']
    cur.execute("SELECT COUNT(DISTINCT topic_id) as c FROM sessions")
    started = cur.fetchone()['c']
    cur.execute("SELECT COUNT(*) as c FROM (SELECT topic_id FROM sessions WHERE review_stage=4 GROUP BY topic_id) x")
    mastered = cur.fetchone()['c']
    cur.execute("""
        SELECT t.subject, COUNT(DISTINCT t.id) as total_t,
            COUNT(DISTINCT s.topic_id) as started_t,
            COALESCE(SUM(s.score),0) as tot_score,
            COALESCE(SUM(s.total_questions),0) as tot_q
        FROM topics t LEFT JOIN sessions s ON s.topic_id=t.id
        WHERE t.archived=0 GROUP BY t.subject ORDER BY t.subject
    """)
    by_sub = cur.fetchall()
    cur.execute("""
        SELECT s.*, t.title, t.subject FROM sessions s JOIN topics t ON t.id=s.topic_id
        ORDER BY s.id DESC LIMIT 12
    """)
    recent = cur.fetchall()
    cur.execute("""
        SELECT t.title, t.subject, s.score, s.total_questions, s.session_date
        FROM sessions s JOIN topics t ON t.id=s.topic_id
        WHERE s.rating='struggled' AND s.id IN (SELECT MAX(id) FROM sessions GROUP BY topic_id)
        ORDER BY s.session_date DESC LIMIT 6
    """)
    weak = cur.fetchall()
    cur.close(); conn.close()
    return render_template('progress.html', total=total, started=started, mastered=mastered,
        by_sub=by_sub, recent=recent, weak=weak, COLORS=SUBJECT_COLORS, EMOJIS=SUBJECT_EMOJIS)

if __name__ == '__main__':
    ok, msg = test_connection()
    if not ok:
        print(f"\n{'='*60}\n  COULD NOT CONNECT TO DATABASE\n  {msg}\n  Check config.py\n{'='*60}\n")
        raise SystemExit(1)
    init_schema()
    from content import seed_all_content
    _c = get_db(); seed_all_content(_c); _c.close()
    mode = "PARENT VIEW" if PARENT_MODE else "FULL ACCESS"
    print(f"\n{'='*60}\n  Anish's 11+ Learning App — {mode}\n  Connected ✓\n  Open: http://127.0.0.1:5151\n{'='*60}\n")
    port = int(os.environ.get('PORT', 5151))
    host = '0.0.0.0' if os.environ.get('PORT') else '127.0.0.1'
    if not os.environ.get('PORT'):
        import threading, webbrowser
        def open_browser():
            import time; time.sleep(1.5)
            webbrowser.open('http://127.0.0.1:5151')
        threading.Thread(target=open_browser, daemon=True).start()
    app.run(host=host, port=port, debug=False)
