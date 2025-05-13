from typing import Any
from ..component import Component


class Transform(Component):
    def __init__(
        self,
        position: tuple[float, float] = (0.0, 0.0),
        rotation: float = 0.0,
        scale: tuple[float, float] = (1.0, 1.0),
    ) -> None:
        super().__init__()
        self._position: tuple[float, float] = position
        self._rotation: float = rotation
        self._scale: tuple[float, float] = scale

    @property
    def position(self) -> tuple[float, float]:
        return self._position

    @position.setter
    def position(self, value: tuple[float, float]) -> None:
        self._position = value

    @property
    def rotation(self) -> float:
        return self._rotation

    @rotation.setter
    def rotation(self, value: float) -> None:
        self._rotation = value % 360

    @property
    def scale(self) -> tuple[float, float]:
        return self._scale

    @scale.setter
    def scale(self, value: tuple[float, float]) -> None:
        self._scale = value

    def to_json(self) -> dict[str, Any]:
        return {
            "position": self._position,
            "rotation": self._rotation,
            "scale": self._scale,
        }

    def __repr__(self):
        return (
            f"{super().__repr__()}({self._position}, {self._rotation}, {self._scale})"
        )
