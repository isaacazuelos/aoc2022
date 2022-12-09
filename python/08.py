# expected test is 21
import sys
input = open(sys.argv[1], 'r').read().split("\n")

input = [[int(tree) for tree in row] for row in input]


def points(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            yield (x, y)


def left(grid, x, y):
    trees = grid[y][:x]
    trees.reverse()
    return trees


def right(grid, x, y):
    trees = grid[y][x+1:]
    return trees


def up(grid, x, y):
    trees = list(row[x] for row in grid[:y])
    trees.reverse()
    return trees


def down(grid, x, y):
    return list(row[x] for row in grid[y+1:])


def height(grid, x, y):
    return grid[y][x]


def is_visible(grid, x, y):
    h = height(grid, x, y)

    vis = [True, True, True, True]

    for i, direction in enumerate([left, right, up, down]):
        for tree in direction(grid, x, y):
            if tree >= h:
                vis[i] = False

    return any(vis)


def part1(grid):
    count = 0
    for (x, y) in points(grid):
        if is_visible(grid, x, y):
            count += 1
    return count


print(part1(input))


def viewing_distance(direction, grid, x, y):
    dist = 0
    h = height(grid, x, y)

    for tree in direction(grid, x, y):
        dist += 1
        if tree >= h:
            break

    return dist


def score(grid, x, y):
    product = 1
    for direction in [left, right, up, down]:
        vd = viewing_distance(direction, grid, x, y)
        product = product * vd
    return product


def part2(grid):
    return max(score(grid, x, y) for (x, y) in points(grid))


print(part2(input))
