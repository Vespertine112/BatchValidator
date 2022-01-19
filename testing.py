import os
def find_all_directories(start_directory: str):
    all_directories = []
    directory_queue = [os.path.normpath(os.path.join(os.getcwd(),start_directory))]
    while (len(directory_queue) > 0):
        current_dir = directory_queue.pop()
        all_directories.append(current_dir)
        for file in os.listdir(current_dir):
            if (file[0] == '.'):
              continue
            full_name = os.path.join(current_dir, file)
            if (os.path.isdir(full_name)):
                directory_queue.append(full_name)
    return all_directories


for directory in find_all_directories('test_failure.css'):
  print(directory)