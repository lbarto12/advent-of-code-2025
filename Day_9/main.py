
from typing import List, Tuple
from utils.types import Solution, Position
from shapely.geometry import Polygon

def area(a, b) -> int:
    return (max(a[0], b[0]) - min(a[0], b[0]) + 1) * (max(a[1], b[1]) - min(a[1], b[1]) + 1)

def is_valid(a, b, p) -> int:
    return p.covers(Polygon([a, (a[0], b[1]), b, (a[1], b[0])])) # preserve cycle hack

def solve() -> Solution:
    with open("Day_9/input.txt") as file:
        red_tiles: List[Position] = [tuple(map(int, i.strip().split(','))) for i in file.readlines()]
        pairs: List[Tuple[Position, Position]] = [(a, b) for i, a in enumerate(red_tiles) for b in red_tiles[i + 1:]]
        
        p = Polygon(red_tiles) # nice of them to provide puzzle input in cyclical order :)

        p1: int = max(area(*p) for p in pairs)
        p2: int = max(c for a, b in pairs if (c := area(a, b)) and is_valid(a, b, p))

        return p1, p2 


if __name__ == '__main__':
    p1, p2 = solve()
    print("Part 1:", p1)
    print("Part 2:", p2)

