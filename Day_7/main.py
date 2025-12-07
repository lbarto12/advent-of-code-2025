from functools import cache

from typing import List, Tuple
from utils.types import Solution, Position
from utils.ds import at, set_at, t_add

def beam_splits(pos: Position, board: List[List[chr]]):
    if pos[1] >= len(board) or at(board, pos) == '|':
        return 0
    if at(board, pos) == "^":
        return beam_splits(t_add(pos, (-1, 1)), board) + \
            beam_splits(t_add(pos, (1, 1)), board) + 1    
    set_at(board, pos, '|')
    return beam_splits(t_add(pos, (0, 1)), board)

@cache
def beam_perms(pos: Position, board: Tuple[Tuple[chr]]):
    if pos[1] >= len(board):
        return 1
    if at(board, pos) == "^":
        return beam_perms(t_add(pos, (-1, 1)), board) + beam_perms(t_add(pos, (1, 1)), board)
    return beam_perms(t_add(pos, (0, 1)), board)

def solve() -> Solution:
    with open("Day_7/input.txt") as file:
        lines: List[List[chr]] = [list(i.strip()) for i in file.readlines()]
        p2_memo: Tuple[Tuple[chr]] = tuple(map(tuple, lines))
        
        start: Position = (lines[0].index("S"), 0)

        p1: int = beam_splits(start, lines)
        p2: int = beam_perms(start, p2_memo)

        return p1, p2 

if __name__ == '__main__':
    p1, p2 = solve()
    print("Part 1:", p1)
    print("Part 2:", p2)

