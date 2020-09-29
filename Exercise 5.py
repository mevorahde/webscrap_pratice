import requests
from bs4 import BeautifulSoup as bs


# Load the webpage content
url = "https://keithgalli.github.io/web-scraping/"
r = requests.get(url + "webpage.html")

# Convert to a beautiful soup object
webpage = bs(r.content, "html.parser")

# Solve the mystery challenge
files = webpage.select("div.block a")
relative_files = [f["href"] for f in files]
for f in relative_files:
	full_url = url + f
	page = requests.get(full_url)
	bs_page = bs(page.content, "html.parser")
	select_word_element = bs_page.find("p", attrs={"id":"secret-word"})
	select_word = select_word_element.string
	print(select_word)

# print(relative_files)