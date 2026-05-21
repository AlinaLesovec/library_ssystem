from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Book:
    id: Optional[int] = None
    title: str = ""
    author: str = ""
    isbn: str = ""
    year: int = 0
    quantity: int = 1
    available: int = field(default=None)

    def __post_init__(self):
        if self.available is None:
            self.available = self.quantity

    def borrow_book(self):
        if self.available > 0:
            self.available -= 1

    def return_book(self):
        if self.available < self.quantity:
            self.available += 1

    def is_available(self):
        return self.available > 0

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "year": self.year,
            "quantity": self.quantity,
            "available": self.available
        }