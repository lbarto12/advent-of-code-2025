from typing import List, Tuple, Set
from utils.types import Solution
from utils.ds import DisjointSetUnion
from utils.timing import runtime

import math

Junction = Tuple[int, int, int]
Circuit = Set[Junction]
Edge = Tuple[Junction, Junction]

def dist(p1: Junction, p2: Junction) -> float:
    return math.sqrt(
        (p2[0] - p1[0]) ** 2 +
        (p2[1] - p1[1]) ** 2 +
        (p2[2] - p1[2]) ** 2
    )

def get_circuit(circuits: List[Circuit], junction: Junction) -> Tuple[int, Circuit]:
    for i, circuit in enumerate(circuits):
        if junction in circuit:
            return i, circuit
    return -1, None

def get_part_1(s: DisjointSetUnion) -> int:
    a, b, c = sorted(s.len(i) for i in s)[-3:]
    return a * b * c

@runtime
def solve() -> Solution:
    with open("Day_8/input.txt") as file:
        j_boxes: List[Junction] = [tuple(map(int, i.strip().split(','))) for i in file.readlines()]

        dists: List[Tuple[Edge, float]] = sorted([((i, j), dist(i, j)) for b, i in enumerate(j_boxes) for j in j_boxes[b + 1:]], key=lambda x: x[1])
        
        circuits = DisjointSetUnion(j_boxes)

        p1: int = 0
        i = -1
        while len(circuits) > 1:
            (a, b), _ = dists[i := i + 1]
            if i == 1000:                       # Change for relative input
                p1 = get_part_1(circuits)
            circuits.union(a, b)

        p2: int = a[0] * b[0]

        return p1, p2 


if __name__ == '__main__':
    p1, p2 = solve()
    print("Part 1:", p1)
    print("Part 2:", p2)

