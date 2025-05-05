import pygame
from ..component import Component


class InputListener(Component):
    def __init__(self) -> None:
        super().__init__()
        self.inputs: dict[str, bool] = {}
        self.input_values: dict[str, float] = {}
        self.mapping: dict[str, dict] = {
            "keyboard": {
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
            },
            "joystick": {
                0: "space",
                1: "B",
                2: "X",
                3: "Y",
                4: "LB",
                5: "RB",
                6: "back",
                7: "start",
                8: "left_stick",
                9: "right_stick",
                "hat_0": {
                    (0, 1): "move_up",
                    (0, -1): "move_down",
                    (1, 0): "move_right",
                    (-1, 0): "move_left",
                    (-1, -1): "move_down | move_left",
                    (1, -1): "move_down | move_right",
                    (1, 1): "move_up | move_right",
                    (-1, 1): "move_up | move_left",
                },
                "axis_0": "move_right | move_left",
                "axis_1": "move_down | move_up",
                "axis_2": "scale_right | scale_left",
                "axis_3": "scale_down | scale_up",
                "axis_4": "rotate_left",  # "trigger_left",
                "axis_5": "rotate_right",  # "trigger_right",
            },
        }

    def handle_events(self, event: pygame.event.Event) -> None:
        super().handle_events(event)

        if event.type == pygame.KEYDOWN:
            if event.key in self.mapping["keyboard"]:
                self.set_input(self.mapping["keyboard"][event.key], True)
            # else:
            #     print(f"Keyboard key '{event.key}' not mapped")
        elif event.type == pygame.KEYUP:
            if event.key in self.mapping["keyboard"]:
                self.set_input(self.mapping["keyboard"][event.key], False)
        elif event.type == pygame.JOYBUTTONDOWN:
            if event.button in self.mapping["joystick"]:
                self.set_input(self.mapping["joystick"][event.button], True)
            # else:
            #     print(f"Joystick button '{event.button}' not mapped")
        elif event.type == pygame.JOYBUTTONUP:
            if event.button in self.mapping["joystick"]:
                self.set_input(self.mapping["joystick"][event.button], False)
        elif event.type == pygame.JOYHATMOTION:
            hat = self.mapping["joystick"][f"hat_{event.hat}"]
            if event.value in hat:
                self.set_input(hat[event.value], True)
            elif event.value == (0, 0):
                for value in hat.values():
                    self.inputs[value] = False
        elif event.type == pygame.JOYAXISMOTION:
            if f"axis_{event.axis}" in self.mapping["joystick"]:
                axis_binds: list[str] = self.mapping["joystick"][f"axis_{event.axis}"].split(" | ")
                axis_value: float = round(event.value, 4)
                if len(axis_binds) == 2:
                    if axis_value > 0:
                        self.set_input(axis_binds[0], True)
                        self.set_input(axis_binds[1], False)
                    elif axis_value < 0:
                        self.set_input(axis_binds[0], False)
                        self.set_input(axis_binds[1], True)
                    else:
                        self.set_input(axis_binds[0], False)
                        self.set_input(axis_binds[1], False)
                    self.input_values[f"axis_{event.axis}"] = axis_value
                else:
                    self.set_input(
                        axis_binds[0], axis_value > 0
                    )
            else:
                print(f"Joystick axis '{event.axis}' not mapped")

    def set_input(self, name: str, value: bool) -> None:
        for inp in name.split(" | "):
            self.inputs[inp] = value

    def get_input(self, name: str) -> bool:
        return self.inputs.get(name, False)

    def get_input_value(self, name: str) -> float:
        return self.input_values.get(name, 0.0)
    