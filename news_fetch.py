import requests, random, os, json
from datetime import date

country = "us"
#article_limit = 3
cache_file = "read_news.json"
format_news = {"date": str(date.today()), "urls": []}
warn_text = "อ๊ะ ดูเหมือนคุณจะพิมพ์จำนวนข่าวไม่ถูกต้องนะครับ 😅\n งั้นจะสรุปแค่ 3 ข่าวนะงับ✨\n ลองพิมพ์แบบนี้สิครับ เช่น `!news 3` เพื่อให้ผมสรุปข่าว 3 ข่าว 🔍"

def get_articles_limit(value, default_value):
    try:
        value = int(value)
    except ValueError:
        return default_value, warn_text
    
    if value <= 0:
        return default_value, warn_text
    
    return value, f"เข้าใจแล้วครับ! เดี๋ยวผมจะสรุปข่าวเทคโนโลยี {value} ข่าวให้เลย 📰✨"

def load_read_news(): # โหลดข่าวที่เคยอ่านแล้วจากไฟล์ read_news.json
    
    if os.path.exists(cache_file): #เจอไฟล์ชื่อ read_news.json ไหม?

        with open(cache_file, "r", encoding="utf-8") as f:
            return json.load(f)
        
    return format_news #ไม่เจอไฟล์ read_news.json

def save_read_news(data): #บันทึกข่าวที่อ่านแล้วลงไฟล์
    
    with open(cache_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def fetch_tech_news(api_key, default_articles_limit, art_limit): # ดึงข่าว

    read_data = load_read_news() #โหลดข่าวที่เคยอ่านแล้ว
    special_text = ""

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
    total_news = len(new_articles)

    if not new_articles:
        return [], ""

    new_articles.sort(key=lambda a: a.get("publishedAt", ""), reverse=True)
    #random.shuffle(new_articles)

    # ตรวจว่า articles limit นั้น valid ไหมม
    article_limit, special_text = get_articles_limit(art_limit, default_articles_limit)
    if article_limit > total_news: # จำนวนข่าวที่จะให้สรุปมีมากกว่าที่จำนวนข่าวทั้งหมดมี
        article_limit = total_news
        special_text = f"วันนี้มีข่าวใหม่ให้สรุปแค่ {total_news} ข่าวเองครับ 😅\n ผมจะสรุปทั้งหมดให้เลยนะครับ!"

    # อัปเดต/save read_news.json - บันทึกข่าวที่อ่าน
    for a in new_articles[:article_limit]:
        if a.get("url"):
            read_data["urls"].append(a["url"])

    save_read_news(read_data)

    return new_articles[:article_limit], special_text