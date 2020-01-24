test_case = int(input())
lista = []
lista2 = []

for case in range(test_case):
    variavel = int(input())
    lista.append(variavel)

lista2 = list(set(lista))
lista2.sort()

for itens in range(len(lista2)):
    results = lista.count(lista2[itens])
    print("{} aparece {} vez(es)".format(lista2[itens], results))

