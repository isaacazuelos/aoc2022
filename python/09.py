import sys
input = open(sys.argv[1], 'r').read().split("\n")


def parse(line):
    (letter, count) = line.split(" ")
    count = int(count)
    if letter == 'R':
        dir = (1, 0)
    elif letter == 'L':
        dir = (-1, 0)
    elif letter == 'U':
        dir = (0, 1)
    elif letter == 'D':
        dir = (0, -1)

    return (dir, count)


input = list(map(parse, input))


def move_head(head, dir):
    return (head[0] + dir[0], head[1] + dir[1])


def update_tail(head, tail):
    (hx, hy) = head
    (tx, ty) = tail
    # If the head is ever two steps directly up, down, left, or right from the
    # tail, the tail must also move one step in that direction so it remains
    # close enough:

    if hy == ty + 2 and hx == tx:  # directly 2 above
        return (tx, ty + 1)
    if hy == ty - 2 and hx == tx:  # directly 2 below
        return (tx, ty - 1)
    if hx == tx + 2 and hy == ty:  # directly 2 left
        return (tx + 1, ty)
    if hx == tx - 2 and hy == ty:  # directly 2 right
        return (tx - 1, ty)

    # Otherwise, if the head and tail aren't touching and aren't in the same row
    # or column, the tail always moves one step diagonally to keep up:
    (dx, dy) = (hx - tx, hy - ty)

    if abs(dx) + abs(dy) <= 2:
        return (tx, ty)

    if hx < tx and hy < ty:
        return (tx - 1, ty - 1)
    if hx < tx and hy > ty:
        return (tx - 1, ty + 1)
    if hx > tx and hy < ty:
        return (tx + 1, ty - 1)
    if hx > tx and hy > ty:
        return (tx + 1, ty + 1)

    return (tx, ty)


def part1():
    head = (0, 0)
    tail = (0, 0)
    seen = set()

    for (dir, count) in input:
        for _ in range(count):
            head = move_head(head, dir)
            tail = update_tail(head, tail)
            seen.add(tail)

    return len(seen)


print(part1())


def part2(knot_count):
    # head is knot 0
    knots = [(0, 0) for _ in range(knot_count)]
    seen = set()

    for j, (dir, count) in enumerate(input):
        for _ in range(count):
            knots[0] = move_head(knots[0], dir)
            for i in range(knot_count-1):
                new_position = update_tail(knots[i], knots[i+1])
                knots[i+1] = new_position
                if i == knot_count-2:
                    seen.add(new_position)
    return seen


def display(knots):
    n = 15
    for y in range(n, -n, -1):
        for x in range(-n, n, 1):
            if (x, y) in knots:
                printed = False
                for i in range(len(knots)):
                    if knots[i] == (x, y) and not printed:
                        if i == 0:
                            print("H", end="")
                        else:
                            print(i, end="")
                        printed = True
            elif (x, y) == (0, 0):
                print("s", end="")
            else:
                print(".", end="")
        print("")
    print()


def display_seen(seen):
    n = 15
    for y in range(n, -n, -1):
        for x in range(-n, n, 1):
            if (x, y) == (0, 0):
                print("s", end="")
            elif (x, y) in seen:
                print("#", end="")
            else:
                print(".", end="")
        print("")
    print()


print(len(part2(10)))
