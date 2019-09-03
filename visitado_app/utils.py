from csv import reader
import plotly.graph_objects as go
import plotly.io as pio
import pandas as pd


def get_all_countries():
    with open("visitado_app/static/countries.csv") as csv_file:
        countries = [(row[1], row[0]) for row in reader(csv_file)]
    return countries


# Only used once to generate map data in map.html
def generate_map(csv_file):
    df = pd.read_csv(csv_file)
    fig = go.Figure(data=go.Choropleth(
        locations=df['country'],  # Spatial coordinates
        z=df['visited'].astype(float),  # Data to be color-coded
        locationmode='country names',  # set of locations match entries in `locations`
        colorscale=[[0, "rgb(223, 230, 233)"], [1, "rgb(108, 92, 231)"]],
        hoverinfo="location",
        showscale=False
    ))

    fig.update_layout(
        geo_scope='world',
        autosize=False,
        width=1000,
        height=1000
    )

    pio.write_html(fig, "templates/map.html")
