from PIL import Image
from maze_generator.maze import Maze


COEFF_OF_SCALING = 10
WALL_COLOR = (0, 0, 0)  # black
EMPTY_FIELD_COLOR = (255, 255, 255)  # white
START_AND_STOP_FIELD_COLOR = (255, 0, 0)  # red
SOLUTION_FIELD_COLOR = (0, 255, 0)  # green


class MazeDrawer:
    """"""

    def __init__(self, heigth: int, width: int):
        self._heigth = heigth * COEFF_OF_SCALING
        self._width = width * COEFF_OF_SCALING

        self.img = Image.new(mode="RGB", size=(self._width, self._heigth))
        self.pixels = self.img.load()

    def __fill_maze_elem(
        self, x1: int, y1: int, x2: int, y2: int, color: tuple
    ) -> None:
        while y1 <= y2:
            x = x1
            while x <= x2:
                self.pixels[x, y1] = color
                x += 1
            y1 += 1

    def draw_maze(self, maze: Maze, filepath: str, solved: bool) -> None:
        for maze_line in range(maze.height):
            for maze_column in range(maze.width):
                if maze.elem_is_wall(y=maze_line, x=maze_column):
                    color = WALL_COLOR
                elif maze.elem_is_start_stop(y=maze_line, x=maze_column):
                    color = START_AND_STOP_FIELD_COLOR
                elif maze.elem_is_way(y=maze_line, x=maze_column) and solved:
                    color = SOLUTION_FIELD_COLOR
                else:
                    color = EMPTY_FIELD_COLOR

                self.__fill_maze_elem(
                    x1=maze_column * COEFF_OF_SCALING,
                    y1=maze_line * COEFF_OF_SCALING,
                    x2=maze_column * COEFF_OF_SCALING + COEFF_OF_SCALING - 1,
                    y2=maze_line * COEFF_OF_SCALING + COEFF_OF_SCALING - 1,
                    color=color,
                )

        self._save_to_file(filepath)

    def _save_to_file(self, filepath: str) -> None:
        self.img.save(filepath + ".jpg", "JPEG")
