while True:
    try:
        filho, filha = list(map(int, input().split(" ")))
        if filho + filha == 0:
            break

        total_filho = filho + filha
        print(total_filho)

    except EOFError:
        break