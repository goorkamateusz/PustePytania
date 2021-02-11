import Config
from PustePytania.PustePytania import *
from PustePytania.RenameFiles import *
from Bot.Downloader import *
from Bot.Report import *
from discord.ext import commands

if __name__ == "__main__":

    if not PustePytania.check_config(Config):
        exit()

    # Parametry połączenia
    bot = commands.Bot(command_prefix='!')

    @bot.event
    async def on_ready():
        """
        Wyświetla komunikat o poprawnym połaczeniu
        """
        for guild in bot.guilds:
            print( f'{bot.user} jest połączony z:\n{guild.name}(id: {guild.id})\n' )


    @bot.command(name="readchannel")
    async def readchannel(ctx):
        """
        Czyta i przetwarza obrazy z historii z kanału, na którym został wywołany.
        """
        await PustePytania.readchannel( ctx, Config.FILE_HEAD )
        RenameFiles.rename(Config.EXAM_NAME)


    @bot.command(name="readlast")
    async def readlast(ctx):
        """
        Czyta i przetwarza obrazy z historii do najświeższej reakcji 🆕 (tylko ostatni tesst)
        """
        await PustePytania.readchannel( ctx, Config.FILE_HEAD, 1 )
        RenameFiles.rename(Config.EXAM_NAME)


    @bot.command(name="download")
    async def download(ctx, arg):
        """ Pobiera pliki o określonym formacie z kanału. """
        await Downloader.get_all_from_channel(ctx, arg)


    @bot.command(name="echo")
    async def send_message(ctx, arg):
        """
        Wysyła wiadomość o podanej treści wiadomość niżej.

        Na przykład:
            !echo "treść do wyświetlenia"
        """
        await Report.echo(ctx, arg)


    @bot.command(name="test")
    async def test_last_message(ctx):
        """
        Wysyła wiadomość z wynikiem ostatniej z przetworzonych wiadomości.
        """
        # todo
        raise NotImplemented()


    # Uruchomienie bota
    bot.run(Config.TOKEN)
