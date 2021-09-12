import os
import discord

bot = discord.Client()
@bot.event
async def on_ready():
  print(f"{bot.user}loged in")

@bot.event
async def on_message(msg):
  if msg.content.startswith("!ping"):
    await msg.channel.send("pong")



my_secret = os.environ['Token']
bot.run(my_secret)