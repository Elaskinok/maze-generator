""""""
from random import randint

from maze_generator.maze_elem import MazeElem
from maze_generator.stack import Stack

WALL_ELEM = "x"
EMPTY_ELEM = " "
START_ELEM = "t"
STOP_ELEM = "p"
SOLUTION_ELEM = "w"


class Maze:
    """"""

    _is_created = False

    def __init__(self, width: int, height: int):
        self.__width = width
        self.__height = height

        self.__maze = []
        self._make_walls()

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    def _make_walls(self) -> None:
        # create and fill (if necessary) lines of matrix
        for line in range(self.__height):
            if line % 2 == 0:
                self.__maze.append(
                    [MazeElem(WALL_ELEM) for elem in range(self.__width)]
                )
            else:
                self.__maze.append(
                    [MazeElem(EMPTY_ELEM) for elem in range(self.__width)]
                )

        # fill (if necessary) columns of matrix
        for column in range(self.__width):
            if column % 2 == 0:
                for line in range(self.__height):
                    self.__maze[line][column] = MazeElem(WALL_ELEM)

    def _check_is_visited(self, y: int, x: int) -> bool:
        if x <= 0 or y <= 0 or x >= self.width - 1 or y >= self.height - 1:
            return True
        else:
            return True if self.__maze[y][x].is_visited else False

    def _create_list_of_not_visited_neighbors_of_point(
        self, y: int, x: int, distance: int
    ) -> list:
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

    def __create_maze(self) -> None:
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
            self.__maze[y][x].is_visited = True

            not_visited_neighbors = self._create_list_of_not_visited_neighbors_of_point(
                y, x, distance=2
            )
            if not not_visited_neighbors:
                # visited neighbors of curr point aren't exist
                stack.pop()
                continue

            # random select of was not visited neighbor
            random_neighbor = randint(0, len(not_visited_neighbors) - 1)
            y_neighbor, x_neighbor = not_visited_neighbors[random_neighbor]

            # break wall between current point and selected neighbor
            y_break, x_break = int((y + y_neighbor) / 2), int((x + x_neighbor) / 2)
            self.__maze[y_break][x_break].meta_symbol = EMPTY_ELEM
            self.__maze[y_break][x_break].is_visited = True

            stack.push((y_neighbor, x_neighbor))

    def _set_start_and_stop_elems(self):
        self.__maze[1][1].meta_symbol = START_ELEM
        self.__maze[self.__height - 2][self.__width - 2].meta_symbol = STOP_ELEM

    def __set_maze_as_not_visited(self):
        for line in range(self.__height):
            for column in range(self.__width):
                if self.__maze[line][column].meta_symbol == WALL_ELEM:
                    self.__maze[line][column].is_visited = True
                else:
                    self.__maze[line][column].is_visited = False

    def _solve_maze(self) -> None:
        stack = Stack()
        stack.push((1, 1))
        # if start element is not at (1, 1) - function of find start must be implemented

        while True:
            y, x = stack.top()

            if self.__maze[y][x].meta_symbol == STOP_ELEM:
                break

            # mark current point as visited
            self.__maze[y][x].is_visited = True
            self.__maze[y][x].meta_symbol = SOLUTION_ELEM

            not_visited_neighbors = self._create_list_of_not_visited_neighbors_of_point(
                y, x, distance=1
            )

            if not not_visited_neighbors:
                self.__maze[y][x].meta_symbol = EMPTY_ELEM
                stack.pop()
                continue

            for neighbor in not_visited_neighbors:
                y_neighbor, x_neighbor = neighbor
                symbol = self.__maze[y_neighbor][x_neighbor].meta_symbol
                if symbol != WALL_ELEM and symbol != SOLUTION_ELEM:
                    # not visited neighbor was found
                    stack.push((y_neighbor, x_neighbor))
                    break

    def create(self) -> None:
        """This method generates a maze."""
        self.__create_maze()
        self._set_start_and_stop_elems()

        self._is_created = True
        self.__set_maze_as_not_visited()

    def solve(self) -> None:
        """This method generates a solution of EXISTING maze.
        Before call this method you have to call 'create'."""
        if self._is_created:
            self._solve_maze()
            self._set_start_and_stop_elems()

    def elem_is_wall(self, y: int, x: int) -> bool:
        return True if self.__maze[y][x].meta_symbol == WALL_ELEM else False

    def elem_is_start_stop(self, y: int, x: int) -> bool:
        return (
            True
            if self.__maze[y][x].meta_symbol == START_ELEM
               or self.__maze[y][x].meta_symbol == STOP_ELEM
            else False
        )

    def elem_is_way(self, y: int, x: int) -> bool:
        return True if self.__maze[y][x].meta_symbol == SOLUTION_ELEM else False
