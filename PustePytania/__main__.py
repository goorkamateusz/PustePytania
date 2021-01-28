from discord.ext import commands
import Config
from PustePytania import *
from RenameFiles import *
from Downloader import *
from Report import *

if __name__ == "__main__":

    if not PustePytania.check_config(Config):
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
        RenameFiles.rename(Config.EXAM_NAME)


    @bot.command(name="readlast")
    async def readlast(ctx):
        """ Czyta i przetwarza wiadomości do najświeższej reakcji 🆕"""
        await PustePytania.readchannel( ctx, Config.file_head, 1 )
        RenameFiles.rename(Config.EXAM_NAME)


    @bot.command(name="download")
    async def download(ctx, arg):
        """ Pobiera pliki o określonym formacie z kanału """
        await Downloader.get_all_from_channel(ctx, arg)


    @bot.command(name="echo")
    async def send_message(ctx, arg):
        """ Wysyła wiadomość o podanej treści wiadomość niżej """
        await Report.echo(ctx, arg)


    # Uruchomienie bota
    bot.run(Config.TOKEN)
