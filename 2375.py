'''
Sedex
https://www.urionlinejudge.com.br/judge/pt/problems/view/2375
'''

diametro_bola = int(input())
altura, largura, cumprimento = list(map(int, input().split()))

bool_alt = diametro_bola <= altura
bool_larg = diametro_bola <= largura
bool_cumprimento = diametro_bola <= cumprimento

if(bool_alt and bool_larg and bool_cumprimento):
    print('S')

else:
    print('N')
