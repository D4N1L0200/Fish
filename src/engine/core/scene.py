import pygame
from .object import Object


class Scene:
    def __init__(self) -> None:
        self.objects: list[Object] = []

    def add_obj(self, obj: Object) -> None:
        obj.scene = self
        self.objects.append(obj)

    def search(self, tag: str) -> list[Object]:
        objs: list[Object] = []
        for o in self.objects:
            if o.has("tag") and o.tag.has(tag):
                objs.append(o)
        return objs
    
    def start(self) -> None:
        for o in self.objects:
            o.start()

    def update(self, dt: float) -> None:
        for o in self.objects:
            if not o.active.get():
                continue

            o.update(dt)

    def draw(self, surface: pygame.Surface) -> None:
        for o in self.objects:
            if not o.active.get():
                continue

            o.draw(surface)

    def handle_events(self, event: pygame.event.Event) -> None:
        for o in self.objects:
            if not o.active.get():
                continue

            o.handle_events(event)

    def to_json(self) -> dict:
        return {"objects": [o.to_json() for o in self.objects]}

    @classmethod
    def from_json(cls, data: dict) -> "Scene":
        scn = cls()
        for o in data["objects"]:
            scn.add_obj(Object.from_json(o))
        return scn
