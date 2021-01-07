'''
Tabuada
https://www.urionlinejudge.com.br/judge/pt/problems/view/1078
'''

case = int(input())

for number in range(1, 11, 1):
    print('{} x {} = {}'.format(number, case, case * number))
