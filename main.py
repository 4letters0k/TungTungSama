import discord, json
from discord.ext import commands

from summarizer import summarize_news

# Load config
config = json.load(open("config.json", encoding="utf-8"))

# Set Discord Bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_message(message):
    #print(f"Message received: {message.content}")  # เช็กใน terminal
    if message.author == bot.user:
        return
    if message.content.startswith('!news'):
        await message.channel.send("กำลังดึงข่าวให้อยู่ครับ...")
    
    await bot.process_commands(message  )


@bot.event
async def on_ready():
    print(f"{bot.user} พร้อมทำงาน!")

@bot.command()
async def news(ctx): # ctx ประกอบไปด้วย ชื่อ ข้อความ channel 

    from news_fetch import fetch_tech_news

    await ctx.send("⏳ กำลังดึงข่าวเทคโนโลยีและสรุปให้ครับ Tung~Tung~ 💫")
    articles = fetch_tech_news(config["news_api_key"])

    # ไม่เจอข่าวใหม่แล้ว หรือ articles = []
    if not articles:
        await ctx.send("📰 วันนี้ TungTungSama ไม่มีข่าวใหม่แล้วนะ! ลองใหม่พรุ่งนี้ 😎")
        return

    for a in articles:
        
        title = a["title"]
        description = a.get("description", "")
        url = a.get("url", "")

        # ให้ Ai สรุป (ใช้ gemini)
        summary = summarize_news(config["ai_api_key"], description or title)

        # ส่งข้อความกลับ Discord
        message = f"**{title}**\n{summary}\n🔗 {url}"
        await ctx.send(message)

bot.run(config["discord_token"])