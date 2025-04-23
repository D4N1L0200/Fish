import pygame
from ..component import Component
from ..world.transform import Transform


class MovementTester(Component):
    dependencies: list[type] = [Transform]

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

        move: tuple[float, float] = self.delta

        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_w:
                    self.delta = (move[0], move[1] - self.speed)
                case pygame.K_s:
                    self.delta = (move[0], move[1] + self.speed)
                case pygame.K_a:
                    self.delta = (move[0] - self.speed, move[1])
                case pygame.K_d:
                    self.delta = (move[0] + self.speed, move[1])

        elif event.type == pygame.KEYUP:
            match event.key:
                case pygame.K_w:
                    self.delta = (move[0], move[1] + self.speed)
                case pygame.K_s:
                    self.delta = (move[0], move[1] - self.speed)
                case pygame.K_a:
                    self.delta = (move[0] + self.speed, move[1])
                case pygame.K_d:
                    self.delta = (move[0] - self.speed, move[1])
