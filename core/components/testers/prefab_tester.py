import pygame
from ..component import Component
from ..input.input_listener import InputListener
from random import randint


class PrefabTester(Component):
    def __init__(self) -> None:
        self.range: int = 500
        super().__init__()

    def handle_events(self, event: pygame.event.Event) -> None:
        super().handle_events(event)

        if self.parent is None:
            return

        input_listener = self.parent.get_components("inputlistener")[0]
        if not input_listener or not isinstance(input_listener, InputListener):
            return

        if input_listener.get_input("space"):
            from ...prefabs import Prefabs

            box = Prefabs.spawn("main", "box")
            pos = (randint(-self.range, self.range), randint(-self.range, self.range))
            box.transform.position = pos
