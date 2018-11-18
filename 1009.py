vendedor = input()
salario_fixo = float(input())
venda = float(input())

comicao = venda * 0.15
TOTAL = salario_fixo + comicao

print("TOTAL = R$ %.2f" % TOTAL)