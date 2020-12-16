from ImageToText import image_to_text


class Task:
    """ Klasa odpowiedzi na pytania """
    def __init__(self):
        self.text       = ""
        self.yes_cnt    = 0
        self.no_cnt     = 0
        self.skip_cnt   = 0
        self.new_exam   = False
        self.skip_photo = False

    def __lt__(self, other):
        if self.text != other.text:
            return self.text < other.text
        else:
            return self.sum_react() < other.sum_react()

    def __str__(self):
        return self.text+"\n"+self.generate_answer()+" | "+self.generate_comment()

    def set_text(self, text) -> None:
        """ Set text """
        self.text = text

    def sum_react(self):
        """ Return sum of number of reaction """
        return self.yes_cnt + self.no_cnt + self.skip_cnt

    def generate_answer(self) -> str:
        """ Return answer """
        if abs(self.yes_cnt - self.no_cnt) > min([self.yes_cnt, self.no_cnt]) :
            return "PRAWDA" if self.yes_cnt > self.no_cnt else "FAŁSZ "
        else:
            return "? ? ? "

    def generate_comment(self) -> str:
        """ Return comment """
        if self.skip_cnt > 0 :
            return f"prawda({self.yes_cnt}), fałsz({self.no_cnt}), nie wiem({self.skip_cnt})"
        else:
            return f"prawda({self.yes_cnt}), fałsz({self.no_cnt})"

    def react(self, reactions):
        """ Process reactions """
        for react in reactions:
            if str(react.emoji) in {"✔", "✅", "✔️"}:
                self.yes_cnt = react.count - 1

            if str(react.emoji) in {"❌", "✖"}:
                self.no_cnt = react.count - 1

            if str(react.emoji) in {"⏭", "⏩", "➡", "↘"}:
                self.skip_cnt = react.count - 1
                # BUG nie działają reakcje na skip'y

            if str(react.emoji) in {"🆕"}:
                self.new_exam = True

            if str(react.emoji) in {"🔕"}:
                self.skip_photo = True

    def skip(self) -> bool:
        """ Is skip task """
        return self.skip_photo

    def end_of_exam(self) -> bool:
        """ Is last task of the exam """
        return self.new_exam

    def average(self, other) -> None:
        """ Count avertage of stats """
        self.no_cnt   += other.no_cnt
        self.yes_cnt  += other.yes_cnt
        self.skip_cnt += other.skip_cnt
        self.no_cnt   /= 2
        self.yes_cnt  /= 2
        self.skip_cnt /= 2


class Exam:
    """ Klasa testu """
    def __init__(self):
        self.task_list = []

    def __len__(self):
        return len(self.task_list)

    def append(self, task: Task):
        """ Append new task """
        self.task_list.append( task )

    def sort(self) -> None:
        """ Sort task list """
        self.task_list = sorted(self.task_list)

    def clear(self) -> None:
        """ Clear task list """
        del self.task_list
        self.task_list = []

    def remove_dup(self) -> None:
        """ Remove duplicate"""
        self.task_list = list(dict.fromkeys( self.task_list ))
        self.sort()

    def save(self, file_name, exam_num, file_head = 0):
        """ Save to file """
        file = open(f"{file_name}-{exam_num}.txt", "w", encoding="utf-8")
        file.write( file_head )

        file.write( "\n\n".join( map(str,self.task_list) ) )
        file.close()


class Counter:
    """ Counter of data """
    def __init__(self):
        self.screen = 0
        self.skip   = 0
        self.exam   = 0
        self.msg    = 0

    def limit_of_exam(self, exam_num_max = 0):
        """ Limit of exam"""
        if exam_num_max == 0:
            return True
        else:
            return self.exam >= exam_num_max


async def readchannel( ctx, file_head, exam_num_max = 0 ):
    """ Czyta z historii kanalow okrelsona ilosc testow.
    ctx - discord ctx
    file_head - naglowek pliku tekstowego
    exam_num_max - ilosc testow do wczytania (0 - jesli wczytac wszystkie)
    """
    print("Trwa przeczesywanie wiadomości...")
    await ctx.send( "Trwa przeczesywanie wiadomości...\n" )

    exam = Exam()
    cnt = Counter()

    async for message in ctx.channel.history(limit=1000):
        cnt.msg += 1

        for att in message.attachments:
            if ".png" in att.url or ".jpg" in att.url:
                task = Task()
                task.react(message.reactions)

                if not task.skip():
                    task.set_text( image_to_text(att.url) )
                    exam.append( task )
                    cnt.screen += 1

                    print( cnt.msg, '\n', cnt.screen, ' ', task )
                else:
                    cnt.skip += 1

                if task.end_of_exam():
                    exam.remove_dup()
                    exam.save("exam", cnt.exam, file_head)
                    exam.clear()
                    cnt.exam += 1

                    print( f"\n--- Zapisan {cnt.exam} test ---\n" )

                    if cnt.limit_of_exam( exam_num_max ):
                        break

        if cnt.limit_of_exam( exam_num_max ):
            break

    # Koniec czytania
    raport = [  f"Gotowe! Zebraliśmy {cnt.screen} screenów w {cnt.exam} plikach!",
                f" Pomineliśmy oznaczonych 🔕: {int(cnt.skip)}." ]
    raport = "".join( raport )
    await ctx.send( raport )
    print( raport )
