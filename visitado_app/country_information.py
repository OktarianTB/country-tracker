import requests
from bs4 import BeautifulSoup

url = "https://www.factmonster.com/world/countries/"


def get_country_info(country):
    response = requests.get(f"{url}{country}")
    if response.status_code == 200:
        data = response.text
        soup = BeautifulSoup(data, "html.parser")

        flag_div = soup.find("div", class_="field_flag")
        flag = flag_div.find("img")["data-src"]
        description = soup.find("div", class_="robot-content").findChildren()[3].text

        return flag, description
    else:
        print(response.status_code)
        return None


