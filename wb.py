import requests
from bs4 import BeautifulSoup as bs
import re

# Load the webpage content
r = requests.get("https://keithgalli.github.io/web-scraping/example.html")

# Convert to a beautiful soup object
soup = bs(r.content, "html.parser")

# Print out all of our html on the page
# print(soup.prettify())


# Find all 'h2' tags
# first_header = soup.find_all("h2")
# print(first_header)

# Pass in a list of elements to look for 'h1' and 'h2' tags
# first_header = soup.find_all(["h1", "h2"])
# print(first_header)

# You can pass in attributes to the find/find_all function
# paragraph = soup.find_all("p", attrs={"id": "paragraph-id"})
# print(paragraph)

# You can nest find/fina_all calls
# body = soup.find("body")
# div = body.find("div")
# header = div.find("h1")
# print(header)

# We can search specific strings in our find/find_all call
# some_search = soup.find_all("p", string=re.compile("Some"))
# print(some_search)
#
# header_search = soup.find_all("h2", string=re.compile("(H|h)eader"))
# print(header_search)


# Select CSS Selector
# content = soup.select("div p")
# print(content)

# paragraphs = soup.select("h2 ~ p")
# print(paragraphs)

# bold_text = soup.select("p#paragraph-id b")
# print(bold_text)

# p = soup.select("body > p")
# for par in p:
# 	print(par.select("i"))

# Remove the html tags by converting value to a string
# h = soup.find("h2")
# print(h.string)

# Can't convert html tags to a string
# EXAMPLE OF SOMETHING THAT WON'T WORK
# div_string = soup.find("div")
# print(div_string.prettify())
# print(div_string.string)

# If multiple child elements use get_text
# This will work
# div_string2 = soup.find("div")
# print(div_string2.prettify())
# print(div_string2.get_text())

# Get a specific property from an element
# link = soup.find("a")
# print(link['href'])
#
# paragraphs = soup.select("p#paragraph-id")
# print(paragraphs[0]["id"])

#########Code Navigation############

# Path Syntax
# print(soup.body.div.h1.string)

# Know the terms: Parent, Sibling, Child
print(soup.body.find("div").find_next_siblings())





