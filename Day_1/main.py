from typing import List, Tuple
from utils.types import Solution
from utils.timing import runtime

Direction = str
Offset = int

@runtime
def solve() -> Solution:
    with open("Day_1/input.txt") as file:
        instructions: List[Tuple[Direction, Offset]] = [(a[0], int(a[1:])) for a in [i.strip() for i in file.readlines()]]

        p1 = p2 = 50
        return sum((p1 := (p1 + (offset if direction == "R" else -offset)) % 100) == 0 for direction, offset in instructions), \
        sum((p2 := (p2 + (1 if direction == "R" else -1)) % 100) == 0 for direction, offset in instructions for _ in range(offset))


if __name__ == '__main__':
    p1, p2 = solve()
    print("Part 1:", p1)
    print("Part 2:", p2)