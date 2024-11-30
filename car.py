products = {}

# Запрос данных о продуктах
for i in range(3):
    product_name = input("Введите название продукта: ")
    while True:
        try:
            price = float(input(f"Введите его стоимость: ")) # Используем float для возможности ввода дробных чисел
            break
        except ValueError:
            print("Некорректный ввод стоимости. Попробуйте еще раз.")
    products[product_name] = price

# Запрос продукта для покупки
product_to_buy = input("Какой продукт вы хотите купить? ")

# Вывод стоимости или сообщения об ошибке
price = products.get(product_to_buy) # Используем .get() для безопасного доступа к элементу
if price is not None:
    print(f"Стоимость {product_to_buy}: {price}")
else:
    print(f"Извините, продукта '{product_to_buy}' нет в наличии.")

