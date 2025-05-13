import os
import sys
import json
import subprocess
import datetime

SRC_DIR: str = os.path.dirname(__file__)
GAMES_DIR: str = os.path.join(SRC_DIR, "games")

REQUIRED_DIRS: list[str] = [
    "data",
    "data/scenes",
    "assets",
    "assets/sprites",
]

META_JSON_TEMPLATE: dict = {
    "name": "Untitled",
    "clean_name": "untitled",
    "description": "No description",
    "executable": "main.py",
    "version": "0.0.1",
    "author": "Anonymous",
    "created_on": None,
    "last-run": None,
    "times-run": 0,
}

MAIN_PY_TEMPLATE: str = """import os
from engine import set_root
from engine.core import Game, FileManager, Scene


def main():
    game = Game()

    main_scn = Scene()

    FileManager.save_scene(main_scn, "main_scn")

    game.scenes["main"] = main_scn
    game.active_scene = "main"

    game.run()


if __name__ == "__main__":
    set_root(os.path.dirname(os.path.abspath(__file__)))
    main()
"""


def create_game() -> None:
    name: str = input("Enter a name for the game: ").strip()
    clean_name: str = name.replace(" ", "_").lower()
    path: str = os.path.join(GAMES_DIR, clean_name)

    if os.path.exists(path):
        print(f"Game {name} already exists")
        return

    os.makedirs(path)

    for subdir in REQUIRED_DIRS:
        os.makedirs(os.path.join(path, subdir))

    meta: dict = META_JSON_TEMPLATE.copy()
    meta["name"] = name
    meta["clean_name"] = clean_name
    meta["created_on"] = str(datetime.datetime.now())

    with open(os.path.join(path, "meta.json"), "w") as f:
        json.dump(meta, f, indent=4)

    with open(os.path.join(path, "main.py"), "w") as f:
        f.write(MAIN_PY_TEMPLATE)

    print(f"Game '{name}' created successfully")


def load_games() -> list[dict]:
    games: list[dict] = []
    for folder in os.listdir(GAMES_DIR):
        game_path: str = os.path.join(GAMES_DIR, folder)
        meta_path: str = os.path.join(game_path, "meta.json")

        if os.path.isdir(game_path) and os.path.isfile(meta_path):
            with open(meta_path, "r") as f:
                meta: dict = json.load(f)
                games.append(meta)

    return games


def choose_game(games: list[dict]) -> dict:
    print("Available games:")

    for i, game in enumerate(games):
        print(f"{i+1}. {game['name']}")

    choice: int = int(input("Choose a game: "))
    return games[int(choice) - 1]


def run_game(game: dict) -> None:
    game["last-run"] = str(datetime.datetime.now())
    game["times-run"] += 1

    game_path = os.path.join(GAMES_DIR, game["clean_name"])

    with open(os.path.join(game_path, "meta.json"), "w") as f:
        json.dump(game, f, indent=4)

    env = os.environ.copy()
    env["PYTHONPATH"] = os.path.abspath(".") + os.pathsep + env.get("PYTHONPATH", "")

    src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "."))

    subprocess.run(
        [sys.executable, os.path.join(game_path, game["executable"])],
        cwd=src_path,
        env=env,
    )


def main() -> None:
    while True:
        print("\n1. Run a game")
        print("2. Create a new game")
        print("3. Exit")
        choice: str = input("Choice: ")
        print()

        if choice == "1":
            games: list[dict] = load_games()

            if not games:
                print("No valid games found")
                continue

            game = choose_game(games)
            run_game(game)
            break
        elif choice == "2":
            create_game()
        elif choice == "3":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
