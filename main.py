import discord
from discord.ext import commands
import json
import os
import pydest

# Get configuration.json
with open("configuration.json", "r") as config: 
	data = json.load(config)
	token = data["token"]
	prefix = data["prefix"]
	owner_id = data["owner_id"]
	destiny_key = data["destiny_key"]



# Intents
intents = discord.Intents.default()
# The bot
bot = discord.Bot(description="I'm here to help, guardian.")

# # Load cogs
# if __name__ == '__main__':
# 	for filename in os.listdir("Cogs"):
# 		if filename.endswith(".py"):
# 			bot.load_extension(f"Cogs.{filename[:-3]}")

@bot.event
async def on_ready():
	print(f"We have logged in as {bot.user}")
	print(discord.__version__)
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name =f"/help"))

@bot.slash_command(guild_ids=["875392150962061352"])
async def xur(ctx):
	# bungo:pydest.Pydest = pydest.Pydest(api_key=destiny_key)
	
	await ctx.respond("Function is under development.")

@bot.slash_command(guild_ids=["875392150962061352"])
async def xur(ctx):
	# bungo:pydest.Pydest = pydest.Pydest(api_key=destiny_key)
	
	await ctx.respond("Function is under development.")

bot.run(token)