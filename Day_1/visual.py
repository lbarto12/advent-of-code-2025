from typing import List, Tuple
import time

import visual_tools.screen as screen

Direction = str
Offset = int

with open("Day_1/input.txt") as file:
    instructions: List[Tuple[Direction, Offset]] = [(a[0], int(a[1:])) for a in [i.strip() for i in file.readlines()]]

    r: List[str] = [str(i) if len(str(i)) == 2 else str(i) + ' ' for i in range(100)]

    pos: int = 50
    for direction, offset in instructions:
        screen.clear()
        print('|'.join(r))
        screen.print_at(pos * 3, 1, "^")
        for _ in range(offset):
            screen.print_at(pos * 3, 1, " ")
            pos += (-1 if direction == "L" else 1)
            pos %= 100
            screen.print_at(pos * 3, 1, "^")
            time.sleep(.05)
        screen.print_at(pos * 3, 1, "CLICK!")
        time.sleep(1)
    
    input()

