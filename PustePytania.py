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

    sc_counter = 0
    skip_counter = 0
    exam_num = 1
    exam = []

    # Czytanie wiadomości
    async for message in ctx.channel.history():
        image_url = ""
        yes_cnt   = 0
        no_cnt    = 0
        save_now  = False
        skip      = False

        # Sprawdza załączniki
        for att in message.attachments:
            if ".png" in att.url or ".jpg" in att.url:
                image_url = att.url
                break

        if image_url != "" :
            # Czyta reakcje
            for react in message.reactions:
                if str(react.emoji) in {"✔", "✅", "✔️"}:
                    yes_cnt = react.count

                if str(react.emoji) in {"❌", "✖"}:
                    no_cnt = react.count

                if str(react.emoji) == "🆕":
                    save_now = True

                if str(react.emoji) in {"🔕"}:
                    skip = True

            if not skip :
                # Polecenie
                text = image_to_text( image_url )

                # Odpowiedz
                if yes_cnt != no_cnt :
                    answer = "PRAWDA" if yes_cnt > no_cnt else "FAŁSZ"
                else:
                    answer = "???"

                answer = " | ".join( [answer, "prawda({}), fałsz({})".format( yes_cnt, no_cnt )] )

                # Zapisz
                sc_counter += 1
                exam.append( "\n".join([text, answer]) )
                print( text )
                print( ": ", answer )
            else:
                skip_counter += 1

            if save_now:
                # Zapisuje do pliku
                file = open("exam-{}.txt".format(exam_num), "w", encoding="utf-8")
                file.write( "\n\n".join( exam ) )
                exam_num += 1
                del exam
                exam = []
                print( "\nZapisano do pliku exam-{}.txt\n".format(exam_num) )

    # Koniec czytania
    raport = "Gotowe! Zebraliśmy {} screenów w {} plikach! Pomineliśmy oznaczonych 🔕: {}.".format( sc_counter, exam_num-1, skip_counter )
    await ctx.send( raport )
    print( raport )

#
# Uruchomienie bota
#
bot.run(TOKEN)

