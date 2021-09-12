import os
import discord
import csv
import random


phrases = []
with open("phrases.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        phrases.append(row[1])


bot = discord.Client()
@bot.event
async def on_ready():
  print(f"{bot.user}loged in")

@bot.event
async def on_message(msg):
  if msg.content.startswith("!ping"):
    await msg.channel.send("pong")

@bot.event
async def on_message(message):
    if message.content.startswith("$greet"):
        await message.channel.send(f"Hello! How are you {message.author}")
    elif "$thought" in message.content:
        response = phrases[random.randint(0, len(phrases) - 1)]
        await message.channel.send(response)





my_secret = os.environ['Token']
bot.run(my_secret)