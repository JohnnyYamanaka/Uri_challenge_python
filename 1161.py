from math import factorial

while True:
    try:
        a, b = list(map(int, input().split()))
        S = factorial(a) + factorial(b)
        print(S)

    except EOFError:
        break

