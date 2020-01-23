dias = int(input())

ano = dias // 365
mes = (dias % 365) // 30
dia = (dias % 365) % 30

print(ano, 'ano(s)')
print(mes, 'mes(es)')
print(dia, 'dia(s)')