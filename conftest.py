import pytest
from practicum.qa_python.main import BooksCollector


@pytest.fixture
def book_collector():
    return BooksCollector()


@pytest.fixture
def book():
    return 'Гарри Поттер и кубок огня'


@pytest.fixture
def genre():
    return 'Фантастика'
