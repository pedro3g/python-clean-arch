from uuid import uuid4
from typing import Optional

class User:
    def __init__(self, id: Optional[str], name: str, email: str, password: str):
        self.id = id or uuid4()
        self.name = name
        self.email = email
        self.password = password
