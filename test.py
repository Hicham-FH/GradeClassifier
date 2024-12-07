from gradeclassifier import classify_grade, classify_multiple_grades, calculate_average, calculate_distribution

grades = [19, 15, 12, 8, 5, 0]

for grade in grades:
    print(f"Grade: {grade}, Classification: {classify_grade(grade)}")

print("\nMultiple Grade Classification:")
print(classify_multiple_grades(grades))

print("\nAverage Grade:")
print(calculate_average(grades))

print("\nGrade Distribution:")
print(calculate_distribution(grades))
