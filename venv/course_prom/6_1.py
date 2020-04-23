def count_holes(n):
    holes = {(1, 2, 3, 5, 7): 0, (0, 4, 6, 9): 1, 8: 2}
    if isinstance(n, float):
        return "ERROR"
    p = int(n)
    if p < 0:
        p *= -1
    if not isinstance(p, int):
        return "ERROR"
    p = str(p)
    holes_num = 0
    for i in range(len(p)):
        for j in holes:
            if isinstance(j, tuple):
                if int(p[i]) in j:
                    holes_num += holes[j]
            elif int(p[i]) == j:
                holes_num += holes[j]
    return holes_num


print(count_holes('888888888888888888888.0'))
