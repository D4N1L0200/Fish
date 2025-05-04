import pygame
from ..component import Component
from ..input.input_listener import InputListener
from ..world.transform import Transform


# def create_box(pos):
#     box = Object()
#     box.add_component(components.Transform(pos, 180, (0.5, 0.5)))
#     box.add_component(components.Active(True))
#     box.add_component(components.RendererFrame(100, 100))
#     box.add_component(components.SpriteRenderer("assets/player.png"))
#     return box


class PrefabTester(Component):
    def __init__(self) -> None:
        super().__init__()

    def handle_events(self, event: pygame.event.Event) -> None:
        super().handle_events(event)

        if self.parent is None:
            return

        input_listener = self.parent.get_components("inputlistener")[0]
        if not input_listener or not isinstance(input_listener, InputListener):
            return

        if input_listener.get_input("space"):
            print("space")
