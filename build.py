# Hess Lewis
# 07/11/2023

import common
import jinja2
import os
import shutil
import subprocess

from os import path
from zipfile import ZipFile
from common import merge_directories

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
