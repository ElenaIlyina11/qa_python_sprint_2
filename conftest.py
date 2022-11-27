import pytest
from main import BooksCollector
from tests import book_name_1, book_name_2, book_rating_1, book_rating_2


@pytest.fixture
def add_new_book():
    collector = BooksCollector()
    collector.add_new_book(book_name_1)
    return collector


@pytest.fixture
def add_new_book_with_rating():
    collector = BooksCollector()
    collector.add_new_book(book_name_1)
    collector.set_book_rating(book_name_1, book_rating_1)
    return collector


@pytest.fixture()
def add_two_new_books():
    collector = BooksCollector()
    collector.add_new_book(book_name_1)
    collector.add_new_book(book_name_2)
    return collector


@pytest.fixture()
def add_two_new_books_with_rating():
    collector = BooksCollector()
    collector.add_new_book(book_name_1)
    collector.set_book_rating(book_name_1, book_rating_1)
    collector.add_new_book(book_name_2)
    collector.set_book_rating(book_name_2, book_rating_2)
    return collector


@pytest.fixture()
def add_two_new_books_with_rating_and_add_to_favorites():
    collector = BooksCollector()
    collector.add_new_book(book_name_1)
    collector.set_book_rating(book_name_1, book_rating_1)
    collector.add_new_book(book_name_2)
    collector.set_book_rating(book_name_2, book_rating_2)
    collector.add_book_in_favorites(book_name_1)
    collector.add_book_in_favorites(book_name_2)
    return collector
