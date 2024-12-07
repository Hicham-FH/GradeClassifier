from .classify import classify_grade
def calculate_average(grades):
    if not grades:
        return "No grades provided."
    return sum(grades) / len(grades)

def calculate_distribution(grades):
    distribution = {"Excellent": 0, "Good": 0, "Average": 0, "Poor": 0, "Fail": 0}
    for grade in grades:
        category = classify_grade(grade)
        if category in distribution:
            distribution[category] += 1
    return distribution
