# Hess Lewis
# 07/11/2023

from common import *
from config import *

# import jinja2
from os import path, mkdir
from sys import argv
import shutil

def build_client():
    print("Building '.minecraft' client directory")
    if path.exists(CLIENT_BUILD_DIR):
        print(f'Target already built at: \'{CLIENT_BUILD_DIR}\'')
        return
    print("Merging client only and common files")
    merge_directories(CLIENT_BUILD_DIR, COMMON_TEMPLATE_DIR, CLIENT_TEMPLATE_DIR)
    print("Finished building client directory\n")

def build_server():
    print("Building server directory")
    if path.exists(SERVER_BUILD_DIR):
        print(f'Target already built at: \'{SERVER_BUILD_DIR}\'\n')
    else: 
        print("Merging server only and common files")
        merge_directories(SERVER_BUILD_DIR, COMMON_TEMPLATE_DIR, SERVER_TEMPLATE_DIR)
        print("Finished building server directory")

    print("Zipping server directory")
    if path.exists(f'{SERVER_TARGET}.zip'):
        print(f'Target already built at: \'{SERVER_TARGET}\'\n')
        return
    shutil.make_archive(SERVER_TARGET, 'zip', SERVER_BUILD_DIR)
    print("Finished zipping server directory\n")

def build_multimc():
    print("Generating MultiMC directory")
    if path.exists(MMC_TARGET):
        print(f'Target already zipped at: \'{MMC_TARGET}\'\n')
    else:
        shutil.copytree(MMC_TEMPLATE_DIR, MMC_BUILD_DIR)
        shutil.copytree(CLIENT_BUILD_DIR, f'{MMC_BUILD_DIR}/.minecraft')

    print("Zipping MultiMC")
    if path.exists(f'{MMC_TARGET}.zip'):
        print(f'Target already zipped at: \'{MMC_TARGET}\'')
    else:
        shutil.make_archive(MMC_TARGET, 'zip', MMC_BUILD_DIR)
        print("Finished zipping MultiMC directory\n")

def build_manifest():
    if path.exists(BUILD_MANIFEST):
        print("Previous build manifest exists")
        manifest = open(BUILD_MANIFEST, 'r')
        last_commit = manifest.readline()
        print(last_commit)
    else: 
        print("Creating build manifest")
        manifest = open(BUILD_MANIFEST, 'w')
        manifest.write(COMMIT_ID)

print(f'Starting build')
print(f'Building with commit: \'{COMMIT_ID}\'\n')

if not path.exists(BUILD_DIR):
    print("Build path not found: creating one")
    mkdir(BUILD_DIR)

build_manifest()
if len(argv) <= 1:
    build_server()
    build_client()
    build_multimc()
if argv[1] == "client":
    build_client()
    build_multimc()
elif argv[1] == "server":
    build_server()
else:
    print("Huh?")

exit(0)


