from ImageToText import image_to_text

##
# \brief Czyta z historii kanalow okrelsona ilosc testow.
# \param ctx - discord ctx
# \param file_head - naglowek pliku tekstowego
# \param exam_num_max - ilosc testow do wczytania (0 - jesli wczytac wszystkie)
#
async def readchannel( ctx, file_head, exam_num_max = 0 ):
    print("Trwa przeczesywanie wiadomości...")
    await ctx.send( "Trwa przeczesywanie wiadomości...\n" )

    sc_counter = 0
    skip_counter = 0
    exam_num = 1
    exam = []
    msg_counter = 0

    # Czytanie wiadomości
    async for message in ctx.channel.history(limit=1000):
        msg_counter += 1
        print( msg_counter )

        image_url = ""
        yes_cnt   = 0
        no_cnt    = 0
        skip_q_cnt= 0
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
                    yes_cnt = react.count - 1

                if str(react.emoji) in {"❌", "✖"}:
                    no_cnt = react.count - 1

                if str(react.emoji) in {"⏭", "⏩", "➡", ""}:
                    skip_q_cnt = react.count - 1

                if str(react.emoji) == "🆕":
                    save_now = True

                if str(react.emoji) in {"🔕"}:
                    skip = True

            if not skip :
                # Poleceniestrz
                text = image_to_text( image_url )

                # Odpowiedz
                if abs(yes_cnt - no_cnt) > min( [ yes_cnt, no_cnt ] ) :
                    answer = "PRAWDA" if yes_cnt > no_cnt else "FAŁSZ "
                else:
                    answer = "? ? ? "

                if skip_q_cnt > 0 :
                    answer = " | ".join( [answer, "prawda({}), fałsz({}), nie wiem({})".format( yes_cnt, no_cnt, skip_q_cnt )] )
                else:
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
                file.write( file_head )
                file.write( "\n\n".join( sorted(exam) ) )
                exam_num += 1

                # Czyszczenie
                del exam
                exam = []

                # Koniec
                print( "\nZapisano do pliku exam-{}.txt\n".format(exam_num) )
                file.close()

                # Warunek konca dla exam_num_max
                if exam_num_max != 0 :
                    if exam_num >= exam_num_max :
                        break

    # Koniec czytania
    raport = "Gotowe! Zebraliśmy {} screenów w {} plikach! Pomineliśmy oznaczonych 🔕: {}.".format( sc_counter, exam_num-1, skip_counter )
    await ctx.send( raport )
    print( raport )