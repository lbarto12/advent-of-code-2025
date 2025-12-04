from typing import List, Tuple
import time

from visual_tools.screen import clear, print_at

Direction = str
Offset = int

with open("Day_1/input.txt") as file:
    instructions: List[Tuple[Direction, Offset]] = [(a[0], int(a[1:])) for a in [i.strip() for i in file.readlines()]]

    r: List[str] = [str(i) if len(str(i)) == 2 else str(i) + ' ' for i in range(100)]

    pos: int = 50
    for direction, offset in instructions:
        clear()
        print('|'.join(r))
        print_at(pos * 3, 1, "^")
        for _ in range(offset):
            print_at(pos * 3, 1, " ")
            pos += (-1 if direction == "L" else 1)
            pos %= 100
            print_at(pos * 3, 1, "^")
            time.sleep(.05)
        print_at(pos * 3, 1, "CLICK!")
        time.sleep(1)

