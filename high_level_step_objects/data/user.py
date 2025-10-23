from datetime import date
from enum import Enum

from dataclasses import dataclass

class Gender(Enum):
    MALE = 'Male'
    FEMALE = 'Female'
    OTHER = 'Other'

class Hobby(Enum):
    SPORTS = 'Sports'
    READING = 'Reading'
    MUSIC = 'Music'


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: Gender
    phone: str
    date_of_birth: date
    subjects: str
    hobbies: tuple[Hobby, ...]
    picture: str
    address: str
    state: str
    city: str

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def formatted_date_of_birth(self):
        return self.date_of_birth.strftime('%d %B,%Y')