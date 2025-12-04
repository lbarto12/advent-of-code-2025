from typing import List, Generator, Tuple, Set

def adjacent(x: int, y: int) -> Generator[None, None, Tuple[int, int]]:
    for i in range(-1, 2):
        for j in range(-1, 2):
            yield (x + j, y + i)

def forklift(floor: List[List[chr]]) -> Tuple[int, Set[Tuple[int, int]]]:
    w, h = len(floor[0]), len(floor)
    valid: Set[Tuple[int, int]] = set()
    result: int = 0
    for y, line in enumerate(floor):
            for x, c in enumerate(line):
                if c == "@" and sum(0 <= cx < w and 0 <= cy < h and floor[cy][cx] == "@" for cx, cy in adjacent(x, y)) <= 4: # exclude self
                    result += 1
                    valid.add((x, y))
    return result, valid

def solve():
    with open("input.txt") as file:
        lines: List[List[chr]] = [list(i.strip()) for i in file.readlines()]

        p1, _ = forklift(lines)

        p2: int = 0
        while True:
            count, remove = forklift(lines)
            if not remove:
                break

            p2 += count

            for x, y in remove:
                lines[y][x] = '.'
        
        print("Part 1:", p1)
        print("Part 2:", p2)

if __name__ == "__main__":
    solve()