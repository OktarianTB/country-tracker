import requests
from bs4 import BeautifulSoup

url = "https://www.factmonster.com/world/countries/"


def get_country_info(country):
    country_url = ""
    sections = country.split(" ")
    for section in sections:
        country_url += f"{section}-"

    response = requests.get(f"{url}{country_url[:-1]}")

    if response.status_code == 200:
        data = response.text
        soup = BeautifulSoup(data, "html.parser")

        flag_div = soup.find("div", class_="field_flag")
        flag = flag_div.find("img")["data-src"]

        description_div = soup.find("div", class_="robot-content").findChildren()
        if len(description_div) >= 3:
            description = description_div[3].text
        else:
            description = None

        return flag, description
    else:
        print(response.status_code)
        return None


