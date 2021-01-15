import os
import Config
from FilesGenerator import *

class DoTestownika:
    """ main class """

    @staticmethod
    def read_dir(dir_path = Config.OUTPUT_DIR):
        """ public """
        for file in os.listdir(dir_path):
            if os.path.isfile(file):
                if ".txt" in file:
                    DoTestownika.prase_exam(file)

            elif os.path.isdir(file):
                DoTestownika.read_dir(file)

            else:
                pass

    @staticmethod
    def prase_exam(file_path):
        """ public """
        exam = FilesGenerator(file_path)
        exam.create_dir()
        exam.convert_and_save()
