import os
import Config
from TaskPraser import *

class FilesGenerator:
    """ Exam file """
    file_cnt = 0

    def __init__(self, file_path):
        self.file_path = file_path
        self.dir_path = None
        self.file = None

    def create_dir(self):
        """ public """
        self.dir_path = f"{Config.OUTPUT_DIR}/{os.path.basename(self.file_path)}"
        try:
            os.mkdir(self.dir_path)
        except FileExistsError:
            pass

    def convert_and_save(self):
        """ public """
        self.file = open(self.file_path, "r")

        self._skip_head_file()
        self._split_file_to_tasks_file()

    def _skip_head_file(self):
        """ private """
        newline_cnt = 0
        for line in self.file.readline():
            if FilesGenerator.is_empty_line(line):
                newline_cnt += 1
                if newline_cnt > 1:
                    break
            else:
                newline_cnt = 0

    def _split_file_to_tasks_file(self):
        """ private """
        while self._prase_and_save_task():
            pass

    def _prase_and_save_task(self) -> bool:
        """ private """
        file_path = f"{self.dir_path}/{FilesGenerator.file_cnt}"

        if os.path.isfile(file_path):
            raise FileExistsError()

        file_out = open(file_path, "w")
        file_out.write(TaskPraser.prase(self.file))
        file_out.close()

    def _read_task(self) -> str:
        """ private """
        task_text = ""
        for line in self.file.readline():
            if FilesGenerator.is_empty_line(line):
                break
            task_text += line
        return task_text

    @staticmethod
    def is_empty_line(line) -> bool:
        """ private """
        return line.strip() == ""
