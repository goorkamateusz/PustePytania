import os
import Config

class ExamFile:
    """ Exam file """

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

    def convert(self):
        """ public """
        self.file = open(self.file_path, "r")

        self._skip_head_file()
        self._split_file_to_tasks()

    def _skip_head_file(self):
        """ private """
        newline_cnt = 0
        for line in self.file.readline():
            if line.strip() == "":
                newline_cnt += 1
                if newline_cnt > 1:
                    break
            else:
                newline_cnt = 0

    def _split_file_to_tasks(self):
        """ private """
        raise NotImplementedError()