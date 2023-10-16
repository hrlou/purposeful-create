PROJECT_DIR = "."
COMMON_TEMPLATE_DIR = f'{PROJECT_DIR}/template_common'
CLIENT_TEMPLATE_DIR = f'{PROJECT_DIR}/template_client'
SERVER_TEMPLATE_DIR = f'{PROJECT_DIR}/template_server'
BUILD_DIR = f'{PROJECT_DIR}/build'
MMC_BUILD = f'{BUILD_DIR}/mmc'

import os
from os import path
import shutil
from zipfile import ZipFile

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

# start
if path.exists(BUILD_DIR):
    print(f'Please delete {BUILD_DIR}')
    exit(0)

os.mkdir(BUILD_DIR)
# generate .minecraft
client = f'{BUILD_DIR}/client'
merge_directories(client, COMMON_TEMPLATE_DIR, CLIENT_TEMPLATE_DIR)
server = f'{BUILD_DIR}/server'
merge_directories(server, COMMON_TEMPLATE_DIR, SERVER_TEMPLATE_DIR)

mmc = MMC_BUILD
os.mkdir(MMC_BUILD)
shutil.copy(f'{PROJECT_DIR}/mmc-pack.json', MMC_BUILD)
shutil.copy(f'{PROJECT_DIR}/instance.cfg', MMC_BUILD)
merge_directories(f'{MMC_BUILD}/.minecraft', COMMON_TEMPLATE_DIR, CLIENT_TEMPLATE_DIR)
shutil.make_archive(f'{BUILD_DIR}/Purposeful_Create', 'zip', MMC_BUILD)
