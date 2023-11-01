def get_grade(key):
    grades = {'F': 1, 'FX': 2, 'E': 3, 'D': 3, 'C': 4, 'B': 5, 'A': 5}
    try:
        return grades[key]
    except KeyError:
        return None


key = input()
print(get_grade(key))


def get_description(key):
    grades = {'F': 'Unsatisfactorily', 'FX': 'Unsatisfactorily',
              'E': 'Enough', 'D': 'Satisfactorily', 'C': 'Good',
              'B': 'Very good', 'A': 'Perfectly'}
    try:
        return grades[key]
    except KeyError:
        return None


key = input()
print(get_description(key))
