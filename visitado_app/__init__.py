from flask import Flask, redirect, url_for
from visitado_app.config import Config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    from visitado_app.routes import visitado
    app.register_blueprint(visitado)

    app.register_error_handler(404, page_not_found)
    return app


def page_not_found(e):
    return redirect(url_for("visitado.home"))
