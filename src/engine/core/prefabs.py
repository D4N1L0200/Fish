from typing import Callable
from .game import Game
from .object import Object


class Prefabs:
    prefabs: dict[str, Callable] = {}
    game: Game | None = None

    @classmethod
    def link_game(cls, game: Game) -> None:
        cls.game = game

    @classmethod
    def add_prefab(cls, name: str, obj: Callable) -> None:
        cls.prefabs[name] = obj

    @classmethod
    def spawn(cls, scn_name: str, obj_name: str) -> Object:
        if cls.game is None:
            raise Exception("Game not linked")

        if scn_name not in cls.game.scenes:
            raise Exception(f"Scene '{scn_name}' not found")

        if obj_name not in cls.prefabs:
            raise Exception(f"Prefab '{obj_name}' not found")

        obj = cls.prefabs[obj_name]()
        cls.game.scenes[scn_name].add_obj(obj)
        return obj
