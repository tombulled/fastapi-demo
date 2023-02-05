from dataclasses import dataclass


@dataclass
class Item:
    id: int


@dataclass
class User(Item):
    name: str
    occupation: str
