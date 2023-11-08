import subprocess

git_process = subprocess.run(['git', 'rev-parse', '--short', 'HEAD'], stdout=subprocess.PIPE)
COMMIT_ID = str(git_process.stdout)
COMMIT_ID = COMMIT_ID[2:-3]

# general
PROJECT_DIR = "."
MINECRAFT_VERSION = "1.19.2"
FABRIC_VERSION = "0.14.24"
# templates
TEMPLATES_DIR = f'{PROJECT_DIR}/templates'
CLIENT_TEMPLATE_DIR = f'{TEMPLATES_DIR}/client'
COMMON_TEMPLATE_DIR = f'{TEMPLATES_DIR}/common'
SERVER_TEMPLATE_DIR = f'{TEMPLATES_DIR}/server'
MMC_TEMPLATE_DIR = f'{TEMPLATES_DIR}/mmc'
# build
BUILD_DIR = f'{PROJECT_DIR}/build'
BUILD_MANIFEST = f'{BUILD_DIR}/manifest.txt'
CLIENT_BUILD_DIR = f'{BUILD_DIR}/.minecraft'
SERVER_BUILD_DIR = f'{BUILD_DIR}/server'
MMC_BUILD_DIR = f'{BUILD_DIR}/mmc'

SERVER_TARGET = f'{PROJECT_DIR}/build/purposeful-create-server-{COMMIT_ID}'
MMC_TARGET = f'{PROJECT_DIR}/build/purposeful-create-mmc-{COMMIT_ID}'
