import pygame
from typing import Any
from ..component import Component


class RendererFrame(Component):
    required_dependencies: list[str] = ["Transform", "SpriteRenderer | AnimatedSpriteRenderer"]

    def __init__(self, width: int, height: int) -> None:
        super().__init__()
        self._width: int = width
        self._height: int = height

    @property
    def width(self) -> int:
        return self._width

    @width.setter
    def width(self, value: int) -> None:
        self._width = value

    @property
    def height(self) -> int:
        return self._height

    @height.setter
    def height(self, value: int) -> None:
        self._height = value

    def draw(self, surface: pygame.Surface) -> None:
        if self.parent is None or self.parent.scene is None:
            return

        from ..render.sprite_renderer import SpriteRenderer
        from ..render.animated_sprite_renderer import AnimatedSpriteRenderer

        world_pos = self.parent.transform.position

        camera_pos = self.parent.scene.search("camera")[0].transform.position
        pos = (world_pos[0] - camera_pos[0], world_pos[1] - camera_pos[1])
        pos = (pos[0] + surface.get_width() / 2, pos[1] + surface.get_height() / 2)

        rot = self.parent.transform.rotation
        sx, sy = self.parent.transform.scale
        s_width = max(0, int(self.width * sx))
        s_height = max(0, int(self.height * sy))

        temp_surf = pygame.Surface((s_width, s_height), pygame.SRCALPHA)

        animatedspriterenderers: list[Component] = self.parent.get_components(
            "animatedspriterenderer"
        )

        if animatedspriterenderers != []:
            for animatedspriterenderer in animatedspriterenderers:
                if isinstance(animatedspriterenderer, AnimatedSpriteRenderer):
                    if animatedspriterenderer.img is None:
                        continue

                    base_img = pygame.transform.scale(
                        animatedspriterenderer.img, (s_width, s_height)
                    )
                    temp_surf.blit(base_img, (0, 0))
        else:
            spriterenderers: list[Component] = self.parent.get_components(
                "spriterenderer"
            )

            if spriterenderers != []:
                for spriterenderer in spriterenderers:
                    if isinstance(spriterenderer, SpriteRenderer):
                        base_img = pygame.transform.scale(
                            spriterenderer.img, (s_width, s_height)
                        )
                        temp_surf.blit(base_img, (0, 0))

        rotated = pygame.transform.rotate(temp_surf, -rot)
        rect = rotated.get_rect(center=pos)
        surface.blit(rotated, rect)

    def to_json(self) -> dict[str, Any]:
        return {
            "width": self._width,
            "height": self._height,
        }

    def __repr__(self):
        return f"{super().__repr__()}({self._width}, {self._height})"
