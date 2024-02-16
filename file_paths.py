import os
def retrive_file_paths(number_of_files, root_dir):
    root_directory = root_dir
    folders = os.listdir(root_directory)
    file_paths_list = []
    count = 0
    for file in folders:
        file_path = os.path.join(root_directory, file)
        txt_files = os.listdir(file_path)
        for txt in txt_files:
            if txt.endswith('.txt') and count < number_of_files:
                count += 1
                file_paths_list.append(os.path.join(file_path, txt))
    return file_paths_list