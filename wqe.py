grades = {
    "математика": 5,
    "физика": 4,
    "информатика": 5,
    "химия": 3
}

# Вычисление среднего балла
average_grade = sum(grades.values()) / len(grades)

# Поиск предмета с наивысшей оценкой
best_subject = max(grades.items(), key=lambda item: item[1])[0]

# Вывод результатов
print(f"Средний балл: {average_grade}")
print(f"Лучшая оценка по предмету: {best_subject}")
