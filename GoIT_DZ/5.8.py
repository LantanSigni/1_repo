grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}
students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}


def formatted_grades(students):
    result = []

    for i, (name, grade) in enumerate(students.items(), start=1):
        points = grades.get(grade, 0)
        result.append(f"{i:>4}|{name:<10}|{grade:^5}|{points:^5}")

    return result


for el in formatted_grades(students):
    print(el)
