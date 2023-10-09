import argparse
import os
from maze_generator.maze import Maze
from maze_generator.maze_drawer import MazeDrawer


RESULT_FOLDER_NAME = "maze_gen_results"


def create_args_parser() -> argparse.ArgumentParser:
    """Func which creates parser of arguments of command-line.
    Return: argparse.ArgumentParser
    """
    parser = argparse.ArgumentParser(description="Maze-generator script.")
    return parser


def add_args(parser: argparse.ArgumentParser) -> None:
    """Func which takes parser and add arguments."""
    parser.add_argument("height", type=int, help="[ODD Integer] Height of the Maze.")
    parser.add_argument("width", type=int, help="[ODD Integer] Width of the Maze.")


def main():
    parser = create_args_parser()
    add_args(parser)
    args = parser.parse_args()

    width = args.width
    height = args.height

    if width % 2 == 0 or height % 2 == 0:
        parser.parse_args(["-h"])
    elif width < 5 or height < 5:
        print("Ha! You are joker ;)")
        return

    maze = Maze(width=width, height=height)
    maze.create()
    maze.solve()

    if not os.path.exists(RESULT_FOLDER_NAME):
        os.mkdir(RESULT_FOLDER_NAME)

    # draw maze into jpg file
    drawer = MazeDrawer(width=width, heigth=height)
    drawer.draw_maze(maze=maze, filepath=RESULT_FOLDER_NAME + "/maze", solved=False)
    drawer.draw_maze(
        maze=maze,
        filepath=RESULT_FOLDER_NAME + "/solved_maze",
        solved=True,
    )


if __name__ == "__main__":
    main()
