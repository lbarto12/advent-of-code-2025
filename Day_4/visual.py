from typing import List

import time
import visual_tools.screen as screen

from Day_4.main import forklift

with open("Day_4/input.txt") as file:
    lines: List[List[chr]] = [list(i.strip()) for i in file.readlines()]

    screen.clear()
    print(*[''.join(i) for i in lines], sep='\n')

    res: int = 0
    while True:
        time.sleep(.1)

        count, remove = forklift(lines)
        if not remove:
            break

        res += count

        for x, y in remove:
            screen.print_at(x, y, screen.colored("x", screen.bcolors.RED))
        
        time.sleep(.1)

        for x, y in remove:
            lines[y][x] = '.'

        for x, y in remove:
            screen.print_at(x, y, ".")

    input()