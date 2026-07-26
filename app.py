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

def _render_quiz(topic, questions, next_stage, COLORS, EMOJIS, parent_mode):
    color = COLORS.get(topic["subject"], "#6C63FF")
    total = len(questions)
    qhtml = ""
    for i, q in enumerate(questions, 1):
        if q["difficulty"] == 1:
            diff = "Easy"
        elif q["difficulty"] == 2:
            diff = "Medium"
        else:
            diff = "Hard"
        
        opts = ""
        if q["question_type"] == "mc":
            opts = '<input type="hidden" name="answer_{0}" id="ans{0}" value="">'.format(q["id"])
            for v, l in [(q["option_a"],"A"),(q["option_b"],"B"),(q["option_c"],"C"),(q["option_d"],"D")]:
                if v:
                    safe_v = str(v).replace('"', '&quot;')
                    opts += '<button type="button" class="opt" data-qid="{0}" data-n="{1}" data-val="{2}" onclick="pick(this)"><div class="ltr">{3}</div><span>{2}</span></button>'.format(q["id"], i, safe_v, l)
        else:
            opts = '<input type="text" class="type-in" name="answer_{0}" placeholder="Type answer..."><button type="button" onclick="advance({1})" style="background:#6C63FF;color:white;border:none;padding:16px;border-radius:50px;font-size:16px;font-weight:800;cursor:pointer;width:100%;margin-top:8px;font-family:inherit;">Next</button>'.format(q["id"], i)
        
        qhtml += '<div id="qc{0}" style="display:none"><div style="background:#1A1A35;border:1px solid #2A2A4A;border-radius:20px;padding:24px;margin-bottom:16px"><input type="hidden" name="question_ids" value="{1}"><div style="font-size:11px;font-weight:800;text-transform:uppercase;color:rgba(255,255,255,0.4);margin-bottom:14px">{2}</div><div style="font-size:18px;font-weight:800;line-height:1.6;margin-bottom:20px;color:white">{3}</div>{4}</div></div>'.format(i, q["id"], diff, q["question_text"], opts)

    parts = []
    parts.append('<!DOCTYPE html><html><head><meta charset="UTF-8">')
    parts.append('<meta name="viewport" content="width=device-width,initial-scale=1">')
    parts.append('<title>Quiz - ' + topic["title"] + '</title>')
    parts.append('<style>')
    parts.append('*{box-sizing:border-box;margin:0;padding:0}')
    parts.append('body{font-family:-apple-system,BlinkMacSystemFont,sans-serif;background:#0A0A1A;color:white;min-height:100vh}')
    parts.append('.nav{display:flex;justify-content:center;gap:6px;padding:12px;flex-wrap:wrap;background:rgba(10,10,26,0.95);position:sticky;top:0;z-index:100;border-bottom:1px solid #2A2A4A}')
    parts.append('.nav a{color:rgba(255,255,255,0.5);text-decoration:none;padding:6px 14px;border-radius:50px;font-size:13px;font-weight:700}')
    parts.append('.nav a:hover{color:white;background:rgba(255,255,255,0.1)}')
    parts.append('.main{max-width:800px;margin:0 auto;padding:20px 16px 80px}')
    parts.append('.opt{width:100%;padding:16px 18px;margin:8px 0;border-radius:14px;border:2px solid #2A2A4A;background:rgba(255,255,255,0.03);font-size:16px;font-weight:700;cursor:pointer;text-align:left;font-family:inherit;color:white;display:flex;align-items:center;gap:12px}')
    parts.append('.ltr{width:36px;height:36px;border-radius:50%;background:#2A2A4A;display:flex;align-items:center;justify-content:center;font-weight:900;font-size:14px;flex-shrink:0;color:white}')
    parts.append('.type-in{width:100%;padding:14px;border-radius:14px;border:2px solid #2A2A4A;font-size:16px;font-weight:700;font-family:inherit;background:rgba(255,255,255,0.05);color:white;margin-bottom:10px}')
    parts.append('.prog-wrap{background:rgba(255,255,255,0.1);border-radius:50px;height:10px;overflow:hidden;margin-top:8px}')
    parts.append('.prog-fill{height:100%;border-radius:50px;transition:width 0.4s;background:linear-gradient(90deg,' + color + ',' + color + '88)}')
    parts.append('</style></head><body>')
    parts.append('<div class="nav">')
    parts.append('<a href="/">Home</a>')
    parts.append('<a href="/subject/Maths">Maths</a>')
    parts.append('<a href="/subject/English">English</a>')
    parts.append('<a href="/subject/Verbal Reasoning">Verbal</a>')
    parts.append('<a href="/progress">Progress</a>')
    parts.append('</div>')
    parts.append('<div class="main">')
    parts.append('<div id="tb" style="background:#1A1A35;border:1px solid #2A2A4A;border-radius:20px;padding:20px;margin-bottom:16px">')
    parts.append('<div style="font-size:15px;font-weight:900;margin-bottom:8px">' + topic["title"] + '</div>')
    parts.append('<div style="color:rgba(255,255,255,0.5);font-size:13px;font-weight:700;margin-bottom:6px">Question <span id="qnum">1</span> of ' + str(total) + '</div>')
    parts.append('<div class="prog-wrap"><div class="prog-fill" id="prog" style="width:0%"></div></div>')
    parts.append('</div>')
    parts.append('<form method="post" action="/quiz/' + str(topic["id"]) + '/submit">')
    parts.append('<input type="hidden" name="next_stage" value="' + str(next_stage) + '">')
    parts.append(qhtml)
    parts.append('<div id="done" style="display:none;background:#1A1A35;border:1px solid #2A2A4A;border-radius:20px;padding:48px;text-align:center">')
    parts.append('<div style="font-size:72px;margin-bottom:16px">&#127881;</div>')
    parts.append('<h2 style="font-size:24px;font-weight:900;margin-bottom:8px;color:white">All done Anish!</h2>')
    parts.append('<p style="color:rgba(255,255,255,0.5);margin-bottom:24px">You answered all ' + str(total) + ' questions!</p>')
    parts.append('<button type="submit" style="background:linear-gradient(135deg,#00C896,#00E5AB);color:#0A2E24;border:none;padding:18px 40px;border-radius:50px;font-size:20px;font-weight:900;cursor:pointer;font-family:inherit;width:100%">See Results!</button>')
    parts.append('</div>')
    parts.append('</form>')
    parts.append('<div style="margin-top:16px"><a href="/learn/' + str(topic["id"]) + '" style="background:rgba(255,255,255,0.1);color:white;border:1px solid #2A2A4A;padding:10px 20px;border-radius:50px;font-weight:800;font-size:13px;display:inline-block">Back to Lesson</a></div>')
    parts.append('</div>')
    
    # JavaScript
    js = '''<script>
var T=''' + str(total) + ''',lk=false;
function showQ(n){
  for(var i=1;i<=T;i++){var e=document.getElementById('qc'+i);if(e)e.style.display='none';}
  document.getElementById('done').style.display='none';
  if(n>T){
    document.getElementById('done').style.display='block';
    document.getElementById('prog').style.width='100%';
    document.getElementById('qnum').textContent=T;
  } else {
    var e=document.getElementById('qc'+n);
    if(e) e.style.display='block';
    document.getElementById('qnum').textContent=n;
    document.getElementById('prog').style.width=Math.round(((n-1)/T)*100)+'%';
  }
  document.getElementById('tb').scrollIntoView({behavior:'smooth',block:'start'});
}
function pick(btn){
  if(lk) return;
  lk=true;
  var qid=btn.getAttribute('data-qid');
  var n=parseInt(btn.getAttribute('data-n'));
  var val=btn.getAttribute('data-val');
  document.getElementById('ans'+qid).value=val;
  var card=document.getElementById('qc'+n);
  if(card) card.querySelectorAll('.opt').forEach(function(b){b.onclick=null;b.style.pointerEvents='none';});
  btn.style.borderColor='#6C63FF';
  btn.style.background='rgba(108,99,255,0.2)';
  btn.querySelector('.ltr').style.background='#6C63FF';
  btn.querySelector('.ltr').style.color='white';
  setTimeout(function(){lk=false;showQ(n+1);},400);
}
function advance(n){
  if(lk) return;
  lk=true;
  setTimeout(function(){lk=false;showQ(n+1);},100);
}
showQ(1);
</script>'''
    
    parts.append(js)
    parts.append('</body></html>')
    
    from flask import Response
    return Response(''.join(parts), mimetype='text/html')


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
    questions = (easy[:2] + med[:2] + hard[:1]) or all_qs[:5]
    random.shuffle(questions)
    current_stage = latest['review_stage'] if latest else None
    next_stage = 0 if current_stage is None else (min(current_stage+1, 4))
    return _render_quiz( topic=topic, questions=questions,
        next_stage=next_stage, REVIEW_LABELS=REVIEW_LABELS,
        color=SUBJECT_COLORS.get(topic['subject'],'#4F46E5'))

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
    app.run(host='127.0.0.1', port=5151, debug=False)
