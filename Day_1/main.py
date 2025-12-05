from typing import List, Tuple

Direction = str
Offset = int

def solve():
    with open("input.txt") as file:
        instructions: List[Tuple[Direction, Offset]] = [(a[0], int(a[1:])) for a in [i.strip() for i in file.readlines()]]

        # Part 1
        p1: int = 50
        print("Part 1:", sum((p1 := (p1 + (offset if direction == "R" else -offset)) % 100) == 0 for direction, offset in instructions))

        # Part 2
        p2: int = 50
        print("Part 2:", sum((p2 := (p2 + (1 if direction == "R" else -1)) % 100) == 0 for direction, offset in instructions for _ in range(offset)))

if __name__ == '__main__':
    solve()