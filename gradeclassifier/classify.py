def classify_grade(grade):
    if grade < 0 or grade > 20:
        return "Invalid grade. Must be between 0 and 20."
    elif grade >= 16:
        return "Excellent"
    elif grade >= 12:
        return "Good"
    elif grade >= 8:
        return "Average"
    elif grade >= 4:
        return "Poor"
    else:
        return "Fail"

def classify_multiple_grades(grades):
    return {grade: classify_grade(grade) for grade in grades}
