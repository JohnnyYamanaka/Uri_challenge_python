while True:
    try:
        vel, tem = list(map(int, input().split(" ")))
        valor = vel * tem
        valor_final = valor * 2
        print(valor_final)

    except EOFError:
        break