""""""


class LabyrinthElem:
    """"""

    def __init__(self, meta_symbol: str=' '):
        self._meta_symbol = meta_symbol
        self._visited = False

    is_visited = property()
    meta_symbol = property()

    @is_visited.getter
    def is_visited(self) -> bool:
        return self._visited

    @is_visited.setter
    def is_visited(self, value: bool) -> None:
        self._visited = value

    @meta_symbol.getter
    def meta_symbol(self) -> str:
        return self._meta_symbol

    @meta_symbol.setter
    def meta_symbol(self, value) -> None:
        self._meta_symbol = value
