from typing import Any
from ..component import Component


class Follow(Component):
    # Makes a Transform follow another
    def __init__(self, follow_tag: str):
        super().__init__()
        self.follow_tag: str = follow_tag

    def update(self, dt: float) -> None:
        if self.parent is None or self.parent.scene is None:
            return

        positions: list[tuple[int, int]] = []
        for o in self.parent.scene.search(self.follow_tag):
            positions.append(o.transform.position)

        if len(positions) < 1:
            raise Exception(f"Could not find object with tag {self.follow_tag}")

        goal: tuple[int, int] = (0, 0)

        if len(positions) == 1:
            goal = self.parent.transform.position = positions[0]
        else:
            for p in positions:
                goal = (goal[0] + p[0], goal[1] + p[1])
            goal = (int(goal[0] / len(positions)), int(goal[1] / len(positions)))

        self.parent.transform.position = goal

    def to_json(self) -> dict[str, Any]:
        return {"follow_tag": self.follow_tag}
