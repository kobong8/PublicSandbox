import os


file_path = "./folder_name/"

if os.path.isdir(file_path):
    pass
else:
    os.mkdir(file_path)
