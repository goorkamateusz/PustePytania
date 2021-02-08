import os
import PustePytania.Config as Config

class RenameFiles:
    """ Rename output files """

    @staticmethod
    def rename(exam_name: str):
        """ public static """
        dir_name = "data_files/out"
        exam_files = list(os.listdir(dir_name))

        def name_filter(name: str):
            return Config.EXAM_NAME not in name and os.path.isfile(f"{dir_name}/{name}")

        def sort_key(name: str):
            return int(name.replace("exam-", "").replace(".txt", ""))

        num_of_files_in_dir = len(exam_files)
        exam_files = list(filter(name_filter, exam_files))
        file_num = num_of_files_in_dir - len(exam_files) + 1
        exam_files.sort(key = sort_key, reverse=True)

        for exam_file in exam_files:
            os.rename(f"{dir_name}/{exam_file}", f"{dir_name}/{exam_name}-{file_num}.txt")
            file_num += 1

if __name__ == "__main__":
    RenameFiles.rename(Config.EXAM_NAME)
