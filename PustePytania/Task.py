""" Klasa odpowiedzi na pytania """

class Task:
    """ Klasa odpowiedzi na pytania """
    def __init__(self, reactions):
        self.text       = ""
        self.yes_cnt    = 0
        self.no_cnt     = 0
        self.skip_cnt   = 0
        self.new_exam   = False
        self.skip_photo = False
        self.react(reactions)

    def __lt__(self, other):
        if self.text != other.text:
            return self.text < other.text
        else:
            return self.sum_react() < other.sum_react()

    def __str__(self):
        return f"> {self.text}\n> {self.generate_answer()} | {self.generate_comment()}"

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

            if str(react.emoji) in {"⏭️", "⏭", "⏩", "➡", "↘"}:
                self.skip_cnt = react.count - 1
                # Wiem, ze 1. i 2. emoji wygladaja tak samo, ale widocznie maja rozne kody

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
        self.sum_stats(other)
        self.no_cnt   /= 2
        self.yes_cnt  /= 2
        self.skip_cnt /= 2

    def sum_stats(self, other) -> None:
        """ Metods sum stats of task """
        self.no_cnt   += other.no_cnt
        self.yes_cnt  += other.yes_cnt
        self.skip_cnt += other.skip_cnt
