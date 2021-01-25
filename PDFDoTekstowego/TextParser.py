import re


class TextParser:

    def __init__(self, text: str):
        self.text = text

    def __str__(self):
        return self.text

    def delete_head_lines(self, num: int):
        self.text = "\n".join(self.text.split("\n")[num:])

    def delete(self, patterns: list):
        """ public """
        self.replace(patterns, "")

    def replace(self, patterns: list, rep: str):
        """ public """
        for pattern in patterns:
            self.text = pattern.sub(rep, self.text)

    def split(self, pattern) -> list:
        """ public """
        return self.text.split(pattern)

    @staticmethod
    def get_patterns(list_reg: list) -> list:
        """ public """
        patterns = []
        for reg in list_reg:
            patterns.append(re.compile(reg))
        return patterns
        