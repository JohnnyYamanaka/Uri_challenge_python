"""
Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.
I=1 J=7
I=1 J=6
I=1 J=5
I=3 J=9
I=3 J=8
I=3 J=7

...
I=9 J=15
I=9 J=14
I=9 J=13
"""
from math import ceil

I = 1
J = 7
counter = 1

while I <= 9:
    print('I={} J={}'.format(I, J))
    if counter < 3:
        J -= 1
        counter += 1

    else:
        J += 4
        I += 2
        counter = 1
        pass
