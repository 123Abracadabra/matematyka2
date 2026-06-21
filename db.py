import sqlite3
from flask import g

DB = "matma.db"

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DB)
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    db = g.pop("db", None)
    if db:
        db.close()

def init_db():
    db = get_db()
    db.executescript("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS progress (
            user_id    INTEGER NOT NULL,
            chapter_id TEXT NOT NULL,
            topic      TEXT NOT NULL,
            level      TEXT NOT NULL DEFAULT 'base',
            crowns     INTEGER NOT NULL DEFAULT 0,
            PRIMARY KEY(user_id, chapter_id, topic, level)
        );

        CREATE TABLE IF NOT EXISTS task_progress (
            user_id  INTEGER NOT NULL,
            task_id  TEXT NOT NULL,
            correct  INTEGER NOT NULL DEFAULT 0,
            PRIMARY KEY(user_id, task_id)
        );

        CREATE TABLE IF NOT EXISTS test_cooldown (
            user_id    INTEGER NOT NULL,
            chapter_id TEXT NOT NULL,
            topic      TEXT NOT NULL,
            level      TEXT NOT NULL DEFAULT 'base',
            failed_at  INTEGER NOT NULL,
            PRIMARY KEY(user_id, chapter_id, topic, level)
        );
    """)
    db.commit()
