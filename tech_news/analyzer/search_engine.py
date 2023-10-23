from tech_news.database import search_news


# Requisito 7
def search_by_title(title):
    search_filter = {"title": {"$regex": title, "$options": "i"}}
    return [
        (item["title"], item["url"]) for item in search_news(search_filter)
    ]


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError
