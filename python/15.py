import sys

input = open(sys.argv[1], 'r').read().split("\n")


def parse(line):
    words = line.split(" ")

    sx = int(words[2].split("=")[1][0:-1])
    sy = int(words[3].split("=")[1][0:-1])
    bx = int(words[8].split("=")[1][0:-1])
    by = int(words[9].split("=")[1])

    return ((sx, sy), (bx, by))


input = list(map(parse, input))


def distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def effect(line, sensor, beacon):
    points = distance(sensor, beacon)
    spent_to_line = abs(sensor[1] - line)
    spread = points - spent_to_line
    if spread >= 0:
        return (sensor[0] - spread, sensor[0] + spread)


def covered(lines, line):
    covered = set()
    for (sensor, beacon) in lines:
        span = effect(line, sensor, beacon)
        if span:
            (start, end) = span
            for point in range(start, end + 1):
                covered.add(point)

    return covered


def part1(lines, line):
    c = covered(lines, line)
    for (_, beacon) in lines:
        if beacon[1] == line and beacon[0] in c:
            c.remove(beacon[0])
    return len(c)


print(part1(input, 2000000))


def tuning_freq(beacon):
    return (beacon[0] * 4000000) + beacon[1]


def part2(lines):
    ranges = []
    for (sensor, beacon) in lines:
        ranges.append(distance(sensor, beacon))
    ranges.sort()
    print(ranges)

    # for y in range(0, 4000000+1):
    #     for x in range(0, 4000000+1):
    #         pass
    #     print(x, y)

    return sum(sr * sr for sr in ranges) - (4000000 * 4000000)


print(part2(input))
