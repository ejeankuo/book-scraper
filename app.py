# the logic for web scraper
from bs4 import BeautifulSoup
import requests

BASE_URL = "http://books.toscrape.com/"

# scrape html content from website
response = requests.get(BASE_URL)

# convert raw html to beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
