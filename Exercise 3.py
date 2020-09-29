import requests
from bs4 import BeautifulSoup as bs
import re

# Load the webpage content
r = requests.get("https://keithgalli.github.io/web-scraping/webpage.html")

# Convert to a beautiful soup object
webpage = bs(r.content, "html.parser")

# Grab all fun facts that use the word "is"
facts = webpage.select("ul.fun-facts li")
facts_with_is = [fact.find(string=re.compile("is")) for fact in facts]
facts_with_is = [fact.find_parent().get_text() for fact in facts_with_is if fact]
print(facts_with_is)