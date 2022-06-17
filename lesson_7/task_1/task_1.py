import os


def checking_and_creating(pat):
    if not os.path.exists(pat):
         os.mkdir(pat)

path = r'C:\PyCharm projects\practical_task_GeekBrains\lesson_7\task_1'
project = 'my_project'
folders = \
    ['settings',
     'mainapp',
     'adminapp',
     'authapp']

path_project = os.path.join(path, project)
checking_and_creating(path_project)
for i in folders:
    path_folders = os.path.join(path_project, i)
    checking_and_creating(path_folders)