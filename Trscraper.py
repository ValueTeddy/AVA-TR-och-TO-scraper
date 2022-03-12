import requests
from bs4 import BeautifulSoup

URL = "https://www.avanza.se/aktier/ratter-teckningsoptioner.html"

soup = BeautifulSoup(requests.get(URL).text, "html.parser")
div = soup.find("div", class_="section ssicomponent")
tr = div.find_all("table")

print(tr)

    