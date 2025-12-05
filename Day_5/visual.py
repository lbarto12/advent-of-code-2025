from typing import List, Tuple, Callable
import re
import math
import time

import visual_tools.screen as screen

def create_range_converter(lower_bound: int, upper_bound: int, w: int = 800) -> Callable:
    def converter(n: int) -> int:
        rng: int = upper_bound - lower_bound
        ratio: float = (n - lower_bound) / rng
        new: int = int(ratio * w)
        return new
    return converter

with open("Day_5/input.txt") as file:
    lines: List[List[chr]] = [i.strip() for i in file.readlines()]
    ranges, ingredients = lines[:(split := lines.index(''))], map(int, lines[split + 1:])
    ranges: Tuple[int, int] = sorted([tuple(map(int, *re.findall(r'(\d+)-(\d+)', i))) for i in ranges])

    screen.clear()

    mn, mx = math.inf, 0
    [(mn := min(mn, l), mx := max(mx, r)) for l, r in ranges]

    con: Callable = create_range_converter(mn, mx)
    
    c = screen.ColorAlternator()
    write_y: int = len(ranges) + 1

    left, right = ranges[0]
    for i, (l, r) in enumerate(ranges):
        if l <= right:
            right = max(r, right)
        else:
            r_char: str = c("0")
            for write_x in range(con(left), con(right) + 1):
                for j in range(i + 1, write_y):
                    screen.print_at(write_x, j, r_char)
                time.sleep(.01)
            left, right = l, r


        for x in range(con(l), con(r) + 1):
            screen.print_at(x, i, "-")

    r_char: str = c("0")
    for write_x in range(con(left), con(right) + 1):
        for j in range(i + 1, write_y):
            screen.print_at(write_x, j, r_char)
        time.sleep(.01)

    input()