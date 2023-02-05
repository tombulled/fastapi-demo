from dataclasses import dataclass, field
from typing import (
    ClassVar,
    Generic,
    MutableMapping,
    Sequence,
    TypeVar,
)

from .models import Item


I = TypeVar("I", bound=Item)


@dataclass
class ItemDoesNotExistError(Exception):
    id: int

    def __str__(self) -> str:
        return f"An item with id {self.id} does not exist"


@dataclass
class ItemAlreadyExistsError(Exception):
    id: int

    def __str__(self) -> str:
        return f"An item with id {self.id} already exists"


@dataclass
class Repository(Generic[I]):
    index: int = 0
    items: MutableMapping[int, I] = field(default_factory=dict)

    def list(self) -> Sequence[I]:
        return tuple(self.items.values())

    def get(self, id: int, /) -> I:
        self._assert_exists(id)

        return self.items[id]

    def has(self, id: int, /) -> bool:
        return id in self.items

    def delete(self, id: int, /) -> None:
        self._assert_exists(id)

        del self.items[id]

    def add(self, item: I, /) -> None:
        if self.has(item.id):
            raise ItemAlreadyExistsError(id=item.id)

        self.items[item.id] = item

        self.index += 1

    def _assert_exists(self, id: int, /) -> None:
        if not self.has(id):
            raise ItemDoesNotExistError(id=id)
