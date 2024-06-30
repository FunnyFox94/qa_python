import pytest

from main import BooksCollector


class TestBooksCollector:
    @pytest.mark.parametrize(
        'books', [
            [],
            ['Гарри Поттер и кубок огня',
             'Люди в черном'],
            ['Гарри Поттер и кубок огня',
             'Люди в черном',
             'Пираты карибского моря']
        ]
    )
    def test_add_new_book_to_collector(self, book_collector, books):
        for book in books:
            book_collector.add_new_book(book)
        assert len(book_collector.get_books_genre()) == len(books)

    def test_set_book_genre_if_correct_genre(self, book_collector, book, genre):
        book_collector.add_new_book(book)
        book_collector.set_book_genre(book, genre)
        assert book_collector.books_genre[book] == genre

    def test_get_book_genre_positive_result(self, book_collector, book, genre):
        book_collector.add_new_book(book)
        book_collector.set_book_genre(book, genre)
        assert book_collector.get_book_genre(book) == genre

    @pytest.mark.parametrize(
        'book, genre', [
            ['Гарри Поттер и кубок огня', 'Научпоп']
        ]
    )
    def test_get_book_genre_if_genre_not_match(self, book_collector, book, genre):
        book_collector.add_new_book(book)
        book_collector.set_book_genre(book, genre)
        assert book_collector.get_book_genre(book) == ''

    def test_get_books_with_specific_genre(self, book_collector, book, genre):
        book_collector.add_new_book(book)
        book_collector.set_book_genre(book, genre)
        assert book_collector.get_books_with_specific_genre(genre) == ['Гарри Поттер и кубок огня']

    @pytest.mark.parametrize(
        'book, genre', [
            ['Гарри Поттер и кубок огня', 'Научпоп']
        ]
    )
    def test_get_books_with_specific_genre_if_genre_not_match(self, book_collector, book, genre):
        book_collector.add_new_book(book)
        book_collector.set_book_genre(book, genre)
        assert len(book_collector.get_books_with_specific_genre(genre)) == 0

    def test_get_books_genre(self, book_collector, book, genre):
        book_collector.add_new_book(book)
        book_collector.set_book_genre(book, genre)
        assert book_collector.get_books_genre() == {'Гарри Поттер и кубок огня': 'Фантастика'}

    def test_get_books_for_children_positive_result(self, book_collector, book, genre):
        book_collector.add_new_book(book)
        book_collector.set_book_genre(book, genre)
        assert book_collector.get_books_for_children() == ['Гарри Поттер и кубок огня']

    @pytest.mark.parametrize(
        'book, genre', [
            ['Гарри Поттер и кубок огня', 'Детектив']
        ]
    )
    def test_get_books_for_children_when_book_in_adults_list(self, book_collector, book, genre):
        book_collector.add_new_book(book)
        book_collector.set_book_genre(book, genre)
        assert len(book_collector.get_books_for_children()) == 0

    def test_add_book_in_favorites_positive(self, book_collector, book):
        book_collector.add_new_book(book)
        book_collector.add_book_in_favorites(book)
        assert book_collector.favorites == ['Гарри Поттер и кубок огня']

    @pytest.mark.parametrize(
        'books', [['Гарри Поттер и кубок огня', 'Гарри Поттер и кубок огня', 'Гарри Поттер и кубок огня']]
    )
    def test_add_book_in_favorites_when_book_already_favorite(self, book_collector, books):
        for i in books:
            book_collector.add_new_book(i)
            book_collector.add_book_in_favorites(i)
        assert book_collector.favorites == ['Гарри Поттер и кубок огня'] and len(book_collector.favorites) == 1

    def test_delete_book_from_favorites(self, book_collector, book):
        book_collector.add_new_book(book)
        book_collector.add_book_in_favorites(book)
        book_collector.delete_book_from_favorites(book)
        assert len(book_collector.favorites) == 0

    @pytest.mark.parametrize(
        'books', [
            ['Гарри Поттер и кубок огня', 'Пираты карибского моря']
        ]
    )
    def test_get_list_of_favorites_books(self, book_collector, books):
        for i in books:
            book_collector.add_new_book(i)
            book_collector.add_book_in_favorites(i)
        assert book_collector.get_list_of_favorites_books() == ['Гарри Поттер и кубок огня', 'Пираты карибского моря']
