""" Klasa testu """
from Task import *
from Counter import *
from CompareString import *

class Exam:
    """ Klasa testu """
    strictness = 4

    def __init__(self):
        self.task_list = []

    def __len__(self):
        return len(self.task_list)

    def append(self, new_task: Task):
        """ Append new task """
        existing_task = self.find_already_added(new_task)
        if existing_task is None:
            self.task_list.append( new_task )
        else:
            existing_task.sum_stats(new_task)

    def find_already_added(self, new_task) -> Task:
        """ Find already existed task on list """
        for task in self.task_list:
            if CompareString.is_similar(task.text, new_task.text, self.strictness):
                return task
        return None

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