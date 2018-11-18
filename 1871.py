number = 0
while True:
    number = input().split(" ")
    sum = int(number[0]) + int(number[1])
    sum1 = list(map(int, str(sum).strip()))

    while 0 in sum1:
        if 0 in sum1:
            sum1.remove(0)
        else:
            pass
    if number == ['0', '0']:
       break

    sum1 = ''.join(str(e) for e in sum1)
    print(int(sum1))

