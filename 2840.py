from math import floor

R, L = list(map(float, input().split(" ")))
pi = 3.1415

volume_necessario = (4 * pi * pow(R, 3) / 3)

qtd_baloes = floor(L / volume_necessario)

print(qtd_baloes)