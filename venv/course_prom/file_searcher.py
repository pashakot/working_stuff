def file_search(folder, filename):
    path_list = []
    make_path_list(folder, "", path_list)
    res = 'False'
    for i in path_list:
        if filename in i[len(i)-len(filename):]:
            res = i
    return res


def make_path_list(folder, root, path_list):
    path = str(root)
    path = path + str(folder[0]) + "/"
    if len(folder) < 2:
        path_list.append(path)
    else:
        for i in range(1, len(folder)):
            if isinstance(folder[i],list):
                make_path_list(folder[i], path, path_list)
            else:
                path_list.append(path+str(folder[i]))


