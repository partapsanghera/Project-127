from bs4 import BeautifulSoup
import requests
import pandas as pd

START_URL = (
    "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
)
wiki = requests.get(START_URL)
soup = BeautifulSoup(wiki.text, "html.parser")
temp_list = []
for tr in soup.find("table").find_all("tr"):
    td = tr.find_all("td")
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

Name = []
Distance = []
Mass = []
Radius = []

for i in range(1, len(temp_list)):
    Name.append(temp_list[i][1])
    Distance.append(temp_list[i][3])
    Mass.append(temp_list[i][5])
    Radius.append(temp_list[i][6])

df = pd.DataFrame(
    list(zip(Name, Distance, Mass, Radius)),
    columns=["Name", "Distance", "Mass", "Radius"],
)
df.to_csv("data.csv")