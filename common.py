import os
import sys
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

def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
            It must be "yes" (the default), "no" or None (meaning
            an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True, "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == "":
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' " "(or 'y' or 'n').\n")
