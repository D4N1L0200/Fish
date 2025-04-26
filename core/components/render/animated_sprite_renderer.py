import pygame
import time
from typing import Any
from ..component import Component
from .renderer_frame import RendererFrame
from .sprite_sheet import SpriteSheet


class AnimatedSpriteRenderer(Component):
    dependencies: list[type] = [RendererFrame, SpriteSheet]

    def __init__(self, sprites: list[tuple[int, int]], fps: int) -> None:
        super().__init__()
        self._sprites: list[tuple[int, int]] = sprites
        self._idx: int = 0
        self._fps: int = fps
        self._img: pygame.Surface | None = None
        self._init_time: float = time.time()

    @property
    def sprites(self) -> list[tuple[int, int]]:
        return self._sprites

    @sprites.setter
    def sprites(self, value: list[tuple[int, int]]):
        self._sprites = value

    @property
    def idx(self) -> int:
        return self._idx

    @idx.setter
    def idx(self, value: int):
        self._idx = value

    @property
    def fps(self) -> int:
        return self._fps

    @fps.setter
    def fps(self, value: int):
        self._fps = value

    @property
    def img(self) -> pygame.Surface | None:
        return self._img

    @img.setter
    def img(self, value: pygame.Surface) -> None:
        self._img = value

    def update(self, dt: float) -> None:
        if time.time() - self._init_time >= 1 / self._fps:
            self._init_time = time.time()
            self._idx = (self._idx + 1) % len(self._sprites)

        if self.parent is None:
            return

        sprite_sheet: Component = self.parent.get_components("spritesheet")[0]

        if isinstance(sprite_sheet, SpriteSheet):
            self._img = sprite_sheet.get(*self._sprites[self._idx])

    def to_json(self) -> dict[str, Any]:
        return {"sprites": self._sprites, "fps": self._fps}

    def __repr__(self):
        return f"{super().__repr__()}({self._path})"
