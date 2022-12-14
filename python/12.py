import sys
from collections import deque

input = open(sys.argv[1], 'r').read().split("\n")


def elevation(grid, x, y):
    letter = grid[y][x]
    if letter.islower():
        return ord(letter)
    elif letter == 'S':
        return ord('a')
    elif letter == 'E':
        return ord('z')


def on_board(grid, x, y):
    return x >= 0 and y < len(grid) and y >= 0 and x < len(grid[0])


def neighbors(grid, x, y):
    yield (x-1, y)
    yield (x+1, y)
    yield (x, y-1)
    yield (x, y+1)


def valid_steps(grid, x, y):
    current = elevation(grid, x, y)
    for (nx, ny) in neighbors(grid, x, y):
        if on_board(grid, nx, ny) and elevation(grid, nx, ny) <= current + 1:
            yield (nx, ny)


def points(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            yield (x, y)


def dijkstra(grid, source):
    dist = {}
    prev = {}
    q = deque()
    for v in points(grid):
        dist[v] = 1000000
        prev[v] = None
        q.append(v)

    dist[source] = 0

    while q:
        u = min(q, key=lambda u: dist[u])
        q.remove(u)

        for v in valid_steps(grid, u[0], u[1]):
            alt = dist[u] + 1
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
    return dist, prev


def find(grid, char):
    for (x, y) in points(grid):
        if grid[y][x] == char:
            return (x, y)


def find_all(grid, char):
    for (x, y) in points(grid):
        if grid[y][x] == char:
            yield (x, y)


def part1(input):
    start = find(input, 'S')
    end = find(input, 'E')
    v, p = dijkstra(input, start)

    return v[end]


# print(part1(input))

# this time we flip it, so a


def valid_back_steps(grid, x, y):
    prev = elevation(grid, x, y)
    for (nx, ny) in neighbors(grid, x, y):
        if on_board(grid, nx, ny) and elevation(grid, nx, ny) >= prev - 1:
            yield (nx, ny)


def dijkstra2(grid, source):
    dist = {}
    prev = {}
    q = deque()
    for v in points(grid):
        dist[v] = 1000000
        prev[v] = None
        q.append(v)

    dist[source] = 0

    while q:
        u = min(q, key=lambda u: dist[u])
        q.remove(u)

        for v in valid_back_steps(grid, u[0], u[1]):
            alt = dist[u] + 1
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
    return dist, prev


def part2(input):
    end = find(input, 'E')
    starts = list(find_all(input, 'a'))
    v, p = dijkstra2(input, end)

    shortest = 100000
    for start in starts:
        if v[start] < shortest:
            shortest = v[start]

    return shortest


print(part2(input))
