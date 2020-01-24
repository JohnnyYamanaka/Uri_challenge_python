while True:
    try:
        A, B, C = list(map(int, input().split(' ')))

        if (A != B) & (A != C):
            print('A')

        elif (B != A) & (B != C):
            print('B')

        elif (C != A) & (C != B):
            print('C')

        else:
            print('*')

    except EOFError:
        break
