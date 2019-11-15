from visitado_app import db
from flask_login import current_user
from visitado_app.utils import get_string_from_list, get_list_from_string
import csv


def add_country_to_user(country_code):
    countries = current_user.countries_visited

    if countries:
        if country_code in countries:
            return

    if not countries:
        current_user.countries_visited = country_code
    else:
        current_user.countries_visited = f"{countries},{country_code}"
    db.session.commit()


def get_countries_visited():
    countries_visited = current_user.countries_visited
    return countries_visited


def delete_country_from_user(country_code):
    if country_code in current_user.countries_visited:
        countries = get_list_from_string(current_user.countries_visited)
        print("1 " + current_user.countries_visited)
        countries.remove(country_code)
        countries = get_string_from_list(countries)
        print("2 " + current_user.countries_visited)
        current_user.countries_visited = countries
    if current_user.countries_visited == "":
        current_user.countries_visited = None
    db.session.commit()


def change_user_color(new_color):
    current_user.color = new_color
    db.session.commit()


def generate_settings_from_data(country_list):
    data = []
    pass_append = False
    with open("visitado_app/static/country_data.csv") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            if country_list:
                for country in country_list:
                    if country == row[1]:
                        data.append(1.0)
                        pass_append = True
                        break
                if not pass_append:
                    data.append(0.0)
                pass_append = False
            else:
                data.append(0.0)
    data.pop(0)
    return data
