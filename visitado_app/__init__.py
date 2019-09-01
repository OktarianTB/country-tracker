from flask import Flask, redirect, url_for
from visitado_app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    app.secret_key = Config.SECRET_KEY

    bcrypt.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    from visitado_app.routes import visitado
    app.register_blueprint(visitado)

    app.register_error_handler(404, page_not_found)
    return app


def page_not_found(e):
    return redirect(url_for("visitado.home"))


