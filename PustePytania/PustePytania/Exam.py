from PustePytania.Counter import *
from PustePytania.Task import *
from Lib.CompareString import *
from PustePytania.Exceptions import ReapetedTask
import os


class Exam:
    """ [PL] Klasa testu, gromadzi wszystkie pytania. Zajmuje się m.in. zapisem, duplikatami. """
    __strictness = 4        # Strictness in task text comparing

    def __init__(self):
        self.task_list = []

    def __len__(self):
        """ Get length of task list """
        return len(self.task_list)

    def is_empty(self):
        """ Task list is empty? """
        return len(self) == 0

    def clear(self) -> None:
        """ Clear task list """
        del self.task_list
        self.task_list = []

    def sort(self) -> None:
        """ Sort task list """
        self.task_list = list(dict.fromkeys( self.task_list ))
        self.task_list = sorted(self.task_list)

    def append(self, new_task: Task) -> None:
        """ Append new task """
        existing_task = self.__find_already_added(new_task)
        if existing_task is None:
            self.task_list.append( new_task )
        else:
            existing_task.sum_stats(new_task)
            raise ReapetedTask()

    def __find_already_added(self, new_task) -> Task:
        """ Find already existed task on list """
        for task in self.task_list:
            if CompareString.is_similar(task.get_text(), new_task.get_text(), self.__strictness):
                return task

    def save(self, file_name, exam_num, file_head = 0):
        """ Save to file """
        self.sort()

        file = Exam.__create_file(file_name, exam_num)
        file.write(file_head + "\n\n\n")
        file.write("\n\n".join( map(str,self.task_list) ))
        file.close()

    @staticmethod
    def __create_file(file_name, exam_num):
        out_dir = f"{os.getcwd()}/data_files/out"

        try:
            os.mkdir(f"{out_dir}")
        except FileExistsError:
            pass

        return open(f"{out_dir}/{file_name}-{exam_num}.txt", "w", encoding="utf-8")
