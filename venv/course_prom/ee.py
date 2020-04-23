import sys


def clean_list(list_to_clean):
    result = []
    for i in range(len(list_to_clean)):
        list_tmp = list_to_clean[:i]
        for n in range(len(list_tmp)):
            n = n + 1
            if list_to_clean[i] == list_tmp[n - 1] and type(list_tmp[n - 1]) == type(list_to_clean[i]):
                list_to_clean[i] = ""
        result.append(list_to_clean[i])
    for i in result:
        if i == "":
            while result.count("") > 0:
                result.remove(i)
    return result


print(clean_list(sys.argv[1:]))
