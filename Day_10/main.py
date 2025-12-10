from typing import List, Tuple, Set
from utils.types import Solution
from utils.timing import runtime
from utils.ds import transpose

import re
from scipy.optimize import linprog

Button = Tuple[int, ...]
Machine = Tuple[str, List[Button], Tuple[int, ...]]

def press(state: str, button: Button) -> str:
    return ''.join({'#': '.', '.': '#'}[c] if i in button else c for i, c in enumerate(state)) # yucky

def min_presses_lights(machine: Machine) -> int:
    seen_states: Set[str] = set()   # NEEEEDED a memo ;)
    target: str = machine[0]
    q = [(0, '.' * len(target), 0)] # (presses, state, b_idx)

    while q:
        presses, state, b_idx = q.pop(0)

        if state == target:
            return presses
        if state in seen_states:
            continue
        seen_states.add(state)

        q += [(presses + 1, press(state, button), i) for i, button in enumerate(machine[1][b_idx:])]

def min_presses_joltage(machine: Machine) -> int: # Learned about ILP *today*, while coding this :)
    return int(linprog(
        c=[1] * len(machine[1]), 
        A_eq=transpose([[int(i in button) for i in range(len(machine[2]))] for button in machine[1]]), 
        b_eq=machine[2], 
        integrality=1).x.sum())
    

@runtime
def solve() -> Solution:
    with open("Day_10/input.txt") as file:
        lines: List[str] = [i.strip() for i in file.readlines()]
        machines: List[Machine] = \
            [(re.findall(r'\[(.+)\]', i)[0], 
                 [tuple(map(int, f)) for f in [x.split(',') for x in re.findall(r'\(([\d,]+)\)', i)]], 
                 tuple(map(int, re.findall(r'\{(.+)\}', i)[0].split(',')))
            ) for i in lines]

        p1: int = sum(min_presses_lights(m) for m in machines)
        p2: int = sum(min_presses_joltage(m) for m in machines)

        return p1, p2 


if __name__ == '__main__':
    p1, p2 = solve()
    print("Part 1:", p1)
    print("Part 2:", p2)

