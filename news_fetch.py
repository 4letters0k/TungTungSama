import requests

country = "us"
article_limit = 3

def fetch_tech_news(api_key):

    url = "https://newsapi.org/v2/top-headlines"

    params = {
        "category": "technology",
        "country": country,
        "apiKey": api_key
    }

    res = requests.get(url, params=params)
    articles = res.json().get("articles", [])

    return articles[:article_limit]