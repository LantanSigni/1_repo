# points = {
#     (0, 1): 2,
#     (0, 2): 3.8,
#     (0, 3): 2.7,
#     (1, 2): 2.5,
#     (1, 3): 4.1,
#     (2, 3): 3.9,
# }


# def calculate_distance(coordinates):
#     if len(coordinates) <= 1:
#         return 0


def calculate_distance(coordinates):
    points = {(0, 1): 2, (0, 2): 3.8, (0, 3): 2.7,
              (1, 2): 2.5, (1, 3): 4.1, (2, 3): 3.9}

    if len(coordinates) <= 1:  # Якщо список порожній або містить лише одну точку
        return 0

    total_distance = 0
    for i in range(len(coordinates) - 1):
        # Створюємо кортеж для пошуку у словнику points
        point_tuple = (
            min(coordinates[i], coordinates[i + 1]), max(coordinates[i], coordinates[i + 1]))

        # Додаємо відстань між точками до загальної відстані
        total_distance += points[point_tuple]

    return total_distance


# Приклад використання:
drone_path = [0, 1, 3, 2, 0]
result = calculate_distance(drone_path)
print(f"Загальна відстань польоту дрона: {result}")
