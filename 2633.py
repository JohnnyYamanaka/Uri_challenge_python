"""
https://www.beecrowd.com.br/judge/pt/problems/view/2633
"""

while True:
    try:
        dict_carnes = {}
        dict_carnes_ordenado = {}
        lista_ordenada = []

        cases = int(input())

        for case in range(cases):
            carne, validade = map(str, input().split(' '))
            dict_carnes_ordenado[carne] = int(validade)

        dict_carnes_ordenado = {k: v for k, v in sorted(
            dict_carnes_ordenado.items(), key=lambda item: item[1])}
        
        print(' '.join(dict_carnes_ordenado))
            
    except EOFError:
        break
    