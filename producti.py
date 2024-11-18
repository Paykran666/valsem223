# Задача 1: Фильтрация студентов по возрасту

def filter_students_by_age(students):
    """Фильтрует студентов, оставляя только тех, кому больше 20 лет."""
    filtered_students = list(filter(lambda student: student[1] > 20, students))
    return [student[0] for student in filtered_students]

students = [("Алексей", 19), ("Мария", 21), ("Дмитрий", 22), ("Ольга", 20)]
print(f"Задача 1: {filter_students_by_age(students)}") # ['Мария', 'Дмитрий']


# Задача 2: Сортировка товаров по цене

def sort_products_by_price(products):
    """Сортирует товары по цене в порядке убывания."""
    return sorted(products, key=lambda product: product[1], reverse=True)

products = [("Хлеб", 50), ("Молоко", 80), ("Сыр", 150), ("Яблоки", 70)]
print(f"Задача 2: {sort_products_by_price(products)}") # [('Сыр', 150), ('Молоко', 80), ('Яблоки', 70), ('Хлеб', 50)]


# Задача 3: Преобразование координат

def transform_coordinates(points):
  """Преобразует координаты, увеличивая y на 10."""
  return list(map(lambda point: (point[0], point[1] + 10), points))

points = [(1, 2), (3, 4), (5, 6)]
print(f"Задача 3: {transform_coordinates(points)}") # [(1, 12), (3, 14), (5, 16)]


# Задача 4: Список сотрудников старше 30 лет, отсортированный по имени

def filter_and_sort_employees(employees):
    """Фильтрует сотрудников старше 30 лет и сортирует их по имени."""
    filtered_employees = list(filter(lambda employee: employee[1] > 30, employees))
    return sorted(filtered_employees, key=lambda employee: employee[0])

employees = [("Иван", 25, "инженер"), ("Анна", 32, "менеджер"), ("Борис", 45, "директор"), ("Мария", 28, "аналитик")]
print(f"Задача 4: {filter_and_sort_employees(employees)}") # [('Анна', 32, 'менеджер'), ('Борис', 45, 'директор')]


# Задача 5: Поиск самых дорогих продуктов

def find_expensive_products(products):
    """Находит продукты дороже 100 и возвращает их названия."""
    expensive_products = list(filter(lambda product: product[1] > 100, products))
    return list(map(lambda product: product[0], expensive_products))

products = [("Бананы", 120), ("Мясо", 300), ("Яблоки", 80), ("Сыр", 200), ("Молоко", 50)]
print(f"Задача 5: {find_expensive_products(products)}") # ['Бананы', 'Мясо', 'Сыр']

