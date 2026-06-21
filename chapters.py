import unicodedata, re, random, time

from flask import Blueprint, redirect, render_template, url_for, request, session

from data.chapters import CHAPTERS_BY_ID
from services.auth import current_user, login_required
from services.db import get_db
from services.progress import build_topic_items, enrich_chapters, get_progress

chapters_bp  = Blueprint("chapters", __name__)
COOLDOWN_SEC = 600   # 10 min


def slugify(text):
    text = unicodedata.normalize("NFD", text)
    text = text.encode("ascii", "ignore").decode()
    text = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return text


# ── helpers ──────────────────────────────────────────────────────────────────

def _crowns(user_id, chapter_id, topic, level):
    row = get_db().execute(
        "SELECT crowns FROM progress WHERE user_id=? AND chapter_id=? AND topic=? AND level=?",
        (user_id, chapter_id, topic, level)
    ).fetchone()
    return row["crowns"] if row else 0


def _cooldown_left(user_id, chapter_id, topic, level):
    row = get_db().execute(
        "SELECT failed_at FROM test_cooldown "
        "WHERE user_id=? AND chapter_id=? AND topic=? AND level=?",
        (user_id, chapter_id, topic, level)
    ).fetchone()
    if not row:
        return 0
    return max(0, COOLDOWN_SEC - (int(time.time()) - row["failed_at"]))


# ── pages ─────────────────────────────────────────────────────────────────────

@chapters_bp.route("/rozdzialy")
def rozdzialy():
    user     = current_user()
    progress = get_progress(user["id"]) if user else {}
    chapters = enrich_chapters(progress)
    return render_template("rozdzialy.html", user=user, chapters=chapters)


@chapters_bp.route("/dzial/<chapter_id>")
def dzial(chapter_id):
    chapter = CHAPTERS_BY_ID.get(chapter_id)
    if not chapter:
        return redirect(url_for("main.index"))

    user     = current_user()
    progress = get_progress(user["id"]) if user else {}
    done_base = progress.get(chapter_id, {}).get("base", [])
    done_ext  = progress.get(chapter_id, {}).get("ext",  [])
    done_any  = list(set(done_base + done_ext))
    pct       = round(len(done_any) / len(chapter["topics"]) * 100) if chapter["topics"] else 0

    topic_items = build_topic_items(chapter, done_base, done_ext)

    # enrich crowns per level
    if user:
        db = get_db()
        for item in topic_items:
            for lv in ("base", "ext"):
                row = db.execute(
                    "SELECT crowns FROM progress "
                    "WHERE user_id=? AND chapter_id=? AND topic=? AND level=?",
                    (user["id"], chapter_id, item["name"], lv)
                ).fetchone()
                item[f"crowns_{lv}"] = row["crowns"] if row else 0

    return render_template("dzial.html", user=user, ch={
        **chapter,
        "done": done_any, "done_base": done_base, "done_ext": done_ext,
        "pct": pct, "topic_items": topic_items,
    })


@chapters_bp.route("/dzial/<chapter_id>/<path:topic_slug>")
def temat(chapter_id, topic_slug):
    from data.topic_tasks   import get_topic_tasks
    from data.topic_content import get_topic_content

    chapter = CHAPTERS_BY_ID.get(chapter_id)
    if not chapter:
        return redirect(url_for("main.index"))

    topic_name = next(
        (t for t in chapter["topics"] if slugify(t) == topic_slug), None
    )
    if not topic_name:
        return redirect(url_for("chapters.dzial", chapter_id=chapter_id))

    user     = current_user()
    progress = get_progress(user["id"]) if user else {}

    done_base_list = progress.get(chapter_id, {}).get("base", [])
    done_ext_list  = progress.get(chapter_id, {}).get("ext",  [])

    tasks   = get_topic_tasks(topic_name)
    content = get_topic_content(topic_name)

    done_task_ids = set()
    crowns_base = crowns_ext = cooldown_base = cooldown_ext = 0

    if user:
        db   = get_db()
        rows = db.execute(
            "SELECT task_id FROM task_progress WHERE user_id=? AND correct=1",
            (user["id"],)
        ).fetchall()
        done_task_ids = {r["task_id"] for r in rows}
        crowns_base   = _crowns(user["id"], chapter_id, topic_name, "base")
        crowns_ext    = _crowns(user["id"], chapter_id, topic_name, "ext")
        cooldown_base = _cooldown_left(user["id"], chapter_id, topic_name, "base")
        cooldown_ext  = _cooldown_left(user["id"], chapter_id, topic_name, "ext")

    task_ids   = [t["id"] for t in tasks]
    done_count = sum(1 for tid in task_ids if tid in done_task_ids)
    pct        = round(done_count / len(tasks) * 100) if tasks else 0

    return render_template("temat.html",
        user=user, ch=chapter,
        topic=topic_name, topic_slug=topic_slug,
        tasks=tasks,
        done_task_ids=list(done_task_ids),
        done_count=done_count, total=len(tasks), pct=pct,
        topic_done_base=(topic_name in done_base_list),
        topic_done_ext=(topic_name in done_ext_list),
        crowns_base=crowns_base, crowns_ext=crowns_ext,
        cooldown_base=cooldown_base, cooldown_ext=cooldown_ext,
        theory_base=content["theory_base"],
        theory_ext=content["theory_ext"],
        video_base=content.get("video_base", ""),
        video_ext=content.get("video_ext", ""),
    )


@chapters_bp.route("/dzial/<chapter_id>/<path:topic_slug>/test")
def test(chapter_id, topic_slug):
    from data.topic_tasks import get_topic_tasks

    chapter = CHAPTERS_BY_ID.get(chapter_id)
    if not chapter:
        return redirect(url_for("main.index"))

    topic_name = next(
        (t for t in chapter["topics"] if slugify(t) == topic_slug), None
    )
    if not topic_name:
        return redirect(url_for("chapters.dzial", chapter_id=chapter_id))

    # level comes from query param: /test?level=base or /test?level=ext
    level = request.args.get("level", "base")
    if level not in ("base", "ext"):
        level = "base"

    user         = current_user()
    cooldown     = 0
    crowns_base  = crowns_ext = 0
    if user:
        cooldown    = _cooldown_left(user["id"], chapter_id, topic_name, level)
        crowns_base = _crowns(user["id"], chapter_id, topic_name, "base")
        crowns_ext  = _crowns(user["id"], chapter_id, topic_name, "ext")

    all_tasks = get_topic_tasks(topic_name)

    # filter by level
    level_filter = "podstawa" if level == "base" else "rozszerzenie"
    level_tasks  = [t for t in all_tasks if t.get("level") == level_filter]
    if not level_tasks:
        level_tasks = all_tasks   # fallback: no filter

    count      = min(5, len(level_tasks))
    test_tasks = random.sample(level_tasks, count) if len(level_tasks) >= count else level_tasks

    # strip answers before sending to template
    safe_tasks = [{k: v for k, v in t.items() if k != "answer"} for t in test_tasks]

    session["test_answers"] = {t["id"]: t["answer"] for t in test_tasks}
    session["test_chapter"] = chapter_id
    session["test_topic"]   = topic_name
    session["test_level"]   = level

    return render_template("test.html",
        user=user, ch=chapter,
        topic=topic_name, topic_slug=topic_slug,
        tasks=safe_tasks, total=count,
        level=level,
        cooldown=cooldown,
        crowns_base=crowns_base, crowns_ext=crowns_ext,
        timer_per_task=180,
    )
