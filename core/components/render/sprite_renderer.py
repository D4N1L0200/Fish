import pygame
import pathlib
from typing import Any
from ..component import Component


class SpriteRenderer(Component):
    required_dependencies: list[str] = ["RendererFrame"]

    def __init__(self, path: pathlib.Path | str) -> None:
        super().__init__()
        self._path: pathlib.Path = pathlib.Path(path)
        self._img: pygame.Surface = pygame.image.load(self._path)

    @property
    def path(self) -> pathlib.Path:
        return self._path

    @path.setter
    def path(self, value: pathlib.Path) -> None:
        self._path = value

    @property
    def img(self) -> pygame.Surface:
        return self._img

    @img.setter
    def img(self, value: pygame.Surface) -> None:
        self._img = value

    def to_json(self) -> dict[str, Any]:
        return {
            "path": str(self._path),
        }

    def __repr__(self):
        return f"{super().__repr__()}({self._path})"
