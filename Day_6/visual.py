from typing import List
import re
import time

import visual_tools.screen as screen
from utils.ds import transpose


with open("Day_6/input.txt") as file:
    read: List[str] = file.readlines()
    lines: List[List[str]] = [i.strip().split() for i in read]
    ops = lines[-1]
    
    p2: int = 0
    left: int = 0
    widths = [len(i) for i in re.findall(r"[*+] +", read[-1])]
    for k, w in enumerate(widths):
        c = screen.ColorAlternator()
        screen.clear()
        screen.print_at(0, len(lines), f"total: {p2}")
        print(*[line[left:left+w] for line in read[:-1]], sep='\n')
        for j, line in enumerate(read[:-1]):
            screen.print_at(0, j, c.next(line[left:left+w]))
            time.sleep(.5)
        print(f'op: {ops[k]}')
        time.sleep(.5)

        screen.print_at(w + 4, 1, "->")
        time.sleep(.5)
        screen.print_at(w + 7, len(lines) - 2, ops[k])

        for i, s in enumerate(transpose([line[left:left+w] for line in read[:-1]])):
            for j, c in enumerate(s):
                screen.print_at(w + 9 + j, i, c)

        for i, s in enumerate(transpose([line[left:left+w] for line in read[:-1]])):
            c2 = screen.ColorAlternator()
            for j, c in enumerate(s):
                screen.print_at(w + 9 + j, i, c2.next(c))
            time.sleep(.5)
        time.sleep(.5)


        nums: List[str] = [''.join(i) for i in transpose([line[left:left+w] for line in read[:-1]]) if any(j.isnumeric() for j in i)]
        screen.print_at(w + 8, len(lines) - 1, f"={eval(ops[k].join(nums))}")
        p2 += eval(ops[k].join(nums))
        left += w
        time.sleep(3)
    screen.print_at(0, len(lines), f"total: {p2}")
    input()
