'''
Tri-du
https://www.urionlinejudge.com.br/judge/pt/problems/view/1933
'''

first_card, second_card = list(map(int, input().split(' ')))
card_in_hands = []

if first_card == second_card:
    third_card = first_card
    print(third_card)

else:
    card_in_hands.extend([first_card, second_card])
    card_in_hands.sort(reverse=False)
    print(card_in_hands[1])
