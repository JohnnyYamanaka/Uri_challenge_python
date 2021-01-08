'''
As Abas de Péricles
https://www.urionlinejudge.com.br/judge/pt/problems/view/2061
'''

abas, acoes = list(map(int, input().split(' ')))

for acao in range(acoes):
    mov = str(input())
    if mov == 'fechou':
        abas += 1

    else:
        abas -= 1

print(abas)
