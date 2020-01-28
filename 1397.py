while True:
    A_points = 0
    B_points = 0
    test_case = int(input())
    if test_case == 0:
        break

    for game in range(test_case):
        A, B = list(map(int, input().split(" ")))
        if A > B:
            A_points += 1

        elif A < B:
            B_points += 1

    print('{} {}'.format(A_points, B_points))
