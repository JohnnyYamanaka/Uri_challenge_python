'''
2381
https://www.urionlinejudge.com.br/judge/pt/problems/view/2381
'''

cases, sorted_number = list(map(int, input().split()))
students = []

for case in range(cases):
    students.append(input())

sorted_number -= 1
students.sort()
print(students[sorted_number])
