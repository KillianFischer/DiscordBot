import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN: str = os.getenv('DISCORD_TOKEN', '') 

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    await bot.wait_until_ready()
    try:
        synced = await bot.tree.sync()
        print(f'Synced {len(synced)} command(s)')
    except Exception as e:
        print(f'Error syncing commands: {e}')
    
    if bot.user is not None:
        print(f'Logged in as {bot.user} (ID: {bot.user.id})')

# commands
@bot.tree.command(name='hello', description='Say hello!')
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f'Hello, {interaction.user.mention}!')

bot.run(TOKEN)
