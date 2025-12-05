from typing import List
import time

import visual_tools.screen as screen

from Day_2.main import Range

with open("Day_2/input.txt") as file:
    ranges: List[Range] = [tuple(int(i) for i in r.split('-')) for r in file.read().split(',')]

    c = screen.ColorAlternator()
    
    for l, r in ranges:
        screen.clear()
        screen.print_at(0, 0, f"{l}-{r}")
        for i in range(l, r + 1):
            screen.print_at(0, 1, i)
            for seg in range((n := len(s := str(i))) // 2, 0, -1):
                if n  % seg:
                    continue
                for x in range(0, n, seg):
                    screen.print_at(x, 1, c(str(i)[x:x+seg]))
                if len(check := {s[x:x+seg] for x in range(0, n, seg)}) == 1:
                    repeated = list(check)[0]
                    screen.clear_line(1)
                    screen.print_at(0, 1, i)
                    for x in range(0, n, seg):
                        screen.print_at(x, 1, c(str(i)[x:x+seg]))           
                        time.sleep(.5)      
                    screen.print_at(0, 2, screen.colored("Invalid!", screen.bcolors.RED))
                    time.sleep(1)
                    break
            screen.clear_line(1)
    
    input()