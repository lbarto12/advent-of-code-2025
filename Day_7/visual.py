from typing import List
from utils.types import Position
from utils.ds import at, set_at, t_add
import visual_tools.screen as screen

import time
from copy import deepcopy


def beam_splits(pos: Position, board: List[List[chr]]):
    q: List[Position] = [t_add(pos, (0, 1))]

    level: int = pos[1]
    render_queue: List[Position] = []

    while q:
        p: Position = q.pop(0)

        if p[1] > level:
            level = p[1]
            for r in render_queue:
                screen.print_at(*r, screen.colored('|', screen.bcolors.RED))
            render_queue.clear()
            time.sleep(.1)

        if p[1] >= len(board) or at(board, p) == '|':
            continue
        if at(board, p) == "^":
            q.append(t_add(p, (-1, 1)))
            q.append(t_add(p, (1, 1)))
            render_queue.append(t_add(p, (-1, 0)))
            render_queue.append(t_add(p, (1, 0)))
        else:
            set_at(board, p, '|')
            render_queue.append(p)
            q.append(t_add(p, (0, 1)))

def beam_perms(pos: Position, board: List[List[chr]]):
    stk: List[Position] = [t_add(pos, (0, 1))]
    erase: List[Position] = []

    while stk:
        time.sleep(.05)
        p: Position = stk.pop()
        while erase and erase[-1][1] >= p[1]:
            e = erase.pop()
            screen.print_at(*e, ' ')
      
        if p[1] >= len(board):
            continue
        if at(board, p) == '^':
            stk.append(t_add(p, (-1, 0)))
            stk.append(t_add(p, (1, 0)))
            continue
        screen.print_at(*p, screen.colored("|", screen.bcolors.RED))  
        erase.append(p)
        stk.append(t_add(p, (0, 1)))

with open("Day_7/input.txt") as file:
    lines: List[List[chr]] = [list(i.strip()) for i in file.readlines()]
    p2_memo: List[List[chr]] = deepcopy(lines)
    
    start: Position = (lines[0].index("S"), 0)

    screen.clear()
    print(*[''.join(i).replace('.', ' ') for i in lines], sep = '\n')
    screen.print_at(0, 0, screen.colored("P1:", screen.bcolors.OKGREEN))
    beam_splits(start, lines)
    time.sleep(5)

    screen.clear()
    print(*[''.join(i).replace('.', ' ') for i in p2_memo], sep = '\n')
    screen.print_at(0, 0, screen.colored("P2:", screen.bcolors.OKGREEN))
    beam_perms(start, p2_memo)
    time.sleep(5)

    




