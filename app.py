# the logic for web scraper
from bs4 import BeautifulSoup
import requests

BASE_URL = "http://books.toscrape.com/"

# scrape html content from website
response = requests.get(BASE_URL)
response.encoding = 'utf-8'

# convert raw html to beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')

books = soup.select("article.product_pod")

# obtain all of the titles, prices, and ratings
for b in books:
    titles = b.select_one("h3 a")['title'] # list of titles
    prices = b.select_one("div.product_price p.price_color").text # list of prices
    ratings = b.select_one("p.star-rating")['class'][1] # list of ratings
    