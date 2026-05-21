import pytest
from models.book import Book
from models.reader import Reader
from models.loan import Loan

def test_book_creation():
    book = Book(title="Test Book", author="Test Author", isbn="123456", year=2024, quantity=5)
    assert book.title == "Test Book"
    assert book.author == "Test Author"
    assert book.isbn == "123456"
    assert book.year == 2024
    assert book.quantity == 5

def test_reader_creation():
    reader = Reader(name="John Doe", email="john@example.com", phone="123456789")
    assert reader.name == "John Doe"
    assert reader.email == "john@example.com"

def test_loan_creation():
    loan = Loan(book_id=1, reader_id=1, loan_date="2024-01-01")
    assert loan.book_id == 1
    assert loan.reader_id == 1