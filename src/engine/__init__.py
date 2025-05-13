from .core.components.render.sprite_renderer import SpriteRenderer
from .core.components.render.sprite_sheet import SpriteSheet
from .core.file_manager import FileManager


def set_root(root: str) -> None:
    SpriteRenderer.root_dir = root
    SpriteSheet.root_dir = root
    FileManager.root_dir = root
