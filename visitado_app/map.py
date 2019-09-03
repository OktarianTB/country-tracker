import csv


def get_map_settings(csv_file):
    data = []
    with open(csv_file) as file:
        reader = csv.reader(file)
        for row in reader:
            try:
                data.append(float(row[3]))
            except ValueError:
                pass
    return data
