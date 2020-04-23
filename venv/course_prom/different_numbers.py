def counter(x, y):
    count = 0
    tmpx = []
    tmpy = []
    for element in str(x):
        tmpx.append(element)
    for element in str(y):
        tmpy.append(element)
    for element in tmpy:
        if tmpy.count(element) > 1:
            tmpy.remove(element)
    for num in tmpy:
        for i in tmpx:
            if int(num) == int(i):
                count = count + 1
                break
    return count


print(counter(123123, 12223))
