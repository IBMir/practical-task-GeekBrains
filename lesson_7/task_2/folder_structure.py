import os


def checking_and_creating(pat):
    if not os.path.exists(pat):
        os.mkdir(pat)


def structure_from_the_list(root, content):
    for r in range(len(content)):
        if type(content[r]) != list and '.' not in str(content[r]):
            route = os.path.join(root, str(content[r]))
            checking_and_creating(route)
        elif type(content[r]) != list and '.' in str(content[r]):
            with open(content[r], 'w'):
                pass
            route = os.path.join(root, str(content[r]))
            os.replace(content[r], route)
        else:
            route = os.path.join(root, content[r - 1])
            structure_from_the_list(route, content[r])


def folder_structure(path, project, folders):
    path_project = os.path.join(path, project)
    checking_and_creating(path_project)
    structure_from_the_list(path_project, folders)
