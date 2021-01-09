'''
2376 - Copa do Mundo
https://www.urionlinejudge.com.br/judge/pt/problems/view/2376
'''

teams = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
        'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']


quarter_final = []
semi_final = []
final = []

for match in range(0, 16, 2):
    first_team_goal, second_team_goal = list(map(int, input().split()))
    if first_team_goal > second_team_goal:
        quarter_final.append(teams[match])

    else:
        quarter_final.append(teams[match + 1])


for match in range(0, 8, 2):
    first_team_goal, second_team_goal = list(map(int, input().split()))
    if first_team_goal > second_team_goal:
        semi_final.append(quarter_final[match])

    else:
        semi_final.append(quarter_final[match + 1])


for match in range(0, 4, 2):
    first_team_goal, second_team_goal = list(map(int, input().split()))

    if first_team_goal > second_team_goal:
        final.append(semi_final[match])

    else:
        final.append(semi_final[match + 1])


first_team_goal, second_team_goal = list(map(int, input().split()))
if first_team_goal > second_team_goal:
    print(final[0])

else:
    print(final[1])
