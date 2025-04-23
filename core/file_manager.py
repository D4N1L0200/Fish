import json
from .scene import Scene


class FileManager:
    @classmethod
    def save_scene(cls, scene: Scene, scn_name: str) -> None:
        path: str = f"data/scenes/{scn_name}.json"
        scn_json: dict = scene.to_json()

        with open(path, "w") as f:
            json.dump(scn_json, f, indent=4)

    @classmethod
    def load_scene(cls, scn_name: str) -> dict:
        path: str = f"data/scenes/{scn_name}.json"

        with open(path, "r") as f:
            return json.load(f)
