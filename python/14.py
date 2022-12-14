from collections import defaultdict
import sys

input = open(sys.argv[1], 'r').read().split("\n")


def parse(line):
    pairs = line.split(" -> ")
    for pair in pairs:
        [x, y] = pair.split(",")
        yield (int(x), int(y))


lines = list(map(lambda l: list(parse(l)), input))


def sparse_grid(value='.'):
    grid = defaultdict(lambda: defaultdict(lambda: value))
    return grid


def draw_line_segment(grid, start, end, value='#'):
    # sorting for range to work right
    x1, x2 = sorted([start[0], end[0]])
    y1, y2 = sorted([start[1], end[1]])

    # +1 for inclusive range
    for y in range(y1, y2+1):
        for x in range(x1, x2+1):
            grid[y][x] = value


def draw_lines(grid, lines, value=''):
    for line in lines:
        end = line.pop()
        while line:
            start = line.pop()
            draw_line_segment(grid, start, end)
            end = start


def print_grid(grid, x1=0, x2=0, y1=0, y2=10):
    for y in range(y1, y2):
        print("{0:03}".format(y), end="")
        for x in range(x1, x2):
            print(grid[y][x], end="")
        print()
    print()


def move_down(grid, sand):
    sx, sy = sand

    if grid[sy+1][sx] == '.':
        grid[sy][sx] = '.'
        grid[sy+1][sx] = 'o'
        return (sx, sy+1)

    elif grid[sy+1][sx-1] == '.':
        grid[sy][sx] = '.'
        grid[sy+1][sx-1] = 'o'
        return (sx-1, sy+1)

    elif grid[sy+1][sx+1] == '.':
        grid[sy][sx] = '.'
        grid[sy+1][sx+1] = 'o'
        return (sx+1, sy+1)

    return None


def simulate_single(grid, sand):
    while True:
        sand = move_down(grid, sand)
        # print_grid(grid, 494, 505, 0, 10)

        if sand is None:
            return False
        elif sand[1] > VOID:
            return True


def simulate(grid):
    count = 0
    into_void = False
    while not into_void and grid[SOURCE[1]][SOURCE[0]] == '.':
        grid[SOURCE[1]][SOURCE[0]] = 'o'
        into_void = simulate_single(grid, SOURCE)
        count += 1
        # print_grid(grid, 470, 530, 0, 20)

    return count


def find_bottom(grid):
    return max(grid.keys())


grid = sparse_grid()
draw_lines(grid, lines)

VOID = find_bottom(grid) + 4
SOURCE = (500, 0)

# part1 = simulate(grid) - 1
# print("part 1:", part1)

floor = find_bottom(grid) + 2
width_max = max(map(max, grid.values())) + 1000
width_min = min(map(min, grid.values())) - 1000

draw_line_segment(grid, (width_min, floor), (width_max, floor), '#')

part2 = simulate(grid)
print(part2)
