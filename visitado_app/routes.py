from flask import Blueprint, render_template, redirect, url_for
from visitado_app.forms import AddCountry
from visitado_app.utils import get_all_countries

visitado = Blueprint("visitado", __name__)


@visitado.route("/", methods=["GET", "POST"])
def home():
    form = AddCountry()
    form.new_country.choices = get_all_countries()
    return render_template("home.html", title="Visitado", form=form)

