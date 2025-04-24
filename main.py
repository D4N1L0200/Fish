from core import Game, FileManager, Scene
from core import Object, components


def create_herick(pos):
    player = Object()
    player.add_component(components.Transform(pos, 0.0, (1, 1)))
    player.add_component(components.Tag("player"))
    player.add_component(components.Active(True))
    player.add_component(components.RendererFrame(100, 100))
    player.add_component(components.SpriteRenderer("assets/player.png"))
    player.add_component(components.MovementTester())
    player.add_component(components.RotationTester())
    player.add_component(components.ScaleTester())
    return player


def create_chara(pos):
    player = Object()
    player.add_component(components.Transform(pos, 0.0, (1, 1)))
    player.add_component(components.Tag("player"))
    player.add_component(components.Active(True))
    player.add_component(components.RendererFrame(100, 100))
    player.add_component(components.SpriteRenderer("assets/chara.png"))
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
    main_scn.add_obj(create_chara((100, 100)))
    main_scn.add_obj(create_box((0, 0)))
    main_scn.add_obj(create_camera())

    # Save the scene
    FileManager.save_scene(main_scn, "main_scn")

    # Load scene from file if needed
    # main_scn = Scene.from_json(FileManager.load_scene("main_scn"))

    game.scenes["main"] = main_scn
    game.active_scene = "main"

    game.run()
