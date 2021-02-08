""" Klasa odpowiedzi na pytania """

class Task:
    """ Klasa odpowiedzi na pytania """
    _ignore_tasks = False

    def __init__(self, reactions):
        self.text       = ""
        self.yes_cnt    = 0
        self.no_cnt     = 0
        self.skip_cnt   = 0
        self.new_exam   = False
        self.skip_photo = False
        self._react(reactions)

    def __lt__(self, other):
        if self.text != other.text:
            return self.text < other.text
        else:
            return self._sum_react() < other.sum_react()

    def __str__(self):
        return f"{self.text}\n{self._generate_answer()} | {self._generate_comment()}"

    def set_text(self, text) -> None:
        """ Set text """
        self.text = text

    def skip(self) -> bool:
        """ Is skip task """
        return self.skip_photo or Task._ignore_tasks

    def end_of_exam(self) -> bool:
        """ Is last task of the exam """
        return self.new_exam

    def average(self, other) -> None:
        """ Count avertage of stats """
        self.sum_stats(other)
        self.no_cnt   /= 2
        self.yes_cnt  /= 2
        self.skip_cnt /= 2

    def sum_stats(self, other) -> None:
        """ Metods sum stats of task """
        self.no_cnt   += other.no_cnt
        self.yes_cnt  += other.yes_cnt
        self.skip_cnt += other.skip_cnt


    def _sum_react(self):
        """ private; Return sum of number of reaction """
        return self.yes_cnt + self.no_cnt + self.skip_cnt

    def _generate_answer(self) -> str:
        """ private """
        if abs(self.yes_cnt - self.no_cnt) > min([self.yes_cnt, self.no_cnt]) :
            return "PRAWDA" if self.yes_cnt > self.no_cnt else "FAŁSZ "
        else:
            return "? ? ? "

    def _generate_comment(self) -> str:
        """ private """
        if self.skip_cnt > 0 :
            return f"{self._get_conffidence()} | prawda:{self.yes_cnt}, fałsz:{self.no_cnt}, nie wiem:{self.skip_cnt}"
        else:
            return f"{self._get_conffidence()} | prawda:{self.yes_cnt}, fałsz:{self.no_cnt}"

    def _get_conffidence(self) -> str:
        try:
            out = (100 * max(self.yes_cnt, self.no_cnt)) / (self.yes_cnt+self.no_cnt+self.skip_cnt)
        except ZeroDivisionError:
            return "0.00"
        else:
            return round(out, 2)

    def _react(self, reactions):
        """ Process reactions """
        for react in reactions:
            if str(react.emoji) in {"🛑"}:
                Task._ignore_tasks = True

            if str(react.emoji) in {"🆕"}:
                if Task._ignore_tasks:
                    Task._ignore_tasks = False
                else:
                    self.new_exam = True

            if str(react.emoji) in {"🔕"}:
                self.skip_photo = True
                break

            if str(react.emoji) in {"✔", "✅", "✔️"}:
                self.yes_cnt = react.count - 1

            if str(react.emoji) in {"❌", "✖"}:
                self.no_cnt = react.count - 1

            if str(react.emoji) in {"⏭️", "⏭", "⏩", "➡", "↘"}:
                self.skip_cnt = react.count - 1
                # Wiem, ze 1. i 2. emoji wygladaja tak samo, ale widocznie maja rozne kody
