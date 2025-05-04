import pygame
from ..component import Component


class InputListener(Component):
    def __init__(self) -> None:
        super().__init__()
        self.inputs: dict[str, bool] = {}
        self.mapping: dict[int, str] = {
            pygame.K_w: "move_up",
            pygame.K_s: "move_down",
            pygame.K_a: "move_left",
            pygame.K_d: "move_right",
            pygame.K_q: "rotate_left",
            pygame.K_e: "rotate_right",
            pygame.K_UP: "scale_up",
            pygame.K_DOWN: "scale_down",
            pygame.K_LEFT: "scale_left",
            pygame.K_RIGHT: "scale_right",
            pygame.K_SPACE: "space",
        }

    def handle_events(self, event: pygame.event.Event) -> None:
        super().handle_events(event)

        if event.type == pygame.KEYDOWN:
            if event.key in self.mapping:
                self.inputs[self.mapping[event.key]] = True
        elif event.type == pygame.KEYUP:
            if event.key in self.mapping:
                self.inputs[self.mapping[event.key]] = False

    def get_input(self, name: str) -> bool:
        return self.inputs.get(name, False)
