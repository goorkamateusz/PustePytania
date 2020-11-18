from discord.ext import commands
from ImageToText import image_to_text

# Parametry połączenia
TOKEN = "{token}"
GUILD = "{guild}"

bot = commands.Bot(command_prefix='!')

#
# Komunikat o poprawnym połączeniu.
#
@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == GUILD:
            break

    print( f'{bot.user} jest połączony z:\n{guild.name}(id: {guild.id})\n' )

#
# Czytanie historii i przetwarzanie obrazów
# Czyta historię od najnowszych wiadomości
# 🆕 - oznacza początek listy z zadaniami
#
@bot.command(name="readchannel")
async def history(ctx):
    print("Trwa przeczesywanie wiadomości...")
    await ctx.send( "Trwa przeczesywanie wiadomości...\n" )

    examNum = 1
    exam = []

    # Czytanie wiadomości
    async for message in ctx.channel.history():
        text = ""
        yes = 0
        no = 0

        for att in message.attachments:
            if ".png" in att.url or ".jpg" in att.url:
                text = image_to_text( att.url )

        if text != "" :
            for react in message.reactions:
                if str(react.emoji) in {"✔", "✅", "✔️"}:
                    yes = react.count

                if str(react.emoji) in {"❌", "✖"}:
                    no = react.count

                if str(react.emoji) == "🆕":
                    file = open("exam-{}.txt".format(examNum), "w", encoding="utf-8")
                    file.write( "\n\n".join( exam ) )
                    examNum = examNum + 1
                    del exam
                    exam = []

            if yes != no :
                answer = "TAK" if yes > no else "NIE"
            else:
                answer = "???"

            answer = " | ".join( [answer, "tak ({}), nie ({})".format( yes, no )] )

            print( text )
            print( answer )
            exam.append( "\n".join([text, answer]) )

    await ctx.send("Gotowe!")
    print("\nGotowe!")

#
# Uruchomienie bota
#
bot.run(TOKEN)

