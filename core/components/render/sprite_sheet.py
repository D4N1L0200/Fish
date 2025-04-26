import pygame
import pathlib
from typing import Any
from ..component import Component
from .renderer_frame import RendererFrame


class SpriteSheet(Component):
    dependencies: list[type] = [RendererFrame]

    def __init__(
        self,
        path: pathlib.Path,
        lenght: tuple[int, int],
        spacing: tuple[int, int] = (0, 0),
        padding: tuple[int, int] = (0, 0),
    ) -> None:
        super().__init__()
        self._path: pathlib.Path = path
        self._img: pygame.Surface = pygame.image.load(self._path)
        self._lenght: tuple[int, int] = lenght
        self._spacing: tuple[int, int] = spacing
        self._padding: tuple[int, int] = padding
        self._imgs: list[list[pygame.Surface]] = []

        spr_width: int = (
            self.img.get_width() - self.padding[0] - (self.lenght[0] * self.spacing[0])
        ) // self.lenght[0]
        spr_height: int = (
            self.img.get_height() - self.padding[1] - (self.lenght[1] * self.spacing[1])
        ) // self.lenght[1]

        for row in range(self._lenght[1]):
            self._imgs.append([])
            for col in range(self._lenght[0]):
                x = (col * spr_width) + (col * self._spacing[1]) + self._padding[1]
                y = (row * spr_height) + (row * self._spacing[0]) + self._padding[0]
                self._imgs[row].append(
                    self._img.subsurface(
                        (x, y, spr_width, spr_height)
                    )
                )

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

    @property
    def lenght(self) -> tuple[int, int]:
        return self._lenght

    @lenght.setter
    def lenght(self, value: tuple[int, int]) -> None:
        self._lenght = value

    @property
    def spacing(self) -> tuple[int, int]:
        return self._spacing

    @spacing.setter
    def spacing(self, value: tuple[int, int]) -> None:
        self._spacing = value

    @property
    def padding(self) -> tuple[int, int]:
        return self._padding

    @padding.setter
    def padding(self, value: tuple[int, int]) -> None:
        self._padding = value

    def to_json(self) -> dict[str, Any]:
        return {
            "path": str(self._path),
            "lenght": self._lenght,
            "spacing": self._spacing,
            "padding": self._padding,
        }
        
    def get(self, x: int, y: int) -> pygame.Surface:
        return self._imgs[y][x]

    def __repr__(self):
        return f"{super().__repr__()}({self._path}, {self._lenght}, {self._spacing}, {self._padding})"
