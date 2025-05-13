import pygame
from typing import Any, TYPE_CHECKING
from . import components

if TYPE_CHECKING:
    from .scene import Scene


class Object:
    def __init__(self) -> None:
        self.components: dict[str, list[components.Component]] = {}
        self.scene: Scene | None = None

    def add_component(self, component: components.Component) -> None:
        key: str = component.__class__.__name__.lower()

        component.parent = self

        self.components.setdefault(key, []).append(component)

    def get_components(self, name: str) -> list[components.Component]:
        return self.components.get(name.lower(), [])
    
    def start(self) -> None:
        for components in self.components.values():
            for component in components:
                key: str = component.__class__.__name__.lower()

                if not component.required_dependencies: 
                    continue

                dependencies: list[str] = component.required_dependencies.copy()
                required_dependencies: list[str] = [d for d in dependencies if " " not in d]
                selected_dependencies: list[str] = [d for d in dependencies if "|" in d]

                for cs in self.components.values():
                    for c in cs:
                        type_name: str = type(c).__name__
                        if type_name in required_dependencies:
                            required_dependencies.remove(type_name)

                for cs in self.components.values():
                    for c in cs:
                        type_name = type(c).__name__
                        for d in selected_dependencies:
                            if type_name in d:
                                selected_dependencies.remove(d)

                if required_dependencies != [] or selected_dependencies != []:
                    raise AttributeError(
                        f"{self.__class__.__name__}'s {key} depends on {required_dependencies[0]}"
                    )

    def update(self, dt: float) -> None:
        for comps in self.components.values():
            for c in comps:
                c.update(dt)

    def draw(self, surface: pygame.Surface) -> None:
        for comps in self.components.values():
            for c in comps:
                c.draw(surface)

    def handle_events(self, event: pygame.event.Event) -> None:
        for comps in self.components.values():
            for c in comps:
                c.handle_events(event)

    def to_json(self) -> dict:
        obj: dict[str, list[dict[str, Any]]] = {}

        for cs in self.components.values():
            cname: str = cs[0].__class__.__name__
            obj[cname] = [c.to_json() for c in cs]

        return obj

    @classmethod
    def from_json(cls, obj: dict[str, list[dict[str, Any]]]) -> "Object":
        o = cls()
        for cname, cs in obj.items():
            for c in cs:
                o.add_component(getattr(components, cname).from_json(**c))
        return o

    def has(self, name: str) -> bool:
        return name in self.components

    def __getattribute__(self, name) -> Any:
        try:
            attr = super().__getattribute__(name)
            return attr
        except AttributeError:
            try:
                comps = self.components.get(name.lower())
                if comps and len(comps) == 1:
                    return comps[0]
                return comps
            except KeyError:
                raise AttributeError(
                    f"'{self.__class__.__name__}' object has no attribute '{name}'"
                )
