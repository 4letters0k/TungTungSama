import requests, random, os, json
from datetime import date

country = "us"
article_limit = 3
cache_file = "read_news.json"
format_news = {"date": str(date.today()), "urls": []}

def load_read_news(): # โหลดข่าวที่เคยอ่านแล้วจากไฟล์ read_news.json
    
    if os.path.exists(cache_file): #เจอไฟล์ชื่อ read_news.json ไหม?

        with open(cache_file, "r", encoding="utf-8") as f:
            return json.load(f)
        
    return format_news #ไม่เจอไฟล์ read_news.json

def save_read_news(data): #บันทึกข่าวที่อ่านแล้วลงไฟล์
    
    with open(cache_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def fetch_tech_news(api_key): # ดึงข่าว
    
    read_data = load_read_news() #โหลดข่าวที่เคยอ่านแล้ว

    if read_data["date"] != str(date.today()): #เช็คว่าหากข่าวที่โหลดไม่ใช่ข่าว ณ วันนี้จะ save ใหม่
        read_data = format_news

    url = "https://newsapi.org/v2/top-headlines"

    params = {
        "category": "technology",
        "country": country,
        "apiKey": api_key
    }

    res = requests.get(url, params=params)
    data = res.json()

    articles = data.get("articles", [])
    new_articles = [a for a in articles if a.get("url") not in read_data["urls"]]

    if not new_articles:
        return []

    new_articles.sort(key=lambda a: a.get("publishedAt", ""), reverse=True)
    #random.shuffle(new_articles)

    # อัปเดต/save read_news.json - บันทึกข่าวที่อ่าน
    for a in new_articles[:article_limit]:
        if a.get("url"):
            read_data["urls"].append(a["url"])

    save_read_news(read_data)

    return new_articles[:article_limit]