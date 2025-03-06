import urllib.request
from bs4 import BeautifulSoup

def scrape_article(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")
    paragraphs = soup.find_all("p")
    return " ".join(p.get_text() for p in paragraphs)