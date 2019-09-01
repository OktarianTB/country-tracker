from flask import Blueprint, render_template, redirect, url_for
from visitado_app.forms import AddCountry, LoginForm, RegisterForm
from visitado_app.utils import get_all_countries

visitado = Blueprint("visitado", __name__)


@visitado.route("/", methods=["GET", "POST"])
def home():
    form = AddCountry()
    form.new_country.choices = get_all_countries()
    return render_template("home.html", title="Home - Visitado", form=form)


@visitado.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    return render_template("login.html", title="Login - Visitado", form=form)


@visitado.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    return render_template("register.html", title="Register - Visitado", form=form)

