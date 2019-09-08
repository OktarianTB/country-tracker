from flask import Blueprint, render_template, redirect, url_for, flash
from visitado_app.forms import AddCountry, LoginForm, RegisterForm
from visitado_app.utils import get_all_countries, get_list_from_string
from visitado_app import db, bcrypt
from visitado_app.model import User
from flask_login import login_user, current_user, logout_user, login_required
from visitado_app.manager import add_country_to_user, get_countries_visited, \
    generate_settings_from_data, delete_country_from_user

visitado = Blueprint("visitado", __name__)


@visitado.route("/", methods=["GET", "POST"])
def home():
    if not current_user.is_authenticated:
        flash(f"Please login to access Visitado's features!", 'info')
        return render_template("home.html", title="Home - Visitado")
    else:
        visited_countries = get_countries_visited()
        country_list = get_list_from_string(visited_countries)
        map_settings = generate_settings_from_data(country_list)

        form = AddCountry()
        form.new_country.choices = get_all_countries()

        if form.validate_on_submit():
            add_country_to_user(form.new_country.data)
            return redirect(url_for("visitado.home"))
        return render_template("home.html", title="Home - Visitado", form=form,
                               map_settings=map_settings, country_list=country_list)


@login_required
@visitado.route("/delete/<country_code>", methods=["GET", "POST"])
def delete_country(country_code):
    delete_country_from_user(country_code)
    return redirect(url_for("visitado.home"))


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
        user = User(username=form.username.data, email=form.email.data, password=hashed_password, countries_visited=None)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been successfully created!', 'success')
        return redirect(url_for("visitado.login"))
    return render_template("register.html", title="Register - Visitado", form=form)


@visitado.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("visitado.home"))
