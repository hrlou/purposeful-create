# Hess Lewis
# 07/11/2023

import os
import subprocess
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

# DECLARE
git_process = subprocess.run(['git', 'rev-parse', '--short', 'HEAD'], stdout=subprocess.PIPE)
COMMIT_ID = str(git_process.stdout)
COMMIT_ID = COMMIT_ID[2:-3]
PROJECT_DIR = "."
COMMON_TEMPLATE_DIR = f'{PROJECT_DIR}/template_common'
CLIENT_TEMPLATE_DIR = f'{PROJECT_DIR}/template_client'
SERVER_TEMPLATE_DIR = f'{PROJECT_DIR}/template_server'
MMC_TEMPLATE_DIR = f'{PROJECT_DIR}/template_mmc'
BUILD_DIR = f'{PROJECT_DIR}/build/{COMMIT_ID}'
MMC_BUILD_DIR = f'{BUILD_DIR}/MultiMC'
CLIENT_BUILD_DIR = f'{BUILD_DIR}/dot_minecraft'
SERVER_BUILD_DIR = f'{BUILD_DIR}/server'

# START
print(f'Build version \'{COMMIT_ID}\'')

if not path.exists(f'{PROJECT_DIR}/build'):
    os.mkdir(f'{PROJECT_DIR}/build')

if path.exists(BUILD_DIR):
    print('Build already completed')
    exit(0)

os.mkdir(BUILD_DIR)

# generate .minecraft
print("Generating '.minecraft'")
merge_directories(CLIENT_BUILD_DIR, COMMON_TEMPLATE_DIR, CLIENT_TEMPLATE_DIR)
merge_directories(SERVER_BUILD_DIR, COMMON_TEMPLATE_DIR, SERVER_TEMPLATE_DIR)

# build multimc
print("Generating MultiMC directory")
shutil.copytree(MMC_TEMPLATE_DIR, MMC_BUILD_DIR)
shutil.copytree(CLIENT_BUILD_DIR, f'{MMC_BUILD_DIR}/.minecraft')

print("Zipping MultiMC")
shutil.make_archive(f'{PROJECT_DIR}/build/Purposeful_Create-MultiMC-{COMMIT_ID}', 'zip', MMC_BUILD_DIR)

print("Zipping Server")
shutil.make_archive(f'{PROJECT_DIR}/build/Purposeful_Create-server-{COMMIT_ID}', 'zip', SERVER_BUILD_DIR)
