'''
Corrida
https://www.urionlinejudge.com.br/judge/pt/problems/view/2516
'''

while True:
    try:

        s, v_a, v_b = list(map(float, input().split(' ')))

        if v_b >= v_a:
            print('impossivel')

        else:
            tempo = s / (v_a - v_b)
            print('%.2f' % tempo)

    except EOFError:
        break
