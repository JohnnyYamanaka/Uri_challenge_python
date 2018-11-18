test_case = int(input())

def supriment_over (food):
    days_until_food_over = 0
    while food > 1:
        food /= 2
        days_until_food_over += 1
    print(days_until_food_over, "dias")

for days in range(0, test_case):

    supriment_over(int(input()))



