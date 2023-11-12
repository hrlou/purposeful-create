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
    print("Finished building client directory")

def build_server():
    print("Building server directory")
    if path.exists(SERVER_BUILD_DIR):
        print(f'Target already built at: \'{SERVER_BUILD_DIR}\'')
    else: 
        print("Merging server only and common files")
        merge_directories(SERVER_BUILD_DIR, COMMON_TEMPLATE_DIR, SERVER_TEMPLATE_DIR)
        print("Finished building server directory")

def build_server_zip():
    print("Zipping server directory")
    if path.exists(f'{SERVER_TARGET}.zip'):
        print(f'Target already built at: \'{SERVER_TARGET}\'')
        return
    shutil.make_archive(SERVER_TARGET, 'zip', SERVER_BUILD_DIR)
    print("Finished zipping server directory")

def build_multimc():
    print("Generating MultiMC directory")
    if path.exists(MMC_TARGET):
        print(f'Target already zipped at: \'{MMC_TARGET}\'')
    else:
        shutil.copytree(MMC_TEMPLATE_DIR, MMC_BUILD_DIR)
        shutil.copytree(CLIENT_BUILD_DIR, f'{MMC_BUILD_DIR}/.minecraft')

def build_multimc_zip():
    print("Zipping MultiMC")
    if path.exists(f'{MMC_TARGET}.zip'):
        print(f'Target already zipped at: \'{MMC_TARGET}\'')
    else:
        shutil.make_archive(MMC_TARGET, 'zip', MMC_BUILD_DIR)
        print("Finished zipping MultiMC directory")

def get_manifest():
    if path.exists(BUILD_MANIFEST):
        manifest = open(BUILD_MANIFEST, 'r')
        last_commit = manifest.readline()
        return last_commit
    return False

def build_manifest():
    print("Creating build manifest")
    manifest = open(BUILD_MANIFEST, 'w')
    manifest.write(COMMIT_ID)

def clean():
    print("Cleaning build directory")
    shutil.rmtree(BUILD_DIR)
    print("Finished cleaning build directory")

do_clean = False
do_build_client = False
do_build_server = False
do_zip = False

print(f'Building with commit: \'{COMMIT_ID}\'')

if len(argv) <= 1:
    do_build_client = True
    do_build_server = True
else:
    if argv[1] == "all":
        do_build_client = True
        do_build_server = True
        do_zip = True
    elif argv[1] == "client":
        do_build_client = True
    elif argv[1] == "server":
        do_build_server = True
    elif argv[1] == "clean":
        do_clean = True

if path.exists(BUILD_DIR):
    manifest = get_manifest()
    if manifest == False:
        print("No previous manifest found")
        build_manifest()
    else:
        if do_clean:
            print("Ignoring previous manifest: cleaning")
        else:
            print(f'Previous build manifest exists: \'{manifest}\'')
            if manifest == COMMIT_ID:
                print("Manifest same as current build: exitiing")
                exit(0)
            do_clean = query_yes_no("Do you wish to clean previous build?")
else:
    print("Build path not found: creating one")
    mkdir(BUILD_DIR)

if do_clean:
    clean()
if do_build_client:
    build_client()
    build_multimc()
    if do_zip:
        build_multimc_zip()
if do_build_server:
    build_server()