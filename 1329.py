vezes_jogado = int(input())
mary_won = 0
john_won = 0
results = []

while vezes_jogado != 0:
    results = list(map(int, input().split(" ")))
    for itens in range(len(results)):
        if results[itens] == 0:
            mary_won += 1
        else:
            john_won += 1
    print("Mary won {} times and John won {} times".format(mary_won, john_won))
    mary_won = 0
    john_won = 0
    vezes_jogado = int(input())
