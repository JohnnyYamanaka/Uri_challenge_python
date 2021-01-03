'''
Quanta Mandioca?
https://www.urionlinejudge.com.br/judge/pt/problems/view/2936
'''

consumo_curupira = int(input()) * 300
consumo_boitata = int(input()) * 1500
consumo_boto = int(input()) * 600
consumo_mapiguari = int(input()) * 1000
consumo_iara = int(input()) * 150
CONSUMO_CHICA = 225

consumo_total = sum((consumo_curupira, consumo_boitata, consumo_boto, consumo_mapiguari, consumo_iara, CONSUMO_CHICA), 0)
print(consumo_total)
