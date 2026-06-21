# -*- coding: utf-8 -*-
from flask import Blueprint, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from services.db import get_db

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/rejestracja", methods=["GET", "POST"])
def rejestracja():
    if session.get("user_id"):
        return redirect(url_for("main.index"))

    error = None

    if request.method == "POST":
        name      = request.form.get("name", "").strip()
        email     = request.form.get("email", "").strip().lower()
        password  = request.form.get("password", "")
        password2 = request.form.get("password2", "")

        if not name:
            error = "Wpisz swoje imię."
        elif "@" not in email:
            error = "Podaj poprawny adres email."
        elif len(password) < 4:
            error = "Hasło musi mieć co najmniej 4 znaki."
        elif password != password2:
            error = "Hasła się nie zgadzają."
        else:
            db = get_db()
            existing = db.execute(
                "SELECT id FROM users WHERE email=?", (email,)
            ).fetchone()

            if existing:
                error = "Ten email jest już zarejestrowany."
            else:
                cursor = db.execute(
                    "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
                    (name, email, generate_password_hash(password))
                )
                db.commit()
                session["user_id"] = cursor.lastrowid
                return redirect(url_for("main.index"))

    return render_template("auth.html", mode="register", error=error)


@auth_bp.route("/logowanie", methods=["GET", "POST"])
def login():
    if session.get("user_id"):
        return redirect(url_for("main.index"))

    error = None

    if request.method == "POST":
        email    = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        db       = get_db()
        user     = db.execute(
            "SELECT * FROM users WHERE email=?", (email,)
        ).fetchone()

        if not user or not check_password_hash(user["password"], password):
            error = "Błędny email lub hasło."
        else:
            session["user_id"] = user["id"]
            return redirect(url_for("main.index"))

    return render_template("auth.html", mode="login", error=error)


@auth_bp.route("/wylogowanie")
def logout():
    session.clear()
    return redirect(url_for("main.index"))
