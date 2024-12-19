import os 

file_path = "downloading"

for i in os.listdir(file_path):
    os.remove(os.path.join(file_path, i))