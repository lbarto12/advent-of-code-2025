from typing import List, Tuple
import time

from visual_tools.screen import *

with open("Day_2/input.txt") as file:
    lines: List[str] = file.read().split(',')

    ranges: List[Tuple[int, int]] = [tuple(int(i) for i in r.split('-')) for r in lines]

    c = ColorAlternator()
    
    for l, r in ranges:
        clear()
        print_at(0, 0, f"{l}-{r}")
        for i in range(l, r + 1):
            print_at(0, 1, i)
            for seg in range((n := len(s := str(i))) // 2, 0, -1):
                if n  % seg:
                    continue
                for x in range(0, n, seg):
                    print_at(x, 1, c.next(str(i)[x:x+seg]))
                if len(check := {s[x:x+seg] for x in range(0, n, seg)}) == 1:
                    repeated = list(check)[0]
                    clear_line(1)
                    print_at(0, 1, i)
                    for x in range(0, n, seg):
                        print_at(x, 1, c.next(str(i)[x:x+seg]))           
                        time.sleep(.5)      
                    print_at(0, 2, colored("Invalid!", bcolors.RED))
                    time.sleep(1)
                    break
            clear_line(1)