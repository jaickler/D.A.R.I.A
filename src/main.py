import discord
from discord.ext import commands
import json
import os

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

# Establishes Xur View
@bot.slash_command(guild_ids=["875392150962061352"])
async def xur(ctx):
    embed = discord.Embed(
        title="Peddler of strange curios",
        description="Xûr's motives are not his own. He bows to his distant masters, the Nine.",
        color=discord.Colour.blurple(), # Pycord provides a class with default colors you can choose from
    )
    embed.add_field(name="Xûr's Inventory", value="Xûr changes his inventory every week, so be sure to check back next Friday.")

    embed.add_field(name="Warlock", value="Test", inline=True)
    embed.add_field(name="Titan", value="Test", inline=True)
    embed.add_field(name="Hunter", value="Test", inline=True)
 
    embed.set_footer(text="Come again, guardian.") # footers can have icons too
    embed.set_author(name="Xûr", icon_url="https://static.wikia.nocookie.net/destinypedia/images/6/67/Xur_Agent_of_the_Nine.png/revision/latest?cb=20140912180018")
    embed.set_thumbnail(url="https://ibb.co/JxFWT4N")
    embed.set_image(url="https://cdn1.dotesports.com/wp-content/uploads/2021/12/07172923/2021_30th_Press_Kit_Compressed_Dares_14.jpg")
    
    await ctx.respond("I have fetched the nine, guardian.", embed=embed) # Send the embed with some text

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
async def xur1(ctx):
    # bungo:pydest.Pydest = pydest.Pydest(api_key=destiny_key)
    
    await ctx.respond("Function is under development.")

@bot.slash_command(guild_ids=["875392150962061352"])
async def xur2(ctx):
    # bungo:pydest.Pydest = pydest.Pydest(api_key=destiny_key)
    
    await ctx.respond("Function is under development.")

bot.run(token)