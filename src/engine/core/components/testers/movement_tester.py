import pygame
from ..component import Component


class MovementTester(Component):
    required_dependencies: list[str] = ["Transform", "InputListener"]

    def __init__(self) -> None:
        super().__init__()
        self.speed: float = 500
        self.delta: tuple[float, float] = (0.0, 0.0)

    def update(self, dt: float) -> None:
        if self.parent is None:
            return

        pos: tuple[float, float] = self.parent.transform.position
        pos = (pos[0] + self.delta[0] * dt, pos[1] + self.delta[1] * dt)
        self.parent.transform.position = pos

    def handle_events(self, event: pygame.event.Event) -> None:
        super().handle_events(event)

        if self.parent is None:
            return

        input_listener = self.parent.inputlistener

        dx: int = 0
        dy: int = 0

        if input_listener.get_input("move_up"):
            dy -= 1
        if input_listener.get_input("move_down"):
            dy += 1

        if input_listener.get_input("move_left"):
            dx -= 1
        if input_listener.get_input("move_right"):
            dx += 1

        self.delta = (dx * self.speed, dy * self.speed)
