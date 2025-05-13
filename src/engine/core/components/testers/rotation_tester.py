import pygame
from ..component import Component


class RotationTester(Component):
    required_dependencies: list[str] = ["Transform", "InputListener"]

    def __init__(self) -> None:
        super().__init__()
        self.speed: float = 90
        self.delta: float = 0.0

    def update(self, dt: float) -> None:
        if self.parent is None:
            return

        rotation: float = self.parent.transform.rotation
        rotation = rotation + self.delta * dt
        self.parent.transform.rotation = rotation

    def handle_events(self, event: pygame.event.Event) -> None:
        super().handle_events(event)

        if self.parent is None:
            return

        input_listener = self.parent.inputlistener

        dr: int = 0

        if input_listener.get_input("rotate_left"):
            dr -= 1
        if input_listener.get_input("rotate_right"):
            dr += 1

        self.delta = dr * self.speed
