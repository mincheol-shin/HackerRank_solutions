def gradingStudents(grades):
    rounded_grades = []

    for i in grades:
        if i < 38 or i % 5 < 3:
            rounded_grades.append(i)
        else:
            # 5로 나눈 나머지는 반올림을 판가름하는 숫자가 될 것이고..
            rounded_grades.append(i + (5-(i % 5)))

    return rounded_grades
if __name__ == '__main__':

    grades_count = int(input().strip())
    grades = [int(input()) for _ in range(grades_count)]

    result = gradingStudents(grades)

    print(*result)