"""
app.py — Anish's 11+ Learning App v2
ONE QUESTION PER PAGE — no JavaScript, works perfectly on iPad
"""
import os, random
from datetime import date, timedelta
from flask import Flask, render_template, request, redirect, url_for, abort, session as flask_session, Response

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
    cur.execute("""SELECT s.topic_id, s.next_review_date, t.title, t.subject, t.section, t.id as tid, s.review_stage
        FROM sessions s JOIN topics t ON t.id=s.topic_id
        WHERE s.id IN (SELECT MAX(id) FROM sessions GROUP BY topic_id)
        AND s.next_review_date <= %s ORDER BY s.next_review_date ASC LIMIT 6""", (today,))
    due = cur.fetchall()
    cur.execute("SELECT s.*, t.title, t.subject FROM sessions s JOIN topics t ON t.id=s.topic_id ORDER BY s.id DESC LIMIT 6")
    recent = cur.fetchall()
    cur.close(); conn.close()
    return render_template('home.html', total=total, started=started, mastered=mastered,
        due=due, recent=recent, today=today, REVIEW_LABELS=REVIEW_LABELS)

@app.route('/subject/<subject>')
def subject_view(subject):
    conn = get_db(); cur = conn.cursor()
    cur.execute("""SELECT t.*,
        (SELECT MAX(review_stage) FROM sessions s WHERE s.topic_id=t.id) as max_stage,
        (SELECT next_review_date FROM sessions s WHERE s.topic_id=t.id ORDER BY id DESC LIMIT 1) as next_review,
        (SELECT score FROM sessions s WHERE s.topic_id=t.id ORDER BY id DESC LIMIT 1) as last_score,
        (SELECT total_questions FROM sessions s WHERE s.topic_id=t.id ORDER BY id DESC LIMIT 1) as last_total
        FROM topics t WHERE t.subject=%s AND t.archived=0 ORDER BY t.section, t.id""", (subject,))
    topics = cur.fetchall()
    sections = {}
    for t in topics:
        sections.setdefault(t['section'], []).append(t)
    cur.close(); conn.close()
    return render_template('subject.html', subject=subject, sections=sections,
        color=SUBJECT_COLORS.get(subject,'#4F46E5'), emoji=SUBJECT_EMOJIS.get(subject,'📖'),
        REVIEW_LABELS=REVIEW_LABELS)

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

