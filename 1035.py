int_number = list(map(int,input().split(" ")))

true = "Valores aceitos"
false = "Valores nao aceitos"

A, B, C, D = int_number[0], int_number[1], int_number[2], int_number[3]

C_is_positive = bool(C >0)
D_is_positive = bool(D >0)
A_is_even = bool((A % 2) == 0)

if(B > C and D > A and (C + D) > (A + B) and C_is_positive and D_is_positive and A_is_even):
    print(true)

else:
    print(false)