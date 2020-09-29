import requests
from bs4 import BeautifulSoup as bs


# Load the webpage content
url = "https://keithgalli.github.io/web-scraping/"
r = requests.get(url + "webpage.html")

# Convert to a beautiful soup object
webpage = bs(r.content, "html.parser")

images = webpage.select("div.row div.column img")
image_url = images[0]["src"]
full_url = url + image_url

image_data = requests.get(full_url).content
with open('lake_como.jpg', 'wb') as handler:
	handler.write(image_data)