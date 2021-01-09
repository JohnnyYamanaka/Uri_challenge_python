'''
2417
https://www.urionlinejudge.com.br/judge/pt/problems/view/2417
'''

c_vitoria, c_empate, c_saldo_gol, \
f_vitoria, f_empate, f_saldo_gol = list(map(int, input().split()))

c_pontos = (c_vitoria * 3) + c_empate
f_pontos = (f_vitoria * 3) + f_empate

if c_pontos == f_pontos:
    if c_saldo_gol == f_saldo_gol:
        print('=')

    elif c_saldo_gol < f_saldo_gol:
        print('F')

    else:
        print('C')

elif c_pontos < f_pontos:
    print('F')

else:
    print('C')
