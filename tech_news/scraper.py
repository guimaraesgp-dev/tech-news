import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        headers = {"user-agent": "Fake user-agent"}
        time.sleep(1)
        response = requests.get(url, timeout=3, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except requests.exceptions.Timeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)
    link = selector.css("a.cs-overlay-link::attr(href)").getall()
    return link


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page_link = selector.css(".next::attr(href)").get()
    return next_page_link


# Requisito 4
def scrape_news(html_content):
    selector = Selector(text=html_content)

    info = {
        "url": selector.css('link[rel="canonical"]::attr(href)').get(),
        "title": selector.css("h1.entry-title::text").get().strip(),
        "timestamp": selector.css("li.meta-date::text").get(),
        "writer": selector.css("h5.title-author span.fn a::text")
        .get()
        .strip(),
        "reading_time": int(
            selector.css("li.meta-reading-time::text").re_first(r"\d+")
        ),
        "summary": "".join(
            selector.css(".entry-content > p:first-of-type *::text").getall()
        ).strip(),
        "category": selector.css(".meta-category span.label::text")
        .get()
        .strip(),
    }

    return info


# Requisito 5
def get_tech_news(amount):
    url = "https://blog.betrybe.com/"
    dbnews = []

    while len(dbnews) < amount:
        html_content = fetch(url)
        updates = scrape_updates(html_content)
        dbnews.extend([scrape_news(fetch(news)) for news in updates])
        url = scrape_next_page_link(html_content)

    create_news(dbnews[:amount])
    return dbnews[:amount]
