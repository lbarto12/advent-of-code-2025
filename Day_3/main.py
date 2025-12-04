from typing import List, Tuple

def max_and_location(s: str) -> Tuple[str, int]:
    mx, mi = '-1', -1
    for i, c in enumerate(s):
        if int(c) > int(mx):
            mx, mi = c, i
    return mx, mi


with open("input.txt") as file:
    lines: List[str] = [i.strip() for i in file.readlines()]
    
    j1 = j2 = 0
    for line in lines:
        # Part 1
        first, f_idx = max_and_location(line[:-1])
        second, _ = max_and_location(line[f_idx + 1:])
        j1 += int(first + second)

        # Part 2
        constructed, boundary = '', 0
        for i in range(-11, 1):
            nxt, idx = max_and_location(line[boundary:i] if i else line[boundary:])
            boundary += idx + 1
            constructed += nxt
        j2 += int(constructed)

    print("Part 1:", j1)
    print("Part 2:", j2)
