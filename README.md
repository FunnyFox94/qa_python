In this case i develop some autotests for class BooksCollector
below you can check titles

tests.py::TestBooksCollector::test_add_new_book_to_collector[books0] PASSED [  6%]
tests.py::TestBooksCollector::test_add_new_book_to_collector[books1] PASSED [ 13%]
tests.py::TestBooksCollector::test_add_new_book_to_collector[books2] PASSED [ 20%]
tests.py::TestBooksCollector::test_set_book_genre_if_correct_genre PASSED [ 26%]
tests.py::TestBooksCollector::test_get_book_genre_positive_result PASSED [ 33%]
tests.py::TestBooksCollector::test_get_book_genre_if_genre_not_match[\u0413\u0430\u0440\u0440\u0438 \u041f\u043e\u0442\u0442\u0435\u0440 \u0438 \u043a\u0443\u0431\u043e\u043a \u043e\u0433\u043d\u044f-\u041d\u0430\u0443\u0447\u043f\u043e\u043f] PASSED [ 40%]
tests.py::TestBooksCollector::test_get_books_with_specific_genre PASSED  [ 46%]
tests.py::TestBooksCollector::test_get_books_with_specific_genre_if_genre_not_match[\u0413\u0430\u0440\u0440\u0438 \u041f\u043e\u0442\u0442\u0435\u0440 \u0438 \u043a\u0443\u0431\u043e\u043a \u043e\u0433\u043d\u044f-\u041d\u0430\u0443\u0447\u043f\u043e\u043f] PASSED [ 53%]
tests.py::TestBooksCollector::test_get_books_genre PASSED                [ 60%]
tests.py::TestBooksCollector::test_get_books_for_children_positive_result PASSED [ 66%]
tests.py::TestBooksCollector::test_get_books_for_children_when_book_in_adults_list[\u0413\u0430\u0440\u0440\u0438 \u041f\u043e\u0442\u0442\u0435\u0440 \u0438 \u043a\u0443\u0431\u043e\u043a \u043e\u0433\u043d\u044f-\u0414\u0435\u0442\u0435\u043a\u0442\u0438\u0432] PASSED [ 73%]
tests.py::TestBooksCollector::test_add_book_in_favorites_positive PASSED [ 80%]
tests.py::TestBooksCollector::test_add_book_in_favorites_when_book_already_favorite[books0] PASSED [ 86%]
tests.py::TestBooksCollector::test_delete_book_from_favorites PASSED     [ 93%]
tests.py::TestBooksCollector::test_get_list_of_favorites_books[books0] PASSED [100%]
