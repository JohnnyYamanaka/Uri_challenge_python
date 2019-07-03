horas = int(input())
vel_med = int(input())
consumo_vei = 12

combustivel_necessario = (horas * vel_med) / consumo_vei

print("%.3f" % combustivel_necessario)