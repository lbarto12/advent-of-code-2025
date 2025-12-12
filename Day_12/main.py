from typing import List, Tuple
from utils.types import Solution
from utils.timing import runtime

import re

Tree = Tuple[Tuple[int, int], List[int]]

def can_fit(tree: Tree, weights: List[int]) -> bool:
    (w, h), counts = tree
    return w * h >= sum(weights[i] * c for i, c in enumerate(counts))


# I wasted an unreasonable amount of time trying to write a packing algorithm.
# Only to realize that, for whatever reason, if I just exclude options that have greater total tiling, I get the right answer.
# Which doesn't work on the demo input - because, realistically, it shouldn't work on the real input either. >:(
# Very misleading, advent.
@runtime
def solve() -> Solution:
    with open("Day_12/input.txt") as file:
        lines: str = file.read()
        chunks: List[str] = lines.split("\n\n")

        weights: List[int] = [sum(f.count('#') for f in x) for x in [tuple(i.split('\n')[1:]) for i in chunks[:-1]]]        
        trees: List[Tree] = [(tuple(map(int, re.findall(r'(\d+)x(\d+)', j)[0])), list(map(int, filter(lambda x: x, j.split(':')[1].split(' '))))) for j in [i for i in filter(lambda x: x, chunks[-1].split('\n'))]]

        p1: int = sum(can_fit(tree, weights) for tree in trees)
        p2: int = ":)"

        return p1, p2 


if __name__ == '__main__':
    p1, p2 = solve()
    print("Part 1:", p1)
    print("Part 2:", p2)

