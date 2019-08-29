from csv import reader


def get_all_countries():
    with open("visitado_app/static/countries.csv") as csv_file:
        countries = [(row[1], row[0]) for row in reader(csv_file)]
    return countries
