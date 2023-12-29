"""
https://www.beecrowd.com.br/judge/pt/problems/view/1259

"""

impares = []
pares = []

qtd_linhas = int(input())

for case in range(qtd_linhas):
    entrada = int(input())

    if entrada % 2 == 0:
        pares.append(entrada)

    else:
        impares.append(entrada)

pares.sort()
impares.sort(reverse=True)

lista_num = pares + impares
for num in lista_num:
    print(num)
