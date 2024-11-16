import re

def is_valid_email(email: str) -> bool:
    """Проверяет, является ли строка корректным почтовым адресом."""
    return bool(re.match(r"^[\w\.]+@[\w]+\.(com|org|ru)$", email))


def replace_prices(text: str) -> str:
    """Заменяет все суммы в тексте на слово PRICE."""
    return re.sub(r"\d+\s*руб[лей|.]?", "PRICE", text)


def split_by_sentence(text: str) -> list:
    """Разделяет текст на предложения."""
    return re.split(r"(?<=[.!?]+)\s*", text)


def extract_hashtags(text: str) -> list:
    """Извлекает все хештеги из текста."""
    return re.findall(r"#\w+", text)


def is_strong_password(password: str) -> bool:
    """Проверяет, соответствует ли пароль критериям безопасности."""
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r"[@#$%&*]", password):
        return False
    return True



# Примеры использования:
print(is_valid_email("example.email@gmail.com")) # True
print(is_valid_email("wrong_email@domain"))       # False
print(is_valid_email("user_name@domain.org"))     # True

text = "Цена ноутбука 50000 руб., а телефона - 2000 рубля."
print(replace_prices(text)) # "Цена ноутбука PRICE, а телефона - PRICE."

text = "Привет! Как дела? Все хорошо..."
print(split_by_sentence(text))   # ['Привет!', 'Как дела?', 'Все хорошо...']

text = "Сегодня отличный день! #python #programming #100DaysOfCode"
print(extract_hashtags(text)) # ['#python', '#programming', '#100DaysOfCode']

print(is_strong_password("Passw0rd@")) # True
print(is_strong_password("weakpass"))   # False

