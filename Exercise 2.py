import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

# Load the webpage content
r = requests.get("https://keithgalli.github.io/web-scraping/webpage.html")

# Convert to a beautiful soup object
webpage = bs(r.content, "html.parser")

# Get the table of hockey stats
table = webpage.select("table.hockey-stats")[0]
columns = table.find("thead").find_all("th")
column_names = [c.string for c in columns]

l = []
table_rows = table.find("tbody").find_all("tr")
for tr in table_rows:
	td = tr.find_all("td")
	row = [str(tr.get_text()).strip() for tr in td]
	l.append(row)

df = pd.DataFrame(l, columns=column_names)
print(df.head())
