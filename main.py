from core import Game, FileManager, Scene
from core import Object, components


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
        components.SpriteSheet("assets/chara.png", (4, 3), (1, 1), (0, 0))
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
    return player


def create_camera():
    camera = Object()
    camera.add_component(components.Transform((0, 0), 0.0, (1, 1)))
    camera.add_component(components.Tag("camera"))
    camera.add_component(components.Active(True))
    camera.add_component(components.Follow("player"))
    return camera


def create_box(pos):
    box = Object()
    box.add_component(components.Transform(pos, 180, (0.5, 0.5)))
    box.add_component(components.Active(True))
    box.add_component(components.RendererFrame(100, 100))
    box.add_component(components.SpriteRenderer("assets/player.png"))
    return box


if __name__ == "__main__":
    game = Game()

    main_scn = Scene()

    # Add objects to the scene
    main_scn.add_obj(create_controller())
    main_scn.add_obj(create_chara())

    import random

    for i in range(20):
        pos = (random.randint(-1000, 1000), random.randint(-1000, 1000))
        main_scn.add_obj(create_box(pos))

    main_scn.add_obj(create_camera())

    # Save the scene
    FileManager.save_scene(main_scn, "main_scn")

    # Load scene from file if needed
    main_scn = Scene.from_json(FileManager.load_scene("main_scn"))

    game.scenes["main"] = main_scn
    game.active_scene = "main"

    game.run()
