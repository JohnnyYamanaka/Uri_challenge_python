from string import ascii_lowercase

letter = list(ascii_lowercase)
numero = 97

for cases in range(26):
    print('{} e {}'.format(numero, letter[cases]))
    numero += 1
