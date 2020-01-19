""""""
from random import randint

from labyr_elem import LabyrinthElem
from stack import Stack

WALL_ELEM = 'x'
EMPTY_ELEM = ' '


class Labyrinth:
    """"""

    def __init__(self, width: int, heigth: int):
        self._width = width 
        self._heigth = heigth

        self._labyrinth = []

    @property
    def width(self):
        return self._width
    
    @property
    def heigth(self):
        return self._heigth

    def _make_walls(self) -> None:
        # create and fill (if neccessary) lines of matrix
        for line in range(self._heigth):
            if line % 2 == 0:
                self._labyrinth.append([LabyrinthElem(WALL_ELEM) for elem in range(self._width)])
            else:
                self._labyrinth.append([LabyrinthElem(EMPTY_ELEM) for elem in range(self._width)])

        # fill (if necessary) columns of matrix
        for column in range(self._width):
            if column % 2 == 0:
                for line in range(self._heigth):
                    self._labyrinth[line][column] = LabyrinthElem(WALL_ELEM)

    def _check_is_visited(self, y: int, x: int) -> bool:
        if x <= 0 or y <= 0 or x >= self.width - 1 or y >= self.heigth - 1:
            return True
        else:
            return True if self._labyrinth[y][x].is_visited else False

    def _create_list_of_not_visited_neighbors_of_point(self, y: int, x: int) -> list:
        result = []
        if not self._check_is_visited(y - 2, x):
            result.append((y - 2, x))
        if not self._check_is_visited(y + 2, x):
            result.append((y + 2, x))
        if not self._check_is_visited(y, x - 2):
            result.append((y, x - 2))
        if not self._check_is_visited(y, x + 2):
            result.append((y, x + 2))

        return result

    def _create_labyr(self) -> None:
        # start values of x,y
        # y, x = int(self._heigth / 2), int(self._width / 2)
        y, x = 1, 1        
        
        stack = Stack()
        stack.push((y, x))

        while True:
            if stack.is_empty():
                # all of points were visited
                break

            y, x = stack.top()

            # mark current point as visited
            self._labyrinth[y][x].is_visited = True

            not_visited_neighbors = self._create_list_of_not_visited_neighbors_of_point(y, x)
            if not not_visited_neighbors:
                # visited neighbors of curr point aren't exist
                stack.pop()
                continue

            # random select of was not visited neighbor
            random_neighbor = randint(0, len(not_visited_neighbors) - 1)
            y_neighbor, x_neighbor = not_visited_neighbors[random_neighbor]

            # break wall between current point and selected neighbor
            y_break, x_break = int((y + y_neighbor) / 2), int((x + x_neighbor) / 2)
            self._labyrinth[y_break][x_break].meta_symbol = EMPTY_ELEM
            self._labyrinth[y_break][x_break].is_visited = True

            stack.push((y_neighbor, x_neighbor))

    def create(self) -> None:
        self._make_walls()
        self._create_labyr()

    def elem_is_wall(self, y: int, x: int) -> bool:
        return True if self._labyrinth[y][x].meta_symbol == WALL_ELEM else False
