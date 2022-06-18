from folder_structure import folder_structure
import yaml

path = r'C:\PyCharm_poyects\practical_task_GeekBrains\lesson_7\task_2'  # Укажите свой путь
project = 'my_project'
with open('config.yaml') as f:
    folders = yaml.full_load(f)

folder_structure(path, project, folders)

# Функция folder_structure() принимает три параметра:
#   path - путь к начальной папке где будет создана струкрура проекта (папок/файлов)
#   project -  название проекта (корневой папки)
#   path - струкру проекта в виде вложенных спиков (list)
# Не работает если в имени папки имеется '.'(точка)
