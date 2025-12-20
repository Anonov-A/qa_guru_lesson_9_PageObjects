from dataclasses import dataclass
from datetime import date


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str = 'Male'
    phone: str = ''
    birth_date: date = None
    subjects: list = None
    hobbies: list = None
    picture: str = ''
    address: str = ''
    state: str = 'NCR'
    city: str = 'Delhi'

    def __post_init__(self):
        if self.birth_date is None:
            self.birth_date = date(1900, 7, 27)
        if self.subjects is None:
            self.subjects = []
        if self.hobbies is None:
            self.hobbies = []

    @property
    def full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'

    @property
    def formatted_birth_date(self) -> str:
        return self.birth_date.strftime('%d %B,%Y')

    @property
    def state_and_city(self) -> str:
        return f'{self.state} {self.city}'