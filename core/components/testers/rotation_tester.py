import pygame
from ..component import Component
from ..world.transform import Transform


class RotationTester(Component):
    dependencies: list[type] = [Transform]

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

        rot: float = self.delta

        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_q:
                    self.delta = rot - self.speed
                case pygame.K_e:
                    self.delta = rot + self.speed

        elif event.type == pygame.KEYUP:
            match event.key:
                case pygame.K_q:
                    self.delta = rot + self.speed
                case pygame.K_e:
                    self.delta = rot - self.speed
