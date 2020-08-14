"""
Leia 2 valores inteiros (A e B). Após, o programa deve mostrar uma mensagem "Sao Multiplos"
ou "Nao sao Multiplos", indicando se os valores lidos são múltiplos entre si.
"""

a, b = list(map(int, input().split(" ")))

a_mult_b = bool((a % b) == 0)
b_mult_a = bool((b % a) == 0)


if a_mult_b or b_mult_a:
    print("Sao Multiplos")

else:
    print("Nao sao Multiplos")
