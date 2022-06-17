from folder_structure import folder_structure
path = r'C:\PyCharm projects\practical_task_GeekBrains\lesson_7\task_2'
project = 'my_project'
folders = \
    ['settings', ['__init__.py',
                  'dev.py',
                  'prod.py'],
     'mainapp', ['__init__.py',
                 'models.py',
                 'views.py',
                 'templates', ['mainapp', ['base.html',
                                           'index.html']]],
     'adminapp', ['__init__.py',
                 'models.py',
                 'views.py',
                 'templates', ['authapp', ['base.html',
                                           'index.html']]]]
folder_structure(path, project, folders)