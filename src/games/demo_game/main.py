import os
from engine import set_root
from engine.core import Game, FileManager, Scene, Object, components, Prefabs, components


def main():
    print("Hello, World!")
    game = Game()

    main_scn = Scene()

    # Add objects to the scene
    main_scn.add_obj(create_controller())
    main_scn.add_obj(create_chara())

    Prefabs.add_prefab("box", create_box)
    Prefabs.link_game(game)

    main_scn.add_obj(create_camera())

    # Save the scene
    FileManager.save_scene(main_scn, "main_scn")

    # Load scene from file if needed
    main_scn = Scene.from_json(FileManager.load_scene("main_scn"))

    game.scenes["main"] = main_scn
    game.active_scene = "main"

    game.run()


def create_controller():
    controller = Object()
    controller.add_component(components.InputMapper())
    controller.add_component(components.Tag("controller"))
    controller.add_component(components.Active(True))
    return controller


def create_chara():
    player = Object()
    player.add_component(components.Transform((0, 0), 0.0, (19 / 20, 29 / 20)))
    player.add_component(components.Tag("player"))
    player.add_component(components.Active(True))
    player.add_component(components.RendererFrame(100, 100))
    player.add_component(
        components.SpriteSheet("assets/sprites/chara.png", (4, 3), (1, 1), (0, 0))
    )
    player.add_component(
        components.AnimatedSpriteRenderer([(0, 0), (1, 0), (2, 0), (3, 0)], 4)
    )  # down
    # player.add_component(
    #     components.AnimatedSpriteRenderer([(0, 1), (1, 1)], 4)
    # )  # left
    # player.add_component(
    #     components.AnimatedSpriteRenderer([(2, 1), (3, 1)], 4)
    # )  # right
    # player.add_component(
    #     components.AnimatedSpriteRenderer([(0, 2), (1, 2), (2, 2), (3, 2)], 4)
    # )  # up
    player.add_component(components.InputListener())
    player.add_component(components.MovementTester())
    player.add_component(components.RotationTester())
    player.add_component(components.ScaleTester())
    player.add_component(components.PrefabTester())
    return player


def create_camera():
    camera = Object()
    camera.add_component(components.Transform((0, 0), 0.0, (1, 1)))
    camera.add_component(components.Tag("camera"))
    camera.add_component(components.Active(True))
    camera.add_component(components.Follow("player"))
    return camera


def create_box():
    box = Object()
    box.add_component(components.Transform((0.0, 0.0), 180, (0.5, 0.5)))
    box.add_component(components.Active(True))
    box.add_component(components.RendererFrame(100, 100))
    box.add_component(components.SpriteRenderer("assets/sprites/player.png"))
    return box


if __name__ == "__main__":
    set_root(os.path.dirname(os.path.abspath(__file__)))
    main()
