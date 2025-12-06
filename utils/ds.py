from typing import List, Tuple, Any, Iterable, Generator

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