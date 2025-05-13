from ..component import Component
from typing import Any


class Tag(Component):
    def __init__(self, *tags: str) -> None:
        super().__init__()
        self._tags: set[str] = set(tags)

    def add(self, *tags: str) -> None:
        self._tags.update(tags)

    def has(self, tag: str) -> bool:
        return tag in self._tags

    def get(self) -> set[str]:
        return self._tags

    def remove(self, *tags: str) -> None:
        self._tags.difference_update(tags)

    def to_json(self) -> dict[str, Any]:
        return {
            "tags": list(self._tags),
        }

    @classmethod
    def from_json(cls, **kwargs) -> "Tag":
        return cls(*kwargs["tags"])

    def __repr__(self):
        return f"{super().__repr__()}({', '.join(self._tags)})"
