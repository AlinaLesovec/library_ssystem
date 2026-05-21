from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

@dataclass
class Loan:
    id: Optional[int] = None
    book_id: int = 0
    reader_id: int = 0
    loan_date: datetime = field(default_factory=datetime.now)
    return_date: datetime = field(default_factory=datetime.now)
    is_returned: bool = False

    def return_book(self):
        self.is_returned = True

    def is_overdue(self):
        return (not self.is_returned) and (
            datetime.now() > self.return_date
        )

    def to_dict(self):
        return {
            "id": self.id,
            "book_id": self.book_id,
            "reader_id": self.reader_id,
            "loan_date": self.loan_date.isoformat(),
            "return_date": self.return_date.isoformat(),
            "is_returned": self.is_returned
        }