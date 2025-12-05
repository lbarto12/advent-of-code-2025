from typing import List

import visual_tools.screen as screen
import time

from Day_3.main import max_and_location


with open("Day_3/input.txt") as file:
    lines: List[str] = [i.strip() for i in file.readlines()]
    
    c = screen.ColorAlternator()

    j2: int = 0
    for line in lines:
        screen.clear()
        screen.print_at(0, 0, line)
        screen.print_at(0, 2, "total: " + screen.colored(j2, screen.bcolors.OKGREEN))
        time.sleep(1)

        constructed, boundary = '', 0
        for i in range(-11, 1):
            screen.print_at(boundary, 0, c(line[boundary:i] if i else line[boundary:]))
            time.sleep(.2)
            nxt, idx = max_and_location(line[boundary:i] if i else line[boundary:])
            screen.print_at(boundary, 0, "-" * idx)
            time.sleep(.2)
            boundary += idx + 1
            constructed += nxt
        j2 += int(constructed)
        screen.print_at(boundary, 0, "-" * (len(line) - boundary))
        time.sleep(.2)
        screen.print_at(0, 1, "adding: " + screen.colored(constructed, screen.bcolors.OKGREEN))
        time.sleep(1)

    input()