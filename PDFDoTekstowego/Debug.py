import os

debug_dir_path = "data_files/pdf_to_text_debug"

def save_debug_file(file_path: str, text: str):
    """ private """
    create_debug_dir()
    file_name = file_path.replace('/', '_').replace(".", "_")
    with open(f"{debug_dir_path}/{file_name}.txt", "w") as file:
        file.write(text)

def create_debug_dir():
    """ private """
    try:
        os.mkdir(debug_dir_path)
    except FileExistsError:
        pass
