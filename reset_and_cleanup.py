"""
reset_and_cleanup.py — Full reset for Anish's 11+ app.

Two things happen:

1. Finds any duplicate topics (same subject + title — these can build up if
   a loader script like add_previous_exam_*.py was ever run against a
   slightly different topic title, or content.py reseeded something twice).
   Duplicate topics are merged: their questions are moved onto the oldest
   (kept) copy of the topic, any exact duplicate questions are dropped, and
   the leftover empty duplicate topic rows are removed.

2. Wipes ALL quiz session history across every subject — scores, streaks,
   ratings, and spaced-repetition review dates. This gives Anish a
   completely clean slate now that the answer-key bugs found while
   building the "Previous Exam Questions" section have been fixed, so old
   sessions (which may have been marked right/wrong against a bad answer
   key) don't linger.

SAFETY: by default this script only PREVIEWS what it would do (dry run).
Nothing is changed unless you pass --apply.

Usage:
    python3 reset_and_cleanup.py            # preview only, changes nothing
    python3 reset_and_cleanup.py --apply     # actually applies the changes
"""
import sys
from collections import defaultdict


def get_db():
    import psycopg2, psycopg2.extras, os
    sys.path.insert(0, os.path.expanduser("~/Downloads/anish_app_v2"))
    try:
        import config
        url = config.DATABASE_URL
    except Exception:
        url = os.environ.get("DATABASE_URL")
    return psycopg2.connect(url, cursor_factory=psycopg2.extras.RealDictCursor)


def main():
    apply = "--apply" in sys.argv
    conn = get_db()
    cur = conn.cursor()

    print("=" * 60)
    print("STEP 1: Checking for duplicate topics (same subject + title)")
    print("=" * 60)

    cur.execute("SELECT id, subject, title FROM topics ORDER BY subject, title, id")
    topics = cur.fetchall()
    groups = defaultdict(list)
    for t in topics:
        groups[(t['subject'], t['title'])].append(t['id'])

    dup_groups = {k: v for k, v in groups.items() if len(v) > 1}
    total_dupe_topics_removed = 0
    total_questions_merged = 0
    total_dupe_questions_removed = 0

    if not dup_groups:
        print("No duplicate topics found — content is already clean.")

    for (subject, title), ids in dup_groups.items():
        keep_id = min(ids)
        remove_ids = [i for i in ids if i != keep_id]
        print("\n'{}' ({}): {} copies (ids {}) -> keeping id {}, merging/removing {}".format(
            title, subject, len(ids), ids, keep_id, remove_ids))

        cur.execute("SELECT question_text FROM questions WHERE topic_id=%s", (keep_id,))
        existing_texts = {r['question_text'] for r in cur.fetchall()}

        for rid in remove_ids:
            cur.execute("SELECT id, question_text FROM questions WHERE topic_id=%s", (rid,))
            dup_questions = cur.fetchall()
            for q in dup_questions:
                short = q['question_text'][:60]
                if q['question_text'] in existing_texts:
                    print("    - dropping duplicate question: {}...".format(short))
                    total_dupe_questions_removed += 1
                    if apply:
                        cur.execute("DELETE FROM questions WHERE id=%s", (q['id'],))
                else:
                    print("    - moving question onto kept topic: {}...".format(short))
                    existing_texts.add(q['question_text'])
                    total_questions_merged += 1
                    if apply:
                        cur.execute("UPDATE questions SET topic_id=%s WHERE id=%s", (keep_id, q['id']))
            if apply:
                cur.execute("DELETE FROM topics WHERE id=%s", (rid,))
            total_dupe_topics_removed += 1

    if apply:
        conn.commit()

    print("\nDuplicate topics removed: {}".format(total_dupe_topics_removed))
    print("Questions merged onto kept topics: {}".format(total_questions_merged))
    print("Duplicate questions dropped: {}".format(total_dupe_questions_removed))

    print("\n" + "=" * 60)
    print("STEP 2: Clearing ALL quiz progress / session history")
    print("=" * 60)
    cur.execute("SELECT COUNT(*) as c FROM sessions")
    session_count = cur.fetchone()['c']
    print("Sessions currently stored: {}".format(session_count))
    if apply:
        cur.execute("DELETE FROM sessions")
        conn.commit()
        print("All sessions deleted. Scores, streaks and spaced-repetition history are now reset for every subject.")
    else:
        print("(dry run — would delete {} session rows)".format(session_count))

    cur.close()
    conn.close()

    if not apply:
        print("\nThis was a DRY RUN — nothing was changed.")
        print("Re-run with --apply to actually make these changes:")
        print("    python3 reset_and_cleanup.py --apply")
    else:
        print("\nDone! Anish's app now has a clean slate with no duplicate topics and no quiz history.")


if __name__ == "__main__":
    main()
