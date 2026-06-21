# -*- coding: utf-8 -*-
from functools import wraps
from flask import session, redirect, url_for
from services.db import get_db


def current_user():
    uid = session.get("user_id")
    if not uid:
        return None
    return get_db().execute(
        "SELECT * FROM users WHERE id=?", (uid,)
    ).fetchone()


def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get("user_id"):
            return redirect(url_for("auth.login"))
        return f(*args, **kwargs)
    return decorated
