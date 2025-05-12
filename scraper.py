
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def fetch_articles():
    url = "https://www.vesti.mk/category/makedonija"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    articles = []
    for item in soup.select("a.newslink"):
        link = item.get("href")
        title = item.get_text(strip=True)
        if not link.startswith("http"):
            link = "https://www.vesti.mk" + link
        articles.append({
            "title": title,
            "link": link,
            "pubDate": datetime.now().strftime("%a, %d %b %Y %H:%M:%S +0000"),
            "description": title,
        })

    return articles
