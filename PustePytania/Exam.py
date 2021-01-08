""" Klasa testu """
from Task import *
from Counter import *
from CompareString import *
from ImageToText import image_to_text


class Exam:
    """ Klasa testu """
    strictness = 4

    def __init__(self):
        self.task_list = []
        self.reapeted_cnt = 0

    def __len__(self):
        return len(self.task_list)

    def append(self, new_task: Task):
        """ Append new task """
        existing_task = self.find_already_added(new_task)
        if existing_task is None:
            self.task_list.append( new_task )
        else:
            existing_task.sum_stats(new_task)
            # todo counter w nie ladnym miejscu
            self.reapeted_cnt += 1

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

        file = open(f"{file_name}-{exam_num}.txt", "w", encoding="utf-8")
        file.write( file_head )

        file.write( "\n\n".join( map(str,self.task_list) ) )
        file.close()

    def add_task(self, discord_msg, image_url) -> Counter:
        task = Task()
        cnt = Counter()

        task.react(discord_msg.reactions)

        if not task.skip():
            task.set_text( image_to_text(image_url) )
            self.append( task )

            cnt.screen = 1
            print( cnt.msg, "\n", cnt.screen, " ", task )
        else:
            cnt.skip = 1

        if task.end_of_exam():
            self.save("exam", cnt.exam, file_head)
            self.clear()

            cnt.exam = 1
            cnt.reapeted += self.reapeted_cnt
            print( f"\n--- Zapisan {cnt.exam} test ---\n" )