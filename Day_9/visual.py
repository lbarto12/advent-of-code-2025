# Again, AI generated. I refuse to take credit for code I did not write. Looks cool though :)
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from shapely.geometry import Polygon
from typing import List, Tuple
import time
from matplotlib.patches import Polygon as MplPolygon

Position = Tuple[int, int]

def area(a: Position, b: Position) -> int:
    return (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)

def is_valid(a: Position, b: Position, p: Polygon) -> bool:
    poly = Polygon([a, (a[0], b[1]), b, (b[0], a[1])])
    return p.covers(poly)

def solve():
    # --- Load points ---
    with open("Day_9/input.txt") as file:
        red_tiles: List[Position] = [
            tuple(map(int, line.strip().split(",")))
            for line in file
        ]

    p = Polygon(red_tiles)
    pairs = [(red_tiles[i], red_tiles[j])
             for i in range(len(red_tiles))
             for j in range(i+1, len(red_tiles))]

    # --- Setup figure ---
    fig, ax = plt.subplots(figsize=(7,7))
    plt.subplots_adjust(bottom=0.15)  # space for button
    xs, ys = p.exterior.xy
    ax.plot(xs, ys, "k-")

    # rectangle artists
    current_rect = MplPolygon([[0,0],[0,1],[1,1],[1,0]], fill=False, edgecolor="red", linewidth=1.5)
    best_rect = MplPolygon([[0,0],[0,1],[1,1],[1,0]], fill=False, edgecolor="green", linewidth=2)
    ax.add_patch(current_rect)
    ax.add_patch(best_rect)

    ax.set_aspect("equal", "box")
    plt.title("Rectangle Search Visualization")
    plt.pause(0.001)

    # blitting setup
    fig.canvas.draw()
    bg = fig.canvas.copy_from_bbox(ax.bbox)

    def update_patch(patch, a, b):
        patch.set_xy([a, (a[0], b[1]), b, (b[0], a[1])])

    # --- Animation function ---
    def start(event):
        start_button.ax.set_visible(False)  # hide button after click
        fig.canvas.draw()

        max_area = 0
        best_pair = None
        t0 = time.time()
        draw_every = 100  # adjust speed

        for i, (a, b) in enumerate(pairs):
            A = area(a, b)

            # update best
            if A > max_area and is_valid(a, b, p):
                max_area = A
                best_pair = (a, b)
                update_patch(best_rect, *best_pair)

            # visualization throttling
            if i % draw_every == 0:
                fig.canvas.restore_region(bg)
                update_patch(current_rect, a, b)
                ax.draw_artist(current_rect)
                ax.draw_artist(best_rect)
                fig.canvas.blit(ax.bbox)
                fig.canvas.flush_events()

        dt = time.time() - t0
        print(f"Completed scan in {dt:.2f} seconds")
        print("Max area:", max_area)

    # --- Button ---
    ax_button = plt.axes([0.4, 0.05, 0.2, 0.05])  # x, y, width, height
    start_button = Button(ax_button, 'Start')
    start_button.on_clicked(start)

    plt.show()

if __name__ == '__main__':
    solve()
