import requests
from bs4 import BeautifulSoup as bs


# Load the webpage content
r = requests.get("https://keithgalli.github.io/web-scraping/webpage.html")

# Convert to a beautiful soup object
webpage = bs(r.content, "html.parser")

# # Print out all of our html on the page
# print(webpage.prettify())

# Grab all of the social links from the webpage

# METHOD 1

# links = webpage.select("ul.socials a")
# actual_links = [link["href"] for link in links]
# print(actual_links)


# METHOD 2

# ulist = webpage.find("ul", attrs={"class":"socials"})
# links = ulist.find_all("a")
# actual_links = [link["href"] for link in links]
# print(actual_links)

# METHOD 3
# links = webpage.select("li.social a")
# actual_links = [link["href"] for link in links]
# print(actual_links)