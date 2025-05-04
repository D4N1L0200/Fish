import sys
import pygame
from .scene import Scene


class Game:
    def __init__(
        self, width=1280, height=720, title="Fishing Island Experiment"
    ) -> None:
        pygame.init()
        pygame.joystick.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.running = True

        if pygame.joystick.get_count() > 1:
            self.joystick = pygame.joystick.Joystick(0)
            self.joystick.init()
            print(self.joystick.get_name())
            print(self.joystick.get_numaxes())
            print(self.joystick.get_numballs())
            print(self.joystick.get_numhats())
            print(self.joystick.get_numbuttons())

        pygame.event.set_blocked(None)
        pygame.event.set_allowed(
            [
                pygame.QUIT,
                pygame.KEYDOWN,
                pygame.KEYUP,
                pygame.JOYAXISMOTION,
                pygame.JOYBALLMOTION,
                pygame.JOYHATMOTION,
                pygame.JOYBUTTONUP,
                pygame.JOYBUTTONDOWN,
            ]
        )

        self.scenes: dict[str, Scene] = {}
        self.active_scene: str = ""

    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            self.scenes[self.active_scene].handle_events(event)

    def update(self, dt) -> None:
        self.scenes[self.active_scene].update(dt)

    def draw(self) -> None:
        self.screen.fill((0, 0, 0))
        self.scenes[self.active_scene].draw(self.screen)
        pygame.display.flip()

    def run(self) -> None:
        while self.running:
            if self.active_scene not in self.scenes:
                raise Exception(f"Scene {self.active_scene} does not exist")

            dt = self.clock.tick(60) / 1000

            self.handle_events()
            self.update(dt)
            self.draw()

        pygame.quit()
        sys.exit()
