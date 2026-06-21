from flask import Blueprint
from flask import render_template

from services.auth import current_user

from services.progress import (
    build_learning_plan,
    get_progress,
    enrich_chapters
)

from data.chapters import CHAPTERS

main_bp = Blueprint(
    "main",
    __name__
)

@main_bp.route("/")
def index():

    user = current_user()

    progress = (
        get_progress(user["id"])
        if user else {}
    )

    chapters = enrich_chapters(
        progress
    )

    total_topics = sum(
        len(ch["topics"])
        for ch in CHAPTERS
    )

    total_done = sum(
        len(v)
        for v in progress.values()
    )

    total_pct = round(
        total_done
        /
        total_topics
        *
        100
    ) if total_topics else 0

    return render_template(
        "index.html",
        user=user,
        chapters=chapters,
        total_pct=total_pct,
        total_done=total_done,
        total_topics=total_topics
    )


@main_bp.route("/mapa")
def mapa():

    user = current_user()

    progress = (
        get_progress(user["id"])
        if user else {}
    )

    chapters = enrich_chapters(
        progress
    )

    total_topics = sum(
        len(ch["topics"])
        for ch in CHAPTERS
    )

    total_done = sum(
        len(v)
        for v in progress.values()
    )

    total_pct = round(
        total_done
        /
        total_topics
        *
        100
    ) if total_topics else 0

    return render_template(
        "mapa.html",
        user=user,
        chapters=chapters,
        plan=build_learning_plan(chapters),
        total_pct=total_pct,
        total_done=total_done,
        total_topics=total_topics
    )
