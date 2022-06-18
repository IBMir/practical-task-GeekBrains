import shutil
import os


def collect_templates(project, collection_folder):
    for dirpath, dirnames, filenames in os.walk(project):
        if collection_folder in dirnames:
            if not os.path.exists(f'{project}\\{collection_folder}'):
                os.mkdir(f'{project}\\{collection_folder}')
            for i in os.listdir(f'{dirpath}\\{collection_folder}'):
                shutil.move(f'{dirpath}\\{collection_folder}\\{i}', f'{project}\\{collection_folder}')
            os.rmdir(f'{dirpath}\\{collection_folder}')


collect_templates('my_project', 'templates')
