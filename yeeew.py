text = input("Введите текст: ")
words = text.lower().split() # Преобразуем текст в нижний регистр для игнорирования регистра

word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print(word_counts)
