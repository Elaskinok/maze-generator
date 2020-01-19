import argparse
import logging
from labyrinth import Labyrinth
from labyr_drawer import LabyrinthDrawer


HEIGTH = 21
WIDTH = 21


def create_args_parser() -> argparse.ArgumentParser:
    """Func which creats parser of arguments of command-line.
    Return: argparse.ArgumentParser
    """
    parser = argparse.ArgumentParser(description='Labyrinth-generator script.')
    return parser



def add_args(parser: argparse.ArgumentParser) -> None:
    """Func which takes parser and add arguments."""
    parser.add_argument(
        'heigth',
        type=int,
        help='[ODD Integer] Heigth of labyrinth.'
    )
    parser.add_argument(
        'width',
        type=int,
        help='[ODD Integer] Width of labyrinth.'
    )


def main():
    parser = create_args_parser()
    add_args(parser)
    args = parser.parse_args()

    width = args.width
    heigth = args.heigth

    if width % 2 == 0 or heigth % 2 == 0:
        parser.parse_args(['-h'])
    elif width == 1 or heigth == 1:
        print('Ha! You are joker ;)')
        return

    # create labyrinth
    labyr = Labyrinth(width=width, heigth=heigth)
    labyr.create()

    # draw labyrinth into jpg file
    drawer = LabyrinthDrawer(width=width, heigth=heigth)
    drawer.draw_labyr(labyrinth=labyr, filepath='labyrinth')


if __name__ == '__main__':
    main()
