import os
from tqdm import tqdm
import time

os.system('cls')

def preload_file_count(directory):
    print("Preloading directories and files..")
    total_items = 0
    for _, dirs, files in os.walk(directory):
        total_items += len(dirs) + len(files)
    return total_items

def search_file_with_progress(directory, target_fn):
    total_items = preload_file_count(directory)
    with tqdm(total=total_items, desc="Searching", unit="item") as pbar:
        result = search_file(directory, target_fn, pbar)
    return result

def search_file(directory, target_fn, pbar):
    try:
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)

            pbar.update(1)  

            if os.path.isfile(item_path) and item == target_fn:
                return item_path
            elif os.path.isdir(item_path):
                result = search_file(item_path, target_fn, pbar)
                if result:
                    return result
    except PermissionError:
        
        pass
    return None


directory_to_search = r"C:\Windows"  
target_file = "img0_3840x2160.jpg"  

start_time = time.perf_counter()
result = search_file_with_progress(directory_to_search, target_file)
end_time = time.perf_counter()

if result:
    print(f"\nFile found: {result}")
else:
    print("\nFile was not found")

print(f"Time elapsed: {end_time - start_time:.6f} seconds")
