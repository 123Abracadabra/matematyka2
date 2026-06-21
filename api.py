import time
from flask import Blueprint, jsonify, request, session

from data.chapters import CHAPTERS_BY_ID
from services.auth import login_required
from services.db import get_db
from services.progress import get_progress

api_bp       = Blueprint("api", __name__, url_prefix="/api")
COOLDOWN_SEC = 600


# ── practice answer ───────────────────────────────────────────────────────────

@api_bp.route("/task/answer", methods=["POST"])
@login_required
def task_answer():
    from data.topic_tasks import TOPIC_TASKS, get_topic_tasks
    data    = request.get_json() or {}
    task_id = data.get("task_id")
    answer  = str(data.get("answer", "")).strip()
    user_id = session["user_id"]

    task = next(
        (t for tasks in TOPIC_TASKS.values() for t in tasks if t["id"] == task_id),
        None
    )
    if not task:
        return jsonify({"error": "not found"}), 404

    is_correct = (answer.lower().replace(" ", "") ==
                  str(task["answer"]).strip().lower().replace(" ", ""))

    db = get_db()
    if is_correct:
        db.execute(
            "INSERT INTO task_progress(user_id, task_id, correct) VALUES(?,?,1) "
            "ON CONFLICT(user_id, task_id) DO UPDATE SET correct=1",
            (user_id, task_id)
        )
        db.commit()

    topic_name = next(
        (n for n, ts in TOPIC_TASKS.items() if any(t["id"] == task_id for t in ts)), None
    )
    done_count = pct = total = 0
    if topic_name:
        topic_tasks = get_topic_tasks(topic_name)
        total       = len(topic_tasks)
        task_ids    = [t["id"] for t in topic_tasks]
        done_ids    = {r["task_id"] for r in db.execute(
            "SELECT task_id FROM task_progress WHERE user_id=? AND correct=1", (user_id,)
        ).fetchall()}
        done_count  = sum(1 for tid in task_ids if tid in done_ids)
        pct         = round(done_count / total * 100) if total else 0

    return jsonify({
        "correct": is_correct, "explanation": task["explanation"],
        "done_count": done_count, "total": total, "pct": pct,
    })


# ── submit test ───────────────────────────────────────────────────────────────

@api_bp.route("/test/submit", methods=["POST"])
@login_required
def test_submit():
    data       = request.get_json() or {}
    answers    = data.get("answers", {})
    user_id    = session["user_id"]
    answer_map = session.get("test_answers", {})
    chapter_id = session.get("test_chapter")
    topic      = session.get("test_topic")
    level      = session.get("test_level", "base")

    if not answer_map or not chapter_id or not topic:
        return jsonify({"error": "no active test"}), 400

    # grade
    correct_count = 0
    results = []
    for task_id, correct_answer in answer_map.items():
        ok = (str(answers.get(task_id, "")).strip().lower().replace(" ", "") ==
              str(correct_answer).strip().lower().replace(" ", ""))
        if ok:
            correct_count += 1
        results.append({"task_id": task_id, "correct": ok})

    total  = len(answer_map)
    passed = correct_count >= 3
    crowns = 0
    if correct_count >= 5:   crowns = 3
    elif correct_count >= 4: crowns = 2
    elif correct_count >= 3: crowns = 1

    db = get_db()
    if passed:
        db.execute(
            "DELETE FROM test_cooldown "
            "WHERE user_id=? AND chapter_id=? AND topic=? AND level=?",
            (user_id, chapter_id, topic, level)
        )
        existing = db.execute(
            "SELECT crowns FROM progress "
            "WHERE user_id=? AND chapter_id=? AND topic=? AND level=?",
            (user_id, chapter_id, topic, level)
        ).fetchone()
        new_crowns = max(existing["crowns"], crowns) if existing else crowns
        if existing:
            db.execute(
                "UPDATE progress SET crowns=? "
                "WHERE user_id=? AND chapter_id=? AND topic=? AND level=?",
                (new_crowns, user_id, chapter_id, topic, level)
            )
        else:
            db.execute(
                "INSERT INTO progress(user_id, chapter_id, topic, level, crowns) "
                "VALUES(?,?,?,?,?)",
                (user_id, chapter_id, topic, level, new_crowns)
            )
    else:
        now = int(time.time())
        db.execute(
            "INSERT INTO test_cooldown(user_id, chapter_id, topic, level, failed_at) "
            "VALUES(?,?,?,?,?) "
            "ON CONFLICT(user_id, chapter_id, topic, level) DO UPDATE SET failed_at=?",
            (user_id, chapter_id, topic, level, now, now)
        )

    db.commit()

    # chapter overall %
    chapter   = CHAPTERS_BY_ID.get(chapter_id, {})
    progress  = get_progress(user_id)
    done_base = progress.get(chapter_id, {}).get("base", [])
    done_ext  = progress.get(chapter_id, {}).get("ext",  [])
    done_any  = list(set(done_base + done_ext))
    ch_pct    = round(len(done_any) / len(chapter.get("topics", [1])) * 100)

    session.pop("test_answers", None)
    session.pop("test_chapter", None)
    session.pop("test_topic",   None)
    session.pop("test_level",   None)

    return jsonify({
        "passed": passed, "correct_count": correct_count,
        "total": total, "crowns": crowns, "level": level,
        "results": results,
        "cooldown": COOLDOWN_SEC if not passed else 0,
        "ch_pct": ch_pct,
    })
