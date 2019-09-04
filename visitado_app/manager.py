from visitado_app import db
from flask_login import current_user
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
    # current_user.countries_visited = None
    db.session.commit()


def get_countries_visited():
    countries_visited = current_user.countries_visited
    return countries_visited


# The map takes a list where 0.0 represents non-visited countries and 1.0 represent visited countries
def generate_settings_from_data(country_list):
    data = []
    pass_append = False
    with open("visitado_app/static/map_data.csv") as csv_file:
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
