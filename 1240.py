test_cases = int(input())

for case in range(test_cases):
    a, b = list(map(str, input().split(' ')))

    b_len = - len(b)
    a_last_char = a[b_len:]

    if b in a_last_char:
        print('encaixa')

    else:
        print('nao encaixa')
