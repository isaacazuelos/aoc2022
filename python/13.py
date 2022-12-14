import sys
from functools import cmp_to_key

input = open(sys.argv[1], 'r').read().split("\n\n")


def parse(pairs):
    parsed = []
    for pair in pairs:
        f, s = pair.split("\n")
        # Don't give me that look
        parsed.append((eval(f), eval(s)))
    return parsed


input = parse(input)


# true is left, none is eq, false is right
def compare(left, right):
    # print("comparing", left, right)
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return 'left'
        elif right < left:
            return 'right'
        else:
            return 'equal'

    elif isinstance(left, list) and isinstance(right, list):
        for i in range(min(len(left), len(right))):
            cmp = compare(left[i], right[i])
            if cmp != 'equal':
                return cmp

        if len(left) < len(right):
            return 'left'
        elif len(left) == len(right):
            return 'equal'
        else:
            return 'right'

    elif isinstance(left, int) and isinstance(right, list):
        return compare([left], right)
    else:
        return compare(left, [right])


def part1(pairs):
    s = 0

    for (i, (left, right)) in enumerate(pairs):
        if compare(left, right) != 'right':
            s += i + 1

    return s


# print(part1(input))


def as_cmp(left, right):
    test = compare(left, right)
    if test == 'right':
        return 1
    elif test == 'left':
        return -1
    else:
        return 0


def is_decoder(packet):
    return packet == [[2]] or packet == [[6]]


def part2(pairs):
    packets = [[[2]], [[6]]]
    for (left, right) in pairs:
        packets.append(left)
        packets.append(right)

    packets = sorted(packets, key=cmp_to_key(as_cmp))

    prod = 1
    for i, packet in enumerate(packets):
        if is_decoder(packet):
            prod *= i + 1  # zero indexing
            print(i)

    return prod


print(part2(input))
