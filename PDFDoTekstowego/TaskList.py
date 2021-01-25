from TextParser import *
import Config

class Task:

    def __init__(self, from_pdf: str):
        self.conntent = from_pdf

    def __str__(self):
        return self.conntent

    def __eq__(self, oth):
        return self.conntent == oth.conntent

    @staticmethod
    def parse(from_pdf: str) -> str:
        """ private """
        raise NotImplementedError()


class TaskList:

    def __init__(self):
        self.tasks = []
        self.all_cnt = 0
        self.unique_cnt = 0

    def __str__(self):
        return self.print_result()

    def add_from_pdf_txt(self, text: str):
        """ public """
        parsering = TextParser(text)
        parsering.delete(TextParser.get_patterns(Config.DELETE_PATT))
        parsering.delete_head_lines(Config.DELETE_HEADLINES)

        for task_conn in parsering.split(Config.SPLIT_PATT):
            new_task = Task(task_conn)
            self.all_cnt += 1

            if self.is_unique(new_task):
                self.tasks.append(new_task)
                self.unique_cnt += 1
            # IDEA mayby list -> set conversion will be faster than is_unique


    def save_to_file(self, file_path: str):
        """ public """
        with open(file_path, "w") as file:
            file.write( self.print_result() )

    def print_report(self) -> str:
        """ public """
        return f"Przetowrzonych zadań {self.all_cnt}, w tym {self.unique_cnt} unikatowych"

    def is_unique(self, new_task: Task) -> bool:
        """ private """
        for task in self.tasks:
            if task == new_task:
                return False
        return True

    def print_result(self) -> str:
        """ private """
        out = ""
        for i in range(len(self.tasks)):
            out += f"## Pytanie {i}\n{self.tasks[i]}\n\n"
        return out
