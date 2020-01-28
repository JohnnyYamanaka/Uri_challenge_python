case = int(input())
counter = 0
new_numb = case + 1

while counter < 6:
    if new_numb % 2 != 0:
        print(new_numb)
        counter += 1

    new_numb += 1

