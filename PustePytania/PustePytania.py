from ImageToText import image_to_text
from Exam import *

class PustePytania:
    """ Główna klasa programu """

    @staticmethod
    async def readchannel(ctx, file_head, exam_num_max = 0 ):
        """ Czyta z historii kanalow okrelsona ilosc testow.
        ctx - discord ctx
        file_head - naglowek pliku tekstowego
        exam_num_max - ilosc testow do wczytania (0 - jesli wczytac wszystkie)
        """

        pustepytania = PustePytania(ctx)
        pustepytania.echo("Trwa przeczesywanie wiadomości...")

        exam = Exam()
        cnt = Counter()

        async for message in ctx.channel.history(limit=None):
            cnt.msg += 1

            for att in message.attachments:
                if PustePytania.is_photo(att.url):
                    task = Task(message.reactions)

                    if not task.skip():
                        task.set_text( image_to_text(att.url) )
                        exam.append( task )
                        cnt.screen += 1

                        print( cnt.msg, "\n", cnt.screen, " ", task )
                    else:
                        cnt.skip += 1

                    if task.end_of_exam():
                        exam.save("exam", cnt.exam, file_head)
                        exam.clear()
                        cnt.exam += 1
                        cnt.reapeted += exam.reapeted_cnt

                        print( f"\n--- Zapisan {cnt.exam} test ---\n" )

                        if cnt.limit_of_exam( exam_num_max ):
                            break

            if cnt.limit_of_exam( exam_num_max ):
                break

        # Koniec czytania
        raport = [  f"Gotowe!\nZebraliśmy {cnt.screen} screenów w {cnt.exam} plikach!\n",
                    f"Pomineliśmy oznaczonych 🔕: {cnt.skip}. Powtórzeń: {cnt.reapeted}" ]
        raport = "".join( raport )
        pustepytania.echo(raport)



    def __init__(self, ctx):
        self.ctx = ctx

    def echo(self, message: str) -> None:
        """ Print and send value """
        await self.ctx.send(message)
        print(message)

    @staticmethod
    def is_photo(url: str) -> bool:
        """ Is photo? """
        url = url.lower()
        return ".png" in url or ".jpg" in url


