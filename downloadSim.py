import time 
import os 

folder_path = "downloading"

os.makedirs(folder_path, exist_ok=True)

for i in range(1, 6):
    file_name = os.path.join(folder_path, f"file_{i}.tmp")
    print(file_name)
    # context manager "with"
    with open(file_name, "w") as f:
        f.write('data' * (i + 1))
    time.sleep(2)
