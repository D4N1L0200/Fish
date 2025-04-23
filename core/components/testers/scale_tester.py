import pygame
from ..component import Component
from ..world.transform import Transform


class ScaleTester(Component):
    dependencies: list[type] = [Transform]

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

        scale: tuple[float, float] = self.delta

        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_UP:
                    self.delta = (scale[0], scale[1] - self.speed)
                case pygame.K_DOWN:
                    self.delta = (scale[0], scale[1] + self.speed)
                case pygame.K_LEFT:
                    self.delta = (scale[0] - self.speed, scale[1])
                case pygame.K_RIGHT:
                    self.delta = (scale[0] + self.speed, scale[1])

        elif event.type == pygame.KEYUP:
            match event.key:
                case pygame.K_UP:
                    self.delta = (scale[0], scale[1] + self.speed)
                case pygame.K_DOWN:
                    self.delta = (scale[0], scale[1] - self.speed)
                case pygame.K_LEFT:
                    self.delta = (scale[0] + self.speed, scale[1])
                case pygame.K_RIGHT:
                    self.delta = (scale[0] - self.speed, scale[1])
