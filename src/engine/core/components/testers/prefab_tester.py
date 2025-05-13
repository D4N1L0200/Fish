import pygame
from random import randint
from ..component import Component


class PrefabTester(Component):
    required_dependencies: list[str] = ["InputListener"]

    def __init__(self) -> None:
        self.range: int = 500
        super().__init__()

    def handle_events(self, event: pygame.event.Event) -> None:
        super().handle_events(event)

        if self.parent is None:
            return

        input_listener = self.parent.inputlistener

        if input_listener.get_input("space"):
            from ...prefabs import Prefabs

            box = Prefabs.spawn("main", "box")
            pos = (randint(-self.range, self.range), randint(-self.range, self.range))
            box.transform.position = pos