def make_q_page(topic, q, qnum, total, color, next_stage, prev_data):
    diff = 'Easy' if q['difficulty']==1 else 'Medium' if q['difficulty']==2 else 'Hard'
    pct = int(((qnum-1)/total)*100)
    safe_title = str(topic['title']).replace('<','&lt;').replace('>','&gt;')
    safe_q = str(q['question_text']).replace('<','&lt;').replace('>','&gt;')

    opts = ''
    if q['question_type'] == 'mc':
        for val, ltr in [(q['option_a'],'A'),(q['option_b'],'B'),(q['option_c'],'C'),(q['option_d'],'D')]:
            if val:
                sv = str(val).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;').replace('"','&quot;')
                opts += '<button type="submit" name="ans" value="{v}" style="width:100%;padding:16px 18px;margin:8px 0;border-radius:14px;border:2px solid #2A2A4A;background:rgba(255,255,255,0.03);font-size:16px;font-weight:700;cursor:pointer;text-align:left;font-family:inherit;color:white;display:flex;align-items:center;gap:12px;touch-action:manipulation;-webkit-appearance:none;transition:background 0.1s,border-color 0.1s;"><span style="width:34px;height:34px;border-radius:50%;background:#2A2A4A;display:inline-flex;align-items:center;justify-content:center;font-weight:900;font-size:13px;flex-shrink:0;">{l}</span><span>{v}</span></button>'.format(v=sv,l=ltr)
    else:
        opts = '<input type="text" name="ans" placeholder="Type your answer..." autocomplete="off" style="width:100%;padding:14px;border-radius:14px;border:2px solid #2A2A4A;font-size:16px;font-weight:700;font-family:inherit;background:rgba(255,255,255,0.05);color:white;margin-bottom:12px;display:block;"><button type="submit" style="width:100%;padding:16px;border-radius:50px;background:{c};color:white;border:none;font-size:16px;font-weight:800;cursor:pointer;font-family:inherit;touch-action:manipulation;">Next</button>'.format(c=color)

    hidden = '<input type="hidden" name="next_stage" value="{0}"><input type="hidden" name="qnum" value="{1}"><input type="hidden" name="qid" value="{2}">'.format(next_stage, qnum, q['id'])
    for k,v in prev_data.items():
        sv = str(v).replace('&','&amp;').replace('"','&quot;')
        hidden += '<input type="hidden" name="prev_{0}" value="{1}">'.format(k, sv)

    return Response('''<!DOCTYPE html><html><head><meta charset=UTF-8><meta name=viewport content="width=device-width,initial-scale=1"><title>Quiz</title><style>*{{box-sizing:border-box;margin:0;padding:0}}body{{font-family:-apple-system,sans-serif;background:#0A0A1A;color:white}}</style></head><body>
<div style="background:#1A1A35;border-bottom:1px solid #2A2A4A;padding:14px 16px;position:sticky;top:0;">
  <div style="font-size:13px;font-weight:900;margin-bottom:4px;">{title}</div>
  <div style="font-size:12px;color:rgba(255,255,255,0.5);margin-bottom:6px;">Question {qnum} of {total}</div>
  <div style="background:rgba(255,255,255,0.1);border-radius:50px;height:6px;overflow:hidden;"><div style="width:{pct}%;height:100%;border-radius:50px;background:{color};"></div></div>
</div>
<div style="max-width:700px;margin:0 auto;padding:16px;">
<div style="background:#1A1A35;border:1px solid #2A2A4A;border-radius:16px;padding:20px;margin-bottom:12px;">
<div style="font-size:10px;font-weight:800;text-transform:uppercase;color:rgba(255,255,255,0.4);margin-bottom:12px;letter-spacing:1px;">{diff}</div>
<div style="font-size:17px;font-weight:800;line-height:1.6;color:white;margin-bottom:18px;">{q}</div>
<form method=post action=/quiz/{tid}/answer>{hidden}{opts}</form>
</div>
<a href="javascript:history.back()" style="background:rgba(255,255,255,0.1);color:white;border:1px solid #2A2A4A;padding:10px 20px;border-radius:50px;font-weight:800;font-size:13px;margin-right:8px;">← Previous</a><a href=/learn/{tid} style="color:rgba(255,255,255,0.4);font-size:13px;font-weight:700;text-decoration:none;">Back to Lesson</a>
</div></body></html>'''.format(title=safe_title,qnum=qnum,total=total,pct=pct,color=color,diff=diff,q=safe_q,tid=topic['id'],hidden=hidden,opts=opts), mimetype='text/html')

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
    easy = [q for q in all_qs if q['difficulty']==1]
    med  = [q for q in all_qs if q['difficulty']==2]
    hard = [q for q in all_qs if q['difficulty']==3]
    random.shuffle(easy); random.shuffle(med); random.shuffle(hard)
    questions = (easy[:4] + med[:4] + hard[:2]) or all_qs[:10]
    flask_session['quiz_{0}'.format(topic_id)] = [dict(q) for q in questions]
    current_stage = latest['review_stage'] if latest else None
    next_stage = 0 if current_stage is None else min(current_stage+1, 4)
    color = SUBJECT_COLORS.get(topic['subject'], '#4F46E5')
    return make_q_page(topic, questions[0], 1, len(questions), color, next_stage, {})

