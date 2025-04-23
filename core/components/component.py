import pygame

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from core import Object


class Component:
    dependencies: list[type] = []

    def __init__(self) -> None:
        self.parent: Object | None = None

    def update(self, dt: float) -> None:
        pass

    def draw(self, surface: pygame.Surface) -> None:
        pass

    def handle_events(self, event: pygame.event.Event) -> None:
        pass

    def to_json(self) -> dict[str, Any]:
        return {}

    @classmethod
    def from_json(cls, **kwargs) -> "Component":
        return cls(**kwargs)

    def __repr__(self) -> str:
        return self.__class__.__name__
