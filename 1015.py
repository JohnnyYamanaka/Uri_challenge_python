from math import sqrt

n1, n2 = list(map(float, input().split(" ")))
n3, n4 = list(map(float, input().split(" ")))

sub1 = n3-n1
sub2 = n4-n2


distancia = sqrt(pow(sub1, 2) + (pow(sub2, 2)))

print('%.4f' % distancia)