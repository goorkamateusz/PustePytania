from discord.ext import commands
import Config
from PustePytania import *

if __name__ == "__main__":

    if Config.TOKEN == "twoj token":
        print("Error: Skonfiguruj swoj token w pliku PustePytania/Config.py!")
        exit()

    # Parametry połączenia
    bot = commands.Bot(command_prefix='!')

    @bot.event
    async def on_ready():
        """ Komunikat o poprawnym połaczeniu """
        for guild in bot.guilds:
            print( f'{bot.user} jest połączony z:\n{guild.name}(id: {guild.id})\n' )


    @bot.command(name="readchannel")
    async def readchannel(ctx):
        """ Czyta i przetwarza historie z kanału, na którym został wywołany. """
        await PustePytania.readchannel( ctx, Config.file_head )


    @bot.command(name="readlast")
    async def readlast(ctx):
        """ Czyta i przetwarza wiadomości do najświeższej reakcji 🆕"""
        await PustePytania.readchannel( ctx, Config.file_head, 1 )

    # Uruchomienie bota
    bot.run(Config.TOKEN)
