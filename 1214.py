test_case = int(input())

def count_n_calulate_average():
    len_student = -1
    count = 0

    for student in range(qty_student + 1):
        student_grade = [line[student]]
        len_student += 1

    len_student_list = len_student

    excluded_value = line[0]
    sum_grade = sum(line) - excluded_value
    average = sum_grade / len_student_list

    for iten in range(len_student_list):
        if line[iten+1] > average:
            count += 1

    student_above_average = (count / len_student_list) * 100
    print("%.3f%%" % student_above_average)


for qty_test in range(test_case):
    line = list(map(int, input().split()))
    qty_student = line[0]
    count_n_calulate_average()
