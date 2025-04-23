from ..component import Component
from typing import Any


class Active(Component):
    def __init__(self, active: bool = True) -> None:
        super().__init__()
        self._active: bool = active

    def set(self, active: bool) -> None:
        self._active = active

    def get(self) -> bool:
        return self._active

    def toggle(self) -> None:
        self._active = not self._active

    def to_json(self) -> dict[str, Any]:
        return {
            "active": self._active,
        }

    def __repr__(self):
        return f"{super().__repr__()}({self._active})"
