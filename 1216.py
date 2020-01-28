counter = 0
total_dist = 0

while True:
    try:
        nome = str(input())
        dist = float(input())

        total_dist += dist
        counter += 1

    except EOFError:
        break

avg = total_dist / counter
print('%.1f' % avg)