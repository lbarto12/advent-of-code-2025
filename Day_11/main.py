from typing import List, Tuple, Set, Dict
from utils.types import Solution
from utils.timing import runtime

Memo = Dict[Tuple[str, bool, bool], int]

def valid_paths(key: str, dac: bool, fft: bool, paths: Dict[str, Set[str]], memo: Memo) -> int:
    if key == 'out':
        return dac * fft
    elif key == 'dac':
        dac = True
    elif key == 'fft':
        fft = True
    if (mk := (key, dac, fft)) not in memo:
        memo[mk] = sum(valid_paths(nxt, dac, fft, paths, memo) for nxt in paths[key])
    return memo[mk]


@runtime
def solve() -> Solution:
    with open("Day_11/input.txt") as file:
        lines: List[List[str]] = [i.strip().split(' ') for i in file.readlines()]

        paths: Dict[str, Set[str]] = {i[0][:-1]: set(i[1:]) for i in lines}

        p1: int = valid_paths('you', True, True, paths, {})
        p2: int = valid_paths('svr', False, False, paths, {})

        return p1, p2 

if __name__ == '__main__':
    p1, p2 = solve()
    print("Part 1:", p1)
    print("Part 2:", p2)

