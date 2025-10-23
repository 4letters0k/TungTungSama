config.json

{
    "discord_token": "Your_Bot_Token",
    "news_api_key": "Your_news_Api_key",
    "ai_api_key": "Your_Ai_Api_key",
    "default_articles_limit": "Your_Articles_Limit"
}

# 🤖 TungTungSama – AI News Summary Discord Bot

TungTungSama is a Discord bot built with **Python** that automatically fetches the latest **technology news**, summarizes them using **Gemini AI**, and sends concise summaries directly into your Discord channel — all in a friendly and stylish tone.

> 📰 “Your personal tech news assistant — simple, smart, and never repeats old stories!”

---

## 🌟 Features

- 🔹 **Fetches tech news** automatically from reliable sources via public API  
- 🔹 **Summarizes news using Gemini AI (Gemini 2.0 Flash)**  
- 🔹 **Customizable number of summaries** — e.g. `!news 3` to get 3 news summaries  
- 🔹 **Smart caching system** — remembers read news and avoids duplicates  
- 🔹 **Natural and friendly conversation style** (TungTungSama’s personality!)  
- 🔹 **Built modularly** using `main.py` (Discord handler) and `news_fetch.py` (API logic)

---

## 🛠️ Technologies Used

| Component | Description |
|------------|--------------|
| **Language** | Python 3 |
| **Libraries** | `discord.py`, `requests`, `google-generativeai`, `json`, `datetime`, `os` |
| **AI Model** | Gemini 2.0 Flash (Google Generative AI API) |
| **Platform** | Discord Bot |
