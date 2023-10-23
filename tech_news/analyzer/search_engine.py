from tech_news.database import search_news
from datetime import datetime


# Requisito 7
def search_by_title(title):
    search_filter = {"title": {"$regex": title, "$options": "i"}}
    return [
        (item["title"], item["url"]) for item in search_news(search_filter)
    ]


# Requisito 8
def search_by_date(date):
    try:
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        format_date = date_obj.strftime("%d/%m/%Y")
        search_filter = {"timestamp": {"$regex": format_date}}
        results = search_news(search_filter)
        return [(result["title"], result["url"]) for result in results]
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError
