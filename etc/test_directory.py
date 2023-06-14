import os

# get the current working directory
cur_path = os.getcwd()
print(cur_path)

# change the current working directory
os.chdir( "../")
new_path = os.getcwd()
print(new_path)

# get the list of all files and directories in the specified directory
fds_in_dir = os.listdir()
print(f"type : {type(fds_in_dir)}")
print(f"total: {len(fds_in_dir)}")
