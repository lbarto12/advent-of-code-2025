from typing import List, Tuple, Any, Iterable, Generator, Dict
from utils.types import Position

def t_add(*args) -> Tuple[Any, ...]:
    if not len({len(i) for i in args}) == 1:
        raise "Tuple Length Mismatch"
    return tuple(sum(a[i] for a in args) for i in range(len(args[0])))

def t_sub(a: Tuple[Any, ...], b: Tuple[Any, ...]) -> Tuple[Any, ...]:
    if not len(a) == len(b):
        raise "Tuple Length Mismatch"
    return tuple(a[0] - b[0], a[1] - b[1])

def transpose(mtx: Iterable[Iterable[Any]]) -> List[Tuple[Any, ...]]:
    return list(zip(*mtx))

def adjacent(x: int, y: int) -> Generator[None, None, Tuple[int, int]]:
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (i, j) == (0, 0):
                continue
            yield (x + j, y + i)

def at(arr: Iterable[Iterable[Any]], pos: Position) -> Any:
    return arr[pos[1]][pos[0]] # assuming x, y coordinates

def set_at(arr: Iterable[Iterable[Any]], pos: Position, item: Any) -> Any:
    arr[pos[1]][pos[0]] = item
    return item

class DisjointSetUnion:
    def __init__(self, items: List[Any]):
        self.parent: Dict[Any, Any] = {i: i for i in items}
        self.sizes = {i: 1 for i in items}
        self.size = len(items)

    def find(self, i: Any) -> Any:
        if self.parent[i] == i:
            return i
        return self.find(self.parent[i])

    def union(self, i: Any, j: Any) -> None:
        if self.find(i) != self.find(j):
            self.parent[a := self.find(i)] = (b := self.find(j))
            self.sizes[b] += self.sizes[a]
            self.sizes[a] = 0
            self.size -= 1

    def len(self, i: Any) -> int:
        return self.sizes[self.find(i)]
    
    def __iter__(self):
        return list(set(self.find(i) for i in self.parent.keys())).__iter__()

    def __len__(self) -> int:
        return self.size