""" Klasa testu """
from Task import *
from Counter import *
from CompareString import *
from ImageToText import image_to_text
import os


class reapetedTask(Exception):
    pass

class Exam:
    """ Klasa testu """
    strictness = 4

    def __init__(self):
        self.task_list = []

    def __len__(self):
        return len(self.task_list)

    def is_empty(self):
        """ public """
        return len(self) == 0

    def append(self, new_task: Task):
        """ Append new task """
        existing_task = self.find_already_added(new_task)
        if existing_task is None:
            self.task_list.append( new_task )
        else:
            existing_task.sum_stats(new_task)
            raise reapetedTask()

    def find_already_added(self, new_task) -> Task:
        """ Find already existed task on list """
        for task in self.task_list:
            if CompareString.is_similar(task.text, new_task.text, self.strictness):
                return task
        return None

    def sort(self) -> None:
        """ Sort task list """
        self.task_list = list(dict.fromkeys( self.task_list ))
        self.task_list = sorted(self.task_list)

    def clear(self) -> None:
        """ Clear task list """
        del self.task_list
        self.task_list = []

    def save(self, file_name, exam_num, file_head = 0):
        """ Save to file """
        self.sort()

        file = Exam.create_file(file_name, exam_num)
        file.write(file_head + "\n\n\n")
        file.write("\n\n".join( map(str,self.task_list) ))
        file.close()

    @staticmethod
    def create_file(file_name, exam_num):
        """ private """
        out_dir = f"{os.getcwd()}/data_files/out"

        try:
            os.mkdir(f"{out_dir}")
        except FileExistsError:
            pass

        return open(f"{out_dir}/{file_name}-{exam_num}.txt", "w", encoding="utf-8")
