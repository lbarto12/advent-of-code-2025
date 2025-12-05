from typing import List

import time
from visual_tools.screen import print_at, clear, colored, bcolors

from Day_4.main import forklift

with open("Day_4/input.txt") as file:
    lines: List[List[chr]] = [list(i.strip()) for i in file.readlines()]

    clear()
    print(*[''.join(i) for i in lines], sep='\n')

    res: int = 0
    while True:
        time.sleep(.1)

        count, remove = forklift(lines)
        if not remove:
            break

        res += count

        for x, y in remove:
            print_at(x, y, colored("x", bcolors.RED))
        
        time.sleep(.1)

        for x, y in remove:
            lines[y][x] = '.'

        for x, y in remove:
            print_at(x, y, ".")

    input()