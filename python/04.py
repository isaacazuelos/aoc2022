import sys
input = open(sys.argv[1], 'r').readlines()


def parse(line):
    [l, r] = line.split(",")
    [l1, l2] = l.split("-")
    [r1, r2] = r.split("-")
    return ((int(l1), int(l2)), (int(r1), int(r2)))


pairs = list(map(parse, input))


def overlaps(pair):
    ((l1, l2), (r1, r2)) = pair
    return (l1 <= r1 and l2 >= r2) or (r1 <= l1 and r2 >= l2)


print(len(list(filter(overlaps, pairs))))


def overlap_at_all(pair):
    ((l1, l2), (r1, r2)) = pair
    return bool((l1 <= r1 and r1 <= l2) or (l1 <= r2 and r2 <= l2) or (r1 <= l1 and l1 <= r2) or (r1 <= l2 and l2 <= r2))


print(len(list(filter(overlap_at_all, pairs))))
