'''
Identificando o Chá
https://www.urionlinejudge.com.br/judge/pt/problems/view/2006
'''

correct_tea = int(input())
list_of_guess = list(map(int, input().split(' ')))

counter = list_of_guess.count(correct_tea)

print(counter)
