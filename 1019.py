segundos = int(input())

hora = segundos // 3600
minutos = (segundos - (hora * 3600)) // 60
seg = segundos % 60

print('{}:{}:{}'.format(hora, minutos, seg))