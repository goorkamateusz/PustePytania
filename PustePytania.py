from discord.ext import commands
import FunReadChannel as read
from Config import *

# Parametry połączenia
bot = commands.Bot(command_prefix='!')

#
# Komunikat o poprawnym połączeniu.
#
@bot.event
async def on_ready():
    for guild in bot.guilds:
        print( f'{bot.user} jest połączony z:\n{guild.name}(id: {guild.id})\n' )

#
# Czytanie historii i przetwarzanie obrazów
# Czyta historię od najnowszych wiadomości
# 🆕 - oznacza początek listy z zadaniami
#
@bot.command(name="readchannel")
async def readchannel(ctx):
    await read.readchannel( ctx, file_head )

#
# Czyta z historii jedynie ostatni test
#
@bot.command(name="readlast")
async def readlast(ctx):
    await read.readchannel( ctx, file_head, 1 )

#
# Uruchomienie bota
#
bot.run(TOKEN)
