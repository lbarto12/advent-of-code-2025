mkdir Day_$1

echo "Creating files..."
touch Day_$1/main.py
touch Day_$1/visual.py
touch Day_$1/readme.md
echo "done"

echo "Fetching daily input..."
curl -o Day_$1/input.txt --cookie "session=53616c7465645f5f2c9cc339d1ccfa9c7b4e97080f62b74994396147eee1ff1ef994737b9f751e703fa8816861c57c831427d9742cd03445ee460a0061f338a9" https://adventofcode.com/2025/day/$2/input
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

def solve() -> Tuple[any, any]:
    with open(\"input.txt\") as file:
        lines: List[List[chr]] = [i.strip() for i in file.readlines()]

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
