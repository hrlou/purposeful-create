import shutil

def merge_directories(new_directory, source_dir1, source_dir2):
    if not os.path.exists(new_directory):
        os.makedirs(new_directory)

    if os.path.exists(source_dir1):
        for item in os.listdir(source_dir1):
            source_item = os.path.join(source_dir1, item)
            destination_item = os.path.join(new_directory, item)

            if os.path.isdir(source_item):
                merge_directories(destination_item, source_item, os.path.join(source_dir2, item))
            else:
                shutil.copy2(source_item, destination_item)

    if os.path.exists(source_dir2):
        for item in os.listdir(source_dir2):
            source_item = os.path.join(source_dir2, item)
            destination_item = os.path.join(new_directory, item)

            if os.path.isdir(source_item):
                merge_directories(destination_item, os.path.join(source_dir1, item), source_item)
            else:
                shutil.copy2(source_item, destination_item)

