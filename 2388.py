qtd_registro = int(input())
km_total1 = 0

for registro in range(qtd_registro):
    temp, vel = list(map(int, input().split(" ")))
    km_total = temp * vel
    km_total1 = km_total1 + km_total

print(km_total1)