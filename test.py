x, y, sum = 12, 1, 0
while y <= x:
    for i in range(y, 12, 3):
        if (i % 2) == 0:
            sum += 1
        else:
            sum += 2
    y += 1
