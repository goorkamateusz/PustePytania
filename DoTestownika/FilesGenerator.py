import os
import Config
from TaskParser import TaskParser

class FilesGenerator:
    """ Exam file """
    file_cnt = 0

    def __init__(self, input_file_path):
        self.input_file_path = input_file_path
        self.dir_path = None
        self.file = None

    def create_dir(self):
        """ public """
        self.dir_path = f"{Config.OUTPUT_DIR}/{os.path.basename(self.input_file_path)}"
        try:
            os.mkdir(self.dir_path)
        except FileExistsError:
            pass

    def convert_and_save(self):
        """ public """
        self.file = iter(open(self.input_file_path, "r", encoding="utf-8").readlines())

        self._skip_head_file()
        self._split_file_to_tasks_file()

    def _skip_head_file(self):
        """ private """
        newline_cnt = 0
        for line in self.file:
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
        task_text = ""
        for line in self.file:
            if FilesGenerator.is_empty_line(line):
                if task_text != "":
                    self._save_task_file(TaskParser.parser(task_text))
                    return True
                else:
                    continue
            else:
                task_text += line

        if task_text != "":
            self._save_task_file(TaskParser.parser(task_text))
        return False

    def _save_task_file(self, outfile_text: str):
        file_path = f"{self.dir_path}/{FilesGenerator.file_cnt}.txt"

        if os.path.isfile(file_path):
            raise FileExistsError()

        file_out = open(file_path, "w", encoding="utf-8")
        file_out.write(outfile_text)
        file_out.close()

        FilesGenerator.file_cnt += 1

    @staticmethod
    def is_empty_line(line) -> bool:
        """ private """
        return line.strip() == ""
