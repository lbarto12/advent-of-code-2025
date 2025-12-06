from typing import List
from utils.types import Solution

import re

from utils.ds import transpose

def solve() -> Solution:
    with open("Day_6/input.txt") as file:
        read: List[str] = file.readlines()
        lines: List[List[str]] = [i.strip().split() for i in read]
        eqs, ops = transpose(lines[:-1]), lines[-1]

        p1: int = sum(eval(ops[i].join(eq)) for i, eq in enumerate(eqs))
        
        p2: int = 0
        left: int = 0
        widths = [len(i) for i in re.findall(r"[*+] +", read[-1])]
        for i, w in enumerate(widths):
            nums: List[str] = [''.join(i) for i in transpose([line[left:left+w] for line in read[:-1]]) if any(j.isnumeric() for j in i)]
            p2 += eval(ops[i].join(nums))
            left += w

    return p1, p2

if __name__ == '__main__':
    p1, p2 = solve()
    print("Part 1:", p1)
    print("Part 2:", p2)

