def saddle_point(matrix):
    point = False
    x = 0
    y = 0
    value = 0
    saddle = None
    test = 0
    for i in range(len(matrix)):
        value = min(matrix[i])
        x = matrix[i].index(value)
        if matrix[i].count(value) > 1:
            x = 0
            continue
        saddle = value
        y = i
        for j in range(len(matrix)):
            test = matrix[j][x]
            if j == i:
                continue
            if matrix[j][x] >= saddle:
                saddle = None
                break
        if saddle is not None:
            final = (y, x)
            return final
    if saddle is None:
        return point


print(saddle_point([[1, 2, 3, 0, 1, 1], [4, 3, 2, 1, 1, 2], [4, 3, 2, 0, 1, 1], [0, 0, 0, 0, 0, 1]]))
