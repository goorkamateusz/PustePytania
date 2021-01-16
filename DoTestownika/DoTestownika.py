import os
import Config
from FilesGenerator import *

class DoTestownika:
    """ main class """

    @staticmethod
    def read_dir(dir_path = Config.INPUT_DIR):
        """ public """
        try:
            os.mkdir(Config.OUTPUT_DIR)
        except FileExistsError:
            pass

        for file in os.listdir(dir_path):
            file_path = dir_path+"/"+file
            if os.path.isfile(file_path):
                if ".txt" in file:
                    print(f"input file: {file}")
                    DoTestownika.prase_exam(file_path)

            elif os.path.isdir(file_path):
                DoTestownika.read_dir(file)

            else:
                pass

    @staticmethod
    def prase_exam(file_path):
        """ public """
        exam = FilesGenerator(file_path)
        exam.create_dir()
        exam.convert_and_save()

if __name__ == "__main__":
    DoTestownika.read_dir()
