import sys
input = open(sys.argv[1], 'r').readlines()

sacks = list(map(lambda x: (x[:len(x) // 2], x[len(x) // 2:]), input))


def score(a):
    if ord(a) >= ord('a') and ord(a) <= ord('z'):
        return ord(a) - ord('a') + 1
    else:
        return ord(a) - ord('A') + 27


def item(sacks):
    (left, right) = sacks
    for l in left:
        if l in right:
            return l
    for r in right:
        if r in left:
            return r


# part 1
print(sum(map(lambda sack: score(item(sack)), sacks)))


def chunk(xs, n):
    for i in range(0, len(xs), n):
        yield xs[i:i + n]


def badge(group):
    [xs, ys, zs] = group
    for x in xs:
        if x in ys and x in zs:
            return x


print(sum(map(lambda group: score(badge(group)), list(chunk(input, 3)))))
