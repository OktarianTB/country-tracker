from flask import Flask, redirect, url_for
from visitado_app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from visitado_app.utils import get_country_from_code


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()

from visitado_app.manager import delete_country_from_user, change_user_color


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    app.secret_key = Config.SECRET_KEY

    bcrypt.init_app(app)
    db.init_app(app)
    # with app.app_context():
    #     from visitado_app.model import User
    #     db.create_all()
    #     from visitado_app import routes, model
    login_manager.init_app(app)

    from visitado_app.routes import visitado
    app.register_blueprint(visitado)

    app.register_error_handler(404, page_not_found)
    app.jinja_env.globals.update(get_country_from_code=get_country_from_code,
                                 delete_country_from_user=delete_country_from_user)
    return app


def page_not_found(e):
    return redirect(url_for("visitado.home"))


