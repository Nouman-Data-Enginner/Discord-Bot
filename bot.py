import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    cogs = ["cogs.news", "cogs.fun", "cogs.crypto"]
    for cog in cogs:
        await bot.load_extension(cog)
    print(f"✅ Bot ready: {bot.user}")
    print(f"📦 {len(cogs)} cogs loaded!")

bot.run(os.getenv("DISCORD_TOKEN"))