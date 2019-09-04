from flask import Blueprint, render_template, redirect, url_for, flash
from visitado_app.forms import AddCountry, LoginForm, RegisterForm
from visitado_app.utils import get_all_countries
from visitado_app import db, bcrypt
from visitado_app.model import User
from flask_login import login_user, current_user, logout_user
from visitado_app.map import get_map_settings

visitado = Blueprint("visitado", __name__)


@visitado.route("/", methods=["GET", "POST"])
def home():
    if not current_user.is_authenticated:
        flash(f"Please login to access Visitado's features!", 'info')
    form = AddCountry()
    form.new_country.choices = get_all_countries()
    if form.validate_on_submit():
        flash(form.new_country.data, "success")
    map_settings = get_map_settings("visitado_app/static/map_data.csv")
    return render_template("home.html", title="Home - Visitado", form=form, map_settings=map_settings)


@visitado.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for("visitado.home"))
        else:
            flash("Login Unsuccessful. Please try again!", "danger")
    return render_template("login.html", title="Login - Visitado", form=form)


@visitado.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("visitado.home"))
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()

        flash(f'Your account has been successfully created!', 'success')
        return redirect(url_for("visitado.login"))
    return render_template("register.html", title="Register - Visitado", form=form)


@visitado.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("visitado.home"))
