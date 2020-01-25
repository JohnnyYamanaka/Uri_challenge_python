from math import sqrt


A, B, C = list(map(float, input().split(' ')))

delta = (pow(B, 2)) - 4 * A * C
if delta <= 0.0 or A == 0.0:
    print('Impossivel calcular')

else:
    raiz_delta = sqrt(delta)
    x1 = (-B + raiz_delta) / (2 * A)
    x2 = (-B - raiz_delta) / (2 * A)

    print('R1 = %.5f' % x1)
    print('R2 = %.5f' % x2)
