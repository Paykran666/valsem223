class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
        else:
            print("Книги нет в библиотеке.")

    def __len__(self):
        return len(self.books)


library = Library()
book1 = Book("Война и мир", "Лев Толстой", 1869)
book2 = Book("Преступление и наказание", "Фёдор Достоевский", 1866)
library.add_book(book1)
library.add_book(book2)
print(f"Количество книг: {len(library)}") # Количество книг
library.remove_book(book1)
print(f"Количество книг после удаления: {len(library)}") # Количество книг

