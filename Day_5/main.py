from typing import List, Tuple
import re

def solve():
    with open("input.txt") as file:
        lines: List[List[chr]] = [i.strip() for i in file.readlines()]
        ranges, ingredients = lines[:(split := lines.index(''))], map(int, lines[split + 1:])
        ranges: Tuple[int, int] = sorted([tuple(map(int, *re.findall(r'(\d+)-(\d+)', i))) for i in ranges])

        p1: int = sum(any(l <= ingredient <= r for l, r in ranges) for ingredient in ingredients)
        
        p2, (left, right) = 0, ranges[0]
        for i, (l, r) in enumerate(ranges[1:]):
            if l <= right:
                right = max(r, right)
            else:
                p2 += right - left + 1
                left, right = l, r

        p2 += (right == r) * (right - left + 1)

        print("Part 1:", p1)
        print("Part 2:", p2)

if __name__ == '__main__':
    solve()