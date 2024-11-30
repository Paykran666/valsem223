employees = {}

def add_employee():
    emp_id = input("Введите ID сотрудника: ")
    if emp_id in employees:
        print("ID уже существует. Попробуйте другой ID.")
        return

    name = input("Введите имя сотрудника: ")
    position = input("Введите должность: ")
    while True:
        try:
            salary = float(input("Введите зарплату: "))
            break
        except ValueError:
            print("Некорректный ввод зарплаты. Попробуйте еще раз.")

    employees[emp_id] = {"name": name, "position": position, "salary": salary}
    print("Сотрудник добавлен.")


def print_all_employees():
    if not employees:
        print("База данных сотрудников пуста.")
        return

    for emp_id, emp_data in employees.items():
        print(f"ID: {emp_id}")
        print(f"Имя: {emp_data['name']}")
        print(f"Должность: {emp_data['position']}")
        print(f"Зарплата: {emp_data['salary']}")
        print("-" * 20)


def find_employee():
    emp_id = input("Введите ID сотрудника для поиска: ")
    employee = employees.get(emp_id)
    if employee:
        print(f"Информация о сотруднике {emp_id}:")
        print(f"Имя: {employee['name']}")
        print(f"Должность: {employee['position']}")
        print(f"Зарплата: {employee['salary']}")
    else:
        print(f"Сотрудник с ID {emp_id} не найден.")


def update_salary():
    emp_id = input("Введите ID сотрудника для изменения зарплаты: ")
    employee = employees.get(emp_id)
    if employee:
        while True:
            try:
                new_salary = float(input("Введите новую зарплату: "))
                break
            except ValueError:
                print("Некорректный ввод зарплаты. Попробуйте еще раз.")
        employee["salary"] = new_salary
        print(f"Зарплата сотрудника {emp_id} обновлена.")
    else:
        print(f"Сотрудник с ID {emp_id} не найден.")


def delete_employee():
    emp_id = input("Введите ID сотрудника для удаления: ")
    if emp_id in employees:
        del employees[emp_id]
        print(f"Сотрудник {emp_id} удален.")
    else:
        print(f"Сотрудник с ID {emp_id} не найден.")


while True:
    print("\nМеню:")
    print("1. Добавить сотрудника")
    print("2. Вывести информацию о всех сотрудниках")
    print("3. Найти сотрудника по ID")
    print("4. Изменить зарплату сотрудника")
    print("5. Удалить сотрудника")
    print("6. Выйти")

    choice = input("Выберите действие: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        print_all_employees()
    elif choice == "3":
        find_employee()
    elif choice == "4":
        update_salary()
    elif choice == "5":
        delete_employee()
    elif choice == "6":
        break
    else:
        print("Неверный выбор. Попробуйте еще раз.")

