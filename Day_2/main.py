from typing import List, Tuple

Range = Tuple[int, int]

def solve():
    with open("Day_2/input.txt") as file:
        ranges: List[Range] = [tuple(int(i) for i in r.split('-')) for r in file.read().split(',')]

        # Both Parts
        p1 = p2 = 0
        for l, r in ranges:
            for i in range(l, r + 1):
                for seg in range((n := len(s := str(i))) // 2, 0, -1):
                    if not n % seg and len({s[x:x+seg] for x in range(0, n, seg)}) == 1:
                        p1 += i * (seg == n // 2 and not n % 2)
                        p2 += i
                        break
        
        print("Part 1:", p1)
        print("Part 2:", p2)

if __name__ == '__main__':
    solve()
