from services.db import get_db
from data.chapters import CHAPTERS
from data.topic_tasks import get_topic_tasks


def get_progress(user_id):
    db   = get_db()
    rows = db.execute(
        "SELECT chapter_id, topic, level, crowns FROM progress WHERE user_id=?",
        (user_id,)
    ).fetchall()

    # result[chapter_id][level] = list of done topics
    result = {}
    for row in rows:
        result.setdefault(row["chapter_id"], {})
        result[row["chapter_id"]].setdefault(row["level"], [])
        result[row["chapter_id"]][row["level"]].append(row["topic"])

    return result


def enrich_chapters(progress):
    chapters = []
    for ch in CHAPTERS:
        # combine base+ext for overall % (topic done if either level done)
        done_base = progress.get(ch["id"], {}).get("base", [])
        done_ext  = progress.get(ch["id"], {}).get("ext",  [])
        done_any  = list(set(done_base + done_ext))

        pct = round(len(done_any) / len(ch["topics"]) * 100) if ch["topics"] else 0

        next_topic = next(
            (t for t in ch["topics"] if t not in done_any), None
        )

        chapters.append({
            **ch,
            "done":        done_any,
            "done_base":   done_base,
            "done_ext":    done_ext,
            "pct":         pct,
            "next_topic":  next_topic,
            "topic_items": build_topic_items(ch, done_base, done_ext),
        })

    return chapters


def build_topic_items(chapter, done_base, done_ext):
    items = []
    for topic in chapter["topics"]:
        tasks      = get_topic_tasks(topic)
        base_count = sum(1 for t in tasks if t.get("level") == "podstawa")
        ext_count  = sum(1 for t in tasks if t.get("level") == "rozszerzenie")

        done_b = topic in done_base
        done_e = topic in done_ext

        # understanding: avg of both levels (0/50/100 each)
        understanding = ((100 if done_b else 0) + (100 if done_e else 0)) // 2

        items.append({
            "name":          topic,
            "done":          done_b or done_e,
            "done_base":     done_b,
            "done_ext":      done_e,
            "understanding": understanding,
            "base_count":    base_count,
            "ext_count":     ext_count,
            "crowns_base":   0,   # filled in by route if user logged in
            "crowns_ext":    0,
        })
    return items


def build_learning_plan(chapters):
    next_chapter = next(
        (ch for ch in chapters if ch["pct"] < 100), None
    )
    next_steps = [ch for ch in chapters if ch["next_topic"]][:3]

    return {
        "next_chapter": next_chapter,
        "next_steps":   next_steps,
        "review_plan":  [],
    }
