
class TaskParser:
    """ Task parser """

    @staticmethod
    def parser(text: str) -> str:
        """ Parse task text to testownik file """
        task = TaskParser(text)
        return task.generate()

    def __init__(self, text_input: str):
        self.input = text_input.split("\n")
        self.input = list(filter(lambda c: c!='', self.input))
        self.true = None
        self.parse_answers()

    def generate(self) -> str:
        """ private - Generate testownik file """
        return f"{self.get_ans_code()}\n{self.get_content()}{self.get_ans_stat()}\nPRAWDA\nFAŁSZ"

    def get_ans_code(self) -> str:
        """ private """
        if self.true is None:
            return "X11"
        else:
            return "X10" if self.true else "X01"

    def get_ans_stat(self) -> str:
        """ private """
        return ""
        # TODO s answer statictis

    def get_content(self):
        """ private """
        return "\n".join(self.input[0:-1])

    def parse_answers(self):
        """ private """
        text = self.input[-1].split(" | ")
        if "? ? ?" not in text[0]:
            self.true = "PRAWDA" in text[0]
