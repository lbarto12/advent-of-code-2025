from typing import List, Tuple, Set
from utils.types import Solution, Position

from utils.ds import adjacent

def forklift(floor: List[List[chr]]) -> Tuple[int, Set[Position]]:
    w, h = len(floor[0]), len(floor)
    valid: Set[Position] = set()
    result: int = 0
    for y, line in enumerate(floor):
            for x, c in enumerate(line):
                if c == "@" and sum(0 <= cx < w and 0 <= cy < h and floor[cy][cx] == "@" for cx, cy in adjacent(x, y)) < 4: # exclude self
                    result += 1
                    valid.add((x, y))
    return result, valid

def solve() -> Solution:
    with open("Day_4/input.txt") as file:
        room: List[List[chr]] = [list(i.strip()) for i in file.readlines()]

        p1, _ = forklift(room)

        p2: int = 0
        while True:
            count, remove = forklift(room)
            if not remove:
                break

            p2 += count

            for x, y in remove:
                room[y][x] = '.'
        
        return p1, p2

if __name__ == "__main__":
    p1, p2 = solve()
    print("Part 1:", p1)
    print("Part 2:", p2)