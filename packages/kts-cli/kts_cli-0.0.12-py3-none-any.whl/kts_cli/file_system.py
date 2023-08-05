import os
import shutil
import json


def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * level
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))


def check_existance(paths):
    """
    Checks necessity of clearing the folder.
    :param paths: list of directories
    :return: True if at least one directory exists, False otherwise
    """
    for path in paths:
        if os.path.isdir(path):
            return True
    return False

def clear_all():
    """
    Clears current folder.
    :return:
    """
    folder = './'
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(e)


def build_file_system(force=False):
    """
    Builds directory structure for correct running kts.
    :param force: True or False (without confirmation or not)
    :return:
    """
    paths = ['./input', './notebooks', './storage', './output', './submissions']

    if check_existance(paths):
        if force:
            clear_all()

        list_files('./')
        print('Do you want to clear existing kts file system? [y/N]')
        try:
            answer = str(input())
            if answer.lower() == 'y' or answer.lower() == 'yes':
                clear_all()
        except Exception as e:
            raise TypeError('Invalid answer')

    print('Do you want to build the file system? [y/N]')
    try:
        answer = str(input())
        if answer.lower() == 'y' or answer.lower() == 'yes':
            for path in paths:
                if not os.path.isdir(path):
                    os.makedirs(path)
    except Exception as e:
        raise TypeError('Invalid answer')

    if os.path.exists('./kts_config.py'):
        print("Config found. Overwrite? [y/N]")
        answer = str(input())
        if answer.lower() == 'y' or answer.lower() == 'yes':
            create_config()
    else:
        create_config()


DEFAULT_CONFIG = f"""\
# Cache mode defines resources used for caching:
# - disk         -- use only disk space, no RAM is used. Choose it if you don't have much RAM.
# - ram          -- use only RAM space. Best for kaggle kernels.
# - disk_and_ram -- use both. The fastest option. Best for local usage. Default. 
cache_mode = 'disk_and_ram'  # "disk", "disk_and_ram", "ram"

# Cache policy defines which types of files will be saved.
# - everything   -- cache everything including feature constructor calls. Default.
# - service      -- only service files are saved. No feature computation speedup. 
#                   Use if you're not lucky with your resources.
cache_policy = 'everything'  # "everything", "service"

# Full path of storage.
# DO NOT ERASE
storage_path = '{os.getcwd()}/storage/'

# Task goal: whether greater is better or not
GOAL = 'MAXIMIZE' # or 'MINIMIZE'
"""


def create_config():
    # json.dump({'storage_path': os.path.realpath('./storage') + '/'}, open('.kts', 'w'))
    with open('kts_config.py', 'w') as f:
        f.write(DEFAULT_CONFIG)
