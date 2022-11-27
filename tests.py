from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_true(self):
        collector = BooksCollector()
        book_name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(book_name)

        assert book_name in collector.books_rating

    def test_new_book_has_rating_one_true(self):
        collector = BooksCollector()
        book_name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(book_name)

        assert collector.get_book_rating(book_name) == 1

    def test_add_two_books_true(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    def test_set_book_rating_true(self):
        collector = BooksCollector()
        book_name = 'Гордость и предубеждение и зомби'
        book_rating = 9
        collector.add_new_book(book_name)
        collector.set_book_rating(book_name, book_rating)
        assert collector.books_rating[book_name] == book_rating

    def test_set_book_rating_false(self):
        collector = BooksCollector()
        book_name = 'Гордость и предубеждение и зомби'
        book_rating = 11
        collector.add_new_book(book_name)
        collector.set_book_rating(book_name, book_rating)
        assert collector.get_book_rating(book_name) != book_rating and collector.get_book_rating(book_name) == 1

    def test_get_book_rating_true(self):
        collector = BooksCollector()
        book_name = 'Гордость и предубеждение и зомби'
        book_rating = 9
        collector.add_new_book(book_name)
        collector.set_book_rating(book_name, book_rating)
        assert collector.get_book_rating(book_name) == book_rating

    def test_get_books_with_specific_rating_true(self):
        collector = BooksCollector()
        book_name_1 = 'Гордость и предубеждение и зомби'
        book_name_2 = 'Что делать, если ваш кот хочет вас убить'
        book_rating_1 = 9
        book_rating_2 = 2
        collector.add_new_book(book_name_1)
        collector.set_book_rating(book_name_1, book_rating_1)
        collector.add_new_book(book_name_2)
        collector.set_book_rating(book_name_2, book_rating_2)
        assert collector.get_books_with_specific_rating(9) == [book_name_1]

    def test_get_books_rating_true(self):
        collector = BooksCollector()
        book_name_1 = 'Гордость и предубеждение и зомби'
        book_name_2 = 'Что делать, если ваш кот хочет вас убить'
        book_rating_1 = 9
        book_rating_2 = 2
        collector.add_new_book(book_name_1)
        collector.set_book_rating(book_name_1, book_rating_1)
        collector.add_new_book(book_name_2)
        collector.set_book_rating(book_name_2, book_rating_2)
        assert collector.get_books_rating() == {book_name_1: book_rating_1,
                                                book_name_2: book_rating_2}

    def test_add_book_in_favorites_true(self):
        collector = BooksCollector()
        book_name_1 = 'Гордость и предубеждение и зомби'
        book_name_2 = 'Что делать, если ваш кот хочет вас убить'
        book_rating_1 = 9
        book_rating_2 = 2
        collector.add_new_book(book_name_1)
        collector.set_book_rating(book_name_1, book_rating_1)
        collector.add_new_book(book_name_2)
        collector.set_book_rating(book_name_2, book_rating_2)
        collector.add_book_in_favorites(book_name_1)
        assert book_name_1 in collector.favorites

    def test_delete_book_from_favorites_true(self):
        collector = BooksCollector()
        book_name_1 = 'Гордость и предубеждение и зомби'
        book_name_2 = 'Что делать, если ваш кот хочет вас убить'
        book_rating_1 = 9
        book_rating_2 = 2
        collector.add_new_book(book_name_1)
        collector.set_book_rating(book_name_1, book_rating_1)
        collector.add_new_book(book_name_2)
        collector.set_book_rating(book_name_2, book_rating_2)
        collector.add_book_in_favorites(book_name_1)
        collector.add_book_in_favorites(book_name_2)
        collector.delete_book_from_favorites(book_name_1)
        assert len(collector.favorites) == 1 and book_name_2 in collector.favorites

    def test_get_list_of_favorites_books_true(self):
        collector = BooksCollector()
        book_name_1 = 'Гордость и предубеждение и зомби'
        book_name_2 = 'Что делать, если ваш кот хочет вас убить'
        book_rating_1 = 9
        book_rating_2 = 2
        collector.add_new_book(book_name_1)
        collector.set_book_rating(book_name_1, book_rating_1)
        collector.add_new_book(book_name_2)
        collector.set_book_rating(book_name_2, book_rating_2)
        collector.add_book_in_favorites(book_name_1)
        collector.add_book_in_favorites(book_name_2)
        assert len(collector.get_list_of_favorites_books()) == 2 and \
               book_name_1 in collector.get_list_of_favorites_books() and \
               book_name_2 in collector.get_list_of_favorites_books()
