num = float(input())

if num >= 0.0 and num <= 25.0:
    print('Intervalo [0,25]')

elif num > 25.00000 and num <= 50.0000000:
    print('Intervalo (25,50]')

elif num > 50.000000 and num <= 75.0000000:
    print('Intervalo (50,75]')

elif num > 75.000000 and num <= 100.0000000:
    print('Intervalo (75,100]')

else:
    print('Fora de intervalo')