@app.route('/quiz/<int:topic_id>/answer', methods=['POST'])
def quiz_answer(topic_id):
    conn = get_db(); cur = conn.cursor()
    cur.execute("SELECT * FROM topics WHERE id=%s", (topic_id,))
    topic = cur.fetchone()
    cur.close(); conn.close()
    if not topic: abort(404)
    color = SUBJECT_COLORS.get(topic['subject'], '#4F46E5')
    qnum = int(request.form.get('qnum', 1))
    next_stage = int(request.form.get('next_stage', 0))
    qid = request.form.get('qid')
    ans = request.form.get('ans', '').strip()
    prev_data = {}
    for k, v in request.form.items():
        if k.startswith('prev_'):
            prev_data[k[5:]] = v
    prev_data[str(qid)] = ans
    questions = flask_session.get('quiz_{0}'.format(topic_id), [])
    total = len(questions)
    if qnum < total:
        next_q = questions[qnum]
        return make_q_page(topic, next_q, qnum+1, total, color, next_stage, prev_data)
    else:
        conn = get_db(); cur = conn.cursor()
        score = 0; results = []
        for q_dict in questions:
            qid_str = str(q_dict['id'])
            cur.execute("SELECT * FROM questions WHERE id=%s", (int(qid_str),))
            q = cur.fetchone()
            if not q: continue
            user_ans = prev_data.get(qid_str, '').strip()
            is_correct = user_ans.lower() == q['correct_answer'].strip().lower()
            if is_correct: score += 1
            results.append({'question':q,'user_answer':user_ans,'correct':is_correct})
        total_answered = len(results)
        today = date.today().isoformat()
        pct = int((score/total_answered*100)) if total_answered > 0 else 0
        rating = 'great' if pct>=80 else ('ok' if pct>=50 else 'struggled')
        nrd = next_review_date(today, next_stage, rating=='struggled')
        cur.execute("""INSERT INTO sessions (topic_id, session_date, session_type, review_stage,
            rating, score, total_questions, next_review_date, created_at)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
            (topic_id, today, 'learn' if next_stage==0 else 'review',
             next_stage, rating, score, total_answered, nrd, today))
        conn.commit(); cur.close(); conn.close()
        flask_session.pop('quiz_{0}'.format(topic_id), None)
        return render_template('results.html', topic=topic, results=results,
            score=score, total=total_answered, pct=pct, rating=rating, next_review=nrd,
            REVIEW_LABELS=REVIEW_LABELS, color=color)

@app.route('/quiz/<int:topic_id>/submit', methods=['POST'])
def quiz_submit(topic_id):
    return redirect(url_for('quiz', topic_id=topic_id))

@app.route('/progress')
def progress():
    conn = get_db(); cur = conn.cursor()
    cur.execute("SELECT COUNT(*) as c FROM topics WHERE archived=0")
    total = cur.fetchone()['c']
    cur.execute("SELECT COUNT(DISTINCT topic_id) as c FROM sessions")
    started = cur.fetchone()['c']
    cur.execute("SELECT COUNT(*) as c FROM (SELECT topic_id FROM sessions WHERE review_stage=4 GROUP BY topic_id) x")
    mastered = cur.fetchone()['c']
    cur.execute("""SELECT t.subject, COUNT(DISTINCT t.id) as total_t,
        COUNT(DISTINCT s.topic_id) as started_t,
        COALESCE(SUM(s.score),0) as tot_score, COALESCE(SUM(s.total_questions),0) as tot_q
        FROM topics t LEFT JOIN sessions s ON s.topic_id=t.id
        WHERE t.archived=0 GROUP BY t.subject ORDER BY t.subject""")
    by_sub = cur.fetchall()
    cur.execute("SELECT s.*, t.title, t.subject FROM sessions s JOIN topics t ON t.id=s.topic_id ORDER BY s.id DESC LIMIT 12")
    recent = cur.fetchall()
    cur.execute("""SELECT t.title, t.subject, s.score, s.total_questions, s.session_date
        FROM sessions s JOIN topics t ON t.id=s.topic_id
        WHERE s.rating='struggled' AND s.id IN (SELECT MAX(id) FROM sessions GROUP BY topic_id)
        ORDER BY s.session_date DESC LIMIT 6""")
    weak = cur.fetchall()
    cur.close(); conn.close()
    return render_template('progress.html', total=total, started=started, mastered=mastered,
        by_sub=by_sub, recent=recent, weak=weak, COLORS=SUBJECT_COLORS, EMOJIS=SUBJECT_EMOJIS)

if __name__ == '__main__':
    ok, msg = test_connection()
    if not ok:
        print(f"\n{'='*60}\n  COULD NOT CONNECT TO DATABASE\n  {msg}\n{'='*60}\n")
        raise SystemExit(1)
    init_schema()
    from content import seed_all_content
    _c = get_db(); seed_all_content(_c); _c.close()
    mode = "PARENT VIEW" if PARENT_MODE else "FULL ACCESS"
    print(f"\n{'='*60}\n  Anish's 11+ App — {mode}\n  Open: http://127.0.0.1:5151\n{'='*60}\n")
    port = int(os.environ.get('PORT', 5151))
    host = '0.0.0.0' if os.environ.get('PORT') else '127.0.0.1'
    if not os.environ.get('PORT'):
        import threading, webbrowser
        def open_browser():
            import time; time.sleep(1.5)
            webbrowser.open('http://127.0.0.1:5151')
        threading.Thread(target=open_browser, daemon=True).start()
    app.run(host=host, port=port, debug=False)
