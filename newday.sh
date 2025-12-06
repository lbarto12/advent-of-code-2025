#!/usr/bin/env bash
source ./.env
echo "Loading with session: $SESSION"

mkdir Day_$1

echo "Creating files..."
touch Day_$1/main.py
touch Day_$1/visual.py
touch Day_$1/readme.md
echo "done"

echo "Fetching daily input..."
curl -o Day_$1/input.txt --cookie "session=$SESSION" https://adventofcode.com/2025/day/$1/input
echo "done"

echo "Populating readme.md..."
echo "
## Visualization
![til](./v.gif)
" >> ./Day_$1/readme.md
echo "done"

echo "Populating code file..."
echo "
from typing import List, Tuple
from utils.types import Solution

def solve() -> Solution:
    with open(\"Day_$1/input.txt\") as file:
        lines: List[str] = [i.strip() for i in file.readlines()]

        p1: int = 0
        p2: int = 0

        return p1, p2 

if __name__ == '__main__':
    p1, p2 = solve()
    print(\"Part 1:\", p1)
    print(\"Part 2:\", p2)
" >> ./Day_$1/main.py
echo "done"

echo "Day setup complete"
