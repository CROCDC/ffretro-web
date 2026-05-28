import os
from datetime import datetime
from typing import Any

from dotenv import load_dotenv
from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix

load_dotenv()

CONTACT: dict[str, str] = {
    "phone_display": "097 735 511",
    "phone_e164": "+59897735511",
    "whatsapp_url": "https://wa.me/59897735511?text=Hola%20FF%20Retro%2C%20quiero%20una%20cotizaci%C3%B3n.",
    "instagram_handle": "@ffretrocolonia",
    "instagram_url": "https://www.instagram.com/ffretrocolonia/",
    "location": "Colonia del Sacramento, Uruguay",
    "tagline": "Máquina potente, trabajo prolijo y responsable.",
}


def create_app() -> Flask:
    app = Flask(__name__)

    app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)

    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-secret-key")
    app.config["DEBUG"] = os.environ.get("FLASK_DEBUG", "false").lower() == "true"

    @app.context_processor
    def inject_globals() -> dict[str, Any]:
        return {
            "current_year": datetime.utcnow().year,
            "contact": CONTACT,
        }

    with app.app_context():
        from app.routes import register_routes

        register_routes(app)

    return app
