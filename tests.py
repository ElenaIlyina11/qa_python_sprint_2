from main import BooksCollector

book_name_1 = 'Гордость и предубеждение и зомби'
book_name_2 = 'Что делать, если ваш кот хочет вас убить'
book_rating_1 = 9
book_rating_2 = 2


class TestBooksCollector:

    def test_add_new_book_add_one_book_true(self):
        collector = BooksCollector()
        collector.add_new_book(book_name_1)
        assert book_name_1 in collector.books_rating

    def test_add_new_book_book_rating_is_one_true(self, add_new_book):
        assert add_new_book.books_rating[book_name_1] == 1

    def test_add_new_book_add_two_books_true(self):
        collector = BooksCollector()
        collector.add_new_book(book_name_1)
        collector.add_new_book(book_name_2)
        assert len(collector.books_rating) == 2

    def test_set_book_rating_is_rating_equal_to_value_set_earlier_true(self, add_new_book):
        add_new_book.set_book_rating(book_name_1, book_rating_1)
        assert add_new_book.books_rating[book_name_1] == book_rating_1

    def test_set_book_rating_cant_set_rating_more_ten_false(self, add_new_book):
        bad_book_rating = 11
        add_new_book.set_book_rating(book_name_1, bad_book_rating)
        assert add_new_book.books_rating[book_name_1] != bad_book_rating and add_new_book.books_rating[book_name_1] == 1

    def test_get_book_rating_book_rating_is_equal_to_set_earlier_true(self, add_new_book_with_rating):
        assert add_new_book_with_rating.get_book_rating(book_name_1) == book_rating_1

    def test_get_books_with_specific_rating_list_contains_expected_book_true(self, add_two_new_books_with_rating):
        assert add_two_new_books_with_rating.get_books_with_specific_rating(book_rating_1) == [book_name_1]

    def test_get_books_rating_returning_all_added_books_true(self, add_two_new_books_with_rating):
        assert add_two_new_books_with_rating.get_books_rating() == {book_name_1: book_rating_1,
                                                                    book_name_2: book_rating_2}

    def test_add_book_in_favorites_book_is_in_favorite_list_true(self, add_two_new_books_with_rating):
        add_two_new_books_with_rating.add_book_in_favorites(book_name_1)
        assert book_name_1 in add_two_new_books_with_rating.favorites

    def test_delete_book_from_favorites_books_is_deleted_from_favorites_true(self, add_two_new_books_with_rating_and_add_to_favorites):
        add_two_new_books_with_rating_and_add_to_favorites.delete_book_from_favorites(book_name_1)
        assert len(add_two_new_books_with_rating_and_add_to_favorites.favorites) == 1 and \
               book_name_2 in add_two_new_books_with_rating_and_add_to_favorites.favorites

    def test_get_list_of_favorites_books_list_contains_all_added_books_true(self, add_two_new_books_with_rating_and_add_to_favorites):
        assert len(add_two_new_books_with_rating_and_add_to_favorites.get_list_of_favorites_books()) == 2 and \
               book_name_1 in add_two_new_books_with_rating_and_add_to_favorites.get_list_of_favorites_books() and \
               book_name_2 in add_two_new_books_with_rating_and_add_to_favorites.get_list_of_favorites_books()
