from tech_news.database import get_collection


# Requisito 10
def top_5_categories():
    aggregation_pipeline = [
        {"$group": {"_id": "$category", "count": {"$sum": 1}}},
        {"$sort": {"count": -1, "_id": 1}},
        {"$limit": 5},
    ]

    return [
        result["_id"]
        for result in get_collection().aggregate(aggregation_pipeline)
    ]
