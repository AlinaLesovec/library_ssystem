from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

@dataclass
class Reader:
    id: Optional[int] = None
    name: str = ""
    email: str = ""
    phone: str = ""
    registration_date: datetime = field(default_factory=datetime.now)

    def update_info(self, name=None, email=None, phone=None):
        if name:
            self.name = name
        if email:
            self.email = email
        if phone:
            self.phone = phone

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "registration_date": self.registration_date.isoformat()
        }