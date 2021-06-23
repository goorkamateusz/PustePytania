from PustePytania.ImageToText import image_to_text
from PustePytania.Exam import *
from Bot import Report

class PustePytania:
    """ [PL] Główna klasa programu """

    @staticmethod
    def check_config(config) -> bool:
        """ [PL] Sprawdza poprawnosc pliku konfiguracji """
        if config.TOKEN == "twoj token":
            print("Error: Skonfiguruj swoj token w pliku PustePytania/Config.py!")
            return False

        if "\n\n\n" in config.FILE_HEAD:
            print("Error: Naglowek pliku nie powinnien zawierac dwoch pustych linii")
            return False

        return True

    @staticmethod
    async def readchannel(ctx, file_head, exam_num_max = 0 ):
        """ [PL] Czyta z historii kanalow okrelsona ilosc testow.
        ctx - discord ctx
        file_head - naglowek pliku tekstowego
        exam_num_max - ilosc testow do wczytania (0 - jesli wczytac wszystkie)
        """

        pustepytania = PustePytania(ctx)
        await pustepytania.echo("Trwa przeczesywanie wiadomości...")

        exam = Exam()
        cnt = Counter()

        async for message in ctx.channel.history(limit=None):
            cnt.msg += 1

            for att in message.attachments:
                if PustePytania.is_photo(att.url):
                    task = Task(message.reactions)

                    if not task.skip():
                        task.set_text( image_to_text(att.url) )
                        cnt.screen += 1

                        try:
                            exam.append( task )
                        except ReapetedTask:
                            print( f"\n{cnt.msg} msg, {cnt.screen} img | POWTORZENIE!" )
                            cnt.reapeted += 1
                        else:
                            print( f"\n{cnt.msg} msg, {cnt.screen} img | " )

                        print( task )
                    else:
                        cnt.skip += 1

                    if task.end_of_exam():
                        exam.save("exam", cnt.exam, file_head)
                        exam.clear()
                        cnt.exam += 1

                        print( f"\n=== Zapisano {cnt.exam} test ============================\n" )

                        if cnt.limit_of_exam( exam_num_max ):
                            break

            if cnt.limit_of_exam( exam_num_max ):
                break

        # Koniec czytania
        print()
        raport = [  f"Gotowe!\nZebraliśmy {cnt.screen} screenów w {cnt.exam} plikach!\n",
                    f"Pomineliśmy oznaczonych 🔕: {cnt.skip}. Powtórzeń: {cnt.reapeted}" ]
        raport = "".join( raport )
        await pustepytania.echo(raport)


    def __init__(self, ctx):
        self.ctx = ctx

    async def echo(self, message: str) -> None:
        """ Print and send value """
        await Report.echo(self.ctx, message)

    @staticmethod
    def is_photo(url: str) -> bool:
        """ Is photo? """
        url = url.lower()
        return ".png" in url or ".jpg" in url


