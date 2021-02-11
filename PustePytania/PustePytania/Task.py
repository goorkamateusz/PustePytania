
class Task:
    """ Klasa reprezentuje odpowiedź na pytanie """
    __ignore_tasks = False

    def __init__(self, reactions):
        self.__text       = ""
        self.__yes_cnt    = 0
        self.__no_cnt     = 0
        self.__skip_cnt   = 0
        self.__new_exam   = False
        self.__skip_photo = False
        self.__react(reactions)

    def __react(self, reactions):
        """ Process reactions """
        for react in reactions:
            if str(react.emoji) in {"🛑"}:
                Task.__ignore_tasks = True

            if str(react.emoji) in {"🆕"}:
                if Task.__ignore_tasks:
                    Task.__ignore_tasks = False
                else:
                    self.__new_exam = True

            if str(react.emoji) in {"🔕"}:
                self.__skip_photo = True
                break

            if str(react.emoji) in {"✔", "✅", "✔️"}:
                self.__yes_cnt = react.count - 1

            if str(react.emoji) in {"❌", "✖"}:
                self.__no_cnt = react.count - 1

            if str(react.emoji) in {"⏭️", "⏭", "⏩", "➡", "↘"}:
                self.__skip_cnt = react.count - 1
                # Wiem, ze 1. i 2. emoji wygladaja tak samo, ale widocznie maja rozne kody

    def set_text(self, text) -> None:
        """ Set text of task """
        self.__text = text

    def get_text(self) -> str:
        """ Get text of task """
        return self.__text

    def skip(self) -> bool:
        """ Skip that task/photo? """
        return self.__skip_photo or Task.__ignore_tasks

    def end_of_exam(self) -> bool:
        """ Is last task of the exam """
        return self.__new_exam

    def average(self, other) -> None:
        """ Count avertage of stats """
        self.sum_stats(other)
        self.__no_cnt   /= 2
        self.__yes_cnt  /= 2
        self.__skip_cnt /= 2

    def __lt__(self, other):
        """ <= operator """
        if self.__text != other.__text:
            return self.__text < other.__text
        else:
            return self.__sum_react() < other.__sum_react()

    def sum_stats(self, other) -> None:
        """ Metods sum stats of task """
        self.__no_cnt   += other.__no_cnt
        self.__yes_cnt  += other.__yes_cnt
        self.__skip_cnt += other.__skip_cnt

    def __sum_react(self):
        """ Return sum of number of reaction """
        return self.__yes_cnt + self.__no_cnt + self.__skip_cnt

    def __str__(self):
        return f"{self.__text}\n{self.__generate_answer()} | {self.__generate_comment()}"

    def __generate_answer(self) -> str:
        if abs(self.__yes_cnt - self.__no_cnt) > min([self.__yes_cnt, self.__no_cnt]) :
            return "PRAWDA" if self.__yes_cnt > self.__no_cnt else "FAŁSZ "
        else:
            return "? ? ? "

    def __generate_comment(self) -> str:
        if self.__skip_cnt > 0 :
            return f"{self.__get_conffidence()} | prawda:{self.__yes_cnt}, fałsz:{self.__no_cnt}, nie wiem:{self.__skip_cnt}"
        else:
            return f"{self.__get_conffidence()} | prawda:{self.__yes_cnt}, fałsz:{self.__no_cnt}"

    def __get_conffidence(self) -> str:
        try:
            out = (100 * max(self.__yes_cnt, self.__no_cnt)) / (self.__yes_cnt+self.__no_cnt+self.__skip_cnt)
        except ZeroDivisionError:
            return "0.00"
        else:
            return round(out, 2)
