from PIL import Image
from labyrinth import Labyrinth


# size = 1280, 1280


# img = Image.new(mode='RGB', size=size)
# img.save('out', 'JPEG')


COEFF_OF_SCALING = 10
WALL_COLOR = (0, 0, 0) # black
EMPTY_FIELD_COLOR = (255, 255, 255) # white


class LabyrinthDrawer:
    """"""

    def __init__(self, heigth: int, width: int):
        self._heigth = heigth * COEFF_OF_SCALING
        self._width = width * COEFF_OF_SCALING

        self.img = Image.new(mode='RGB', size=(self._width, self._heigth))
        self.pixels = self.img.load()

    def _fill_labyr_elem(self, x1: int, y1: int, x2: int, y2: int, color: tuple) -> None:
        while y1 <= y2:
            x = x1
            while x <= x2:
                self.pixels[x, y1] = color
                x += 1
            y1 += 1

    def draw_labyr(self, labyrinth: Labyrinth ,filepath: str) -> None:
        for labyr_line in range(labyrinth.heigth):
            for labyr_column in range(labyrinth.width):
                if labyrinth.elem_is_wall(y=labyr_line, x=labyr_column):
                    color = WALL_COLOR
                else:
                    color = EMPTY_FIELD_COLOR

                self._fill_labyr_elem(x1=labyr_column * COEFF_OF_SCALING,
                                      y1=labyr_line * COEFF_OF_SCALING,
                                      x2=labyr_column * COEFF_OF_SCALING + COEFF_OF_SCALING - 1,
                                      y2=labyr_line * COEFF_OF_SCALING + COEFF_OF_SCALING - 1,
                                      color=color)


        self._save_to_file(filepath)

    def _save_to_file(self, filepath: str) -> None:
        self.img.save(filepath + '.jpg', 'JPEG')
