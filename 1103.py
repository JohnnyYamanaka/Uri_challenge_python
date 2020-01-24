
while True:
    h1, m1, h2, m2 = list(map(int, input().split(" ")))
    if (h1 + m1 + h2 + m2) == 0:
        break
    min1 = (h1 * 60) + m1
    min2 = (h2 * 60) + m2
    if min2 < min1:
        min2 += 1440

    total = min2 - min1
    print(total)