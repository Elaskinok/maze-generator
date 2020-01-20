""""""
from random import randint

from labyr_generator.labyr_elem import LabyrinthElem
from labyr_generator.stack import Stack

WALL_ELEM = 'x'
EMPTY_ELEM = ' '
START_ELEM = 't'
STOP_ELEM = 'p'
SOLUTION_ELEM = 'w'


class Labyrinth:
    """"""

    _is_created = False

    def __init__(self, width: int, heigth: int):
        self._width = width 
        self._heigth = heigth

        self._labyrinth = []
        self._make_walls()

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

    def _create_list_of_not_visited_neighbors_of_point(self, y: int, x: int, distance: int) -> list:
        """distance: int. This argument is count of steps between current point and neighbor."""
        result = []
        if not self._check_is_visited(y - distance, x):
            result.append((y - distance, x))
        if not self._check_is_visited(y + distance, x):
            result.append((y + distance, x))
        if not self._check_is_visited(y, x - distance):
            result.append((y, x - distance))
        if not self._check_is_visited(y, x + distance):
            result.append((y, x + distance))

        return result

    def _create_labyr(self) -> None:
        # start values of x,y
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

            not_visited_neighbors = self._create_list_of_not_visited_neighbors_of_point(y, x, distance=2)
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

    def _set_start_and_stop_elems(self):
        self._labyrinth[1][1].meta_symbol = START_ELEM
        self._labyrinth[self._heigth - 2][self._width - 2].meta_symbol = STOP_ELEM

    def _set_labyrinth_as_not_visited(self):
        for line in range(self._heigth):
            for column in range(self._width):
                if self._labyrinth[line][column].meta_symbol == WALL_ELEM:
                    self._labyrinth[line][column].is_visited = True
                else:
                    self._labyrinth[line][column].is_visited = False

    def _solve_labyr(self) -> None:
        stack = Stack()
        stack.push((1, 1))
        # if start element is not at (1, 1) - function of find start must be implemented

        while True:
            y, x = stack.top()
            
            if self._labyrinth[y][x].meta_symbol == STOP_ELEM:
                break

            # mark current point as visited
            self._labyrinth[y][x].is_visited = True
            self._labyrinth[y][x].meta_symbol = SOLUTION_ELEM

            not_visited_neighbors = self._create_list_of_not_visited_neighbors_of_point(y, x, distance=1)

            if not not_visited_neighbors:
                self._labyrinth[y][x].meta_symbol = EMPTY_ELEM
                stack.pop()
                continue

            for neighbor in not_visited_neighbors:
                y_neighbor, x_neighbor = neighbor
                symbol = self._labyrinth[y_neighbor][x_neighbor].meta_symbol
                if symbol != WALL_ELEM and symbol != SOLUTION_ELEM:
                    # not visited neighbor was found
                    stack.push((y_neighbor, x_neighbor))
                    break

    def create(self) -> None:
        """This method generates a labyrinth."""
        self._create_labyr()
        self._set_start_and_stop_elems()

        self._is_created = True
        self._set_labyrinth_as_not_visited()

    def solve(self) -> None:
        """This method generates a solution of EXISTING labyrinth.
        Before call this method you have to call 'create'."""
        if self._is_created:
            self._solve_labyr()
            self._set_start_and_stop_elems()

    def elem_is_wall(self, y: int, x: int) -> bool:
        return True if self._labyrinth[y][x].meta_symbol == WALL_ELEM else False

    def elem_is_start_stop(self, y: int, x: int) -> bool:
        return True if self._labyrinth[y][x].meta_symbol == START_ELEM\
                        or self._labyrinth[y][x].meta_symbol == STOP_ELEM else False

    def elem_is_way(self, y: int, x: int) -> bool:
        return True if self._labyrinth[y][x].meta_symbol == SOLUTION_ELEM else False
