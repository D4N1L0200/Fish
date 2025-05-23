import pygame
from ..component import Component


class ScaleTester(Component):
    required_dependencies: list[str] = ["Transform", "InputListener"]

    def __init__(self) -> None:
        super().__init__()
        self.speed: float = 2
        self.delta: tuple[float, float] = (0.0, 0.0)

    def update(self, dt: float) -> None:
        if self.parent is None:
            return

        scale: tuple[float, float] = self.parent.transform.scale
        scale = (scale[0] + self.delta[0] * dt, scale[1] + self.delta[1] * dt)
        self.parent.transform.scale = scale

    def handle_events(self, event: pygame.event.Event) -> None:
        super().handle_events(event)

        if self.parent is None:
            return

        input_listener = self.parent.inputlistener

        dx: int = 0
        dy: int = 0

        if input_listener.get_input("scale_up"):
            dy -= 1
        if input_listener.get_input("scale_down"):
            dy += 1

        if input_listener.get_input("scale_left"):
            dx -= 1
        if input_listener.get_input("scale_right"):
            dx += 1

        self.delta = (dx * self.speed, dy * self.speed)
