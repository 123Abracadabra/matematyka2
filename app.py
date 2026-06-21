import unicodedata, re

from flask import Flask

from routes.api import api_bp
from routes.auth import auth_bp
from routes.chapters import chapters_bp
from routes.main import main_bp
from services.db import close_db, init_db


def slugify(text):
    text = unicodedata.normalize("NFD", text)
    text = text.encode("ascii", "ignore").decode()
    text = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return text


def create_app():
    app = Flask(__name__)
    app.secret_key = "matematyczna-wolnosc-super-secret-key-2024"

    app.jinja_env.filters["slugify"] = slugify

    app.teardown_appcontext(close_db)

    app.register_blueprint(main_bp)
    app.register_blueprint(chapters_bp)
    app.register_blueprint(api_bp)
    app.register_blueprint(auth_bp)

    return app


app = create_app()


if __name__ == "__main__":
    with app.app_context():
        init_db()
    app.run(host="0.0.0.0", port=5000, debug=True)
