import os

folder_path = './'

file_list = os.listdir(folder_path)
print(f"type : {type(file_list)}")
print(f"total: {len(file_list)}")
