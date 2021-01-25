import os
from TextParser import *
import Config
import Debug

class Task:

    def __init__(self, from_pdf: str):
        from_pdf = from_pdf.split("\n")
        self.conntent = from_pdf[0]
        self.answers = from_pdf[1:]
        self.answers.sort()

    def __str__(self):
        txt = f"{self.conntent}\n"
        for ans in self.answers:
            txt += f"- {ans}\n"
        return txt

    def __eq__(self, oth):
        if self.conntent != oth.conntent:
            return False
        if len(self.answers) != len(oth.answers):
            return False
        for i in range(len(self.answers)):
            if self.answers[i] != oth.answers[i]:
                return False
        return True

    def save_to_testownik(self, dir_path: str, num: int):
        """ public """
        file = open(f"{dir_path}/{num}.txt", "w")
        file.write(self.print_to_testownik())
        file.close()

    def print_to_testownik(self) -> str:
        """ public """
        out = "X"
        for _ in range(len(self.answers)):
            out += "0"
        out += f"\n{self.conntent}\n"
        out += "\n".join(self.answers)
        return out


class TaskList:

    def __init__(self):
        self.tasks = []
        self.all_cnt = 0
        self.unique_cnt = 0

    def __str__(self):
        return self.print_result()

    def add_from_pdf_txt(self, text: str, debug_mode = False):
        """ public """
        parsering = TextParser(text)
        parsering.delete(TextParser.get_patterns(Config.DELETE_PATT))
        parsering.delete_head_lines(Config.DELETE_HEADLINES)

        for task_conn in parsering.split(Config.SPLIT_PATT):
            if task_conn == "":
                continue

            new_task = Task(task_conn)
            self.all_cnt += 1

            if self.is_unique(new_task):
                self.tasks.append(new_task)
                self.unique_cnt += 1
            # IDEA mayby list -> set conversion will be faster than is_unique

        if debug_mode:
            Debug.save_debug_file(f"{self.all_cnt}", str(parsering))

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

    def save_to_testownik(self, dir_path: str):
        """ public """
        try:
            os.mkdir(dir_path)
        except FileExistsError:
            pass

        for i in range(len(self.tasks)):
            self.tasks[i].save_to_testownik(dir_path, i)
