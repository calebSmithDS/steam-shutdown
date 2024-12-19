import os 
import time 

def monitor(path):
    x = 0
    for i in os.listdir(path):
        path_1 =os.path.join(path, i)
        if os.path.isdir(path_1) == True:
            x += monitor(path_1)
        else:
            x += os.path.getsize(path_1)
    return x


folder_path = "downloading"
total_dir_size = 0


while True:
    total_dir_size += monitor(folder_path)
    print(total_dir_size)
    if total_dir_size == 0:
        break
    time.sleep(10)
    print("shutdown")
# os.system("shutdown /s /t 1")

