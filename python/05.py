import sys
input = open(sys.argv[1], 'r').read()

[crates_input, moves_input] = input.split("\n\n")


def parse_crates(input: list[str]):
    # the +1 is the missing ' ' after the last ']'
    length = (len(input[0]) + 1) // 4
    crates = []

    for _ in range(length):
        crates.append([])

    # the last line is the numbering, which we skip
    # from the test input, we can expect whitespace
    for line in input[:len(input) - 1]:
        for i in range(length):
            label = line[1 + (i*4)]
            if label != " ":
                crates[i].append(label)

    # they were constructed backwards, so we need to flip each crate
    for crate in crates:
        crate.reverse()

    return crates


def parse_move(move):
    # move 2  from 7    to 2
    [_,    n, _,   src, _, dst] = move.split(" ")
    return (int(n), int(src), int(dst))


crates = parse_crates(crates_input.splitlines())
moves = list(map(parse_move, moves_input.splitlines()))


def apply_move(crates, move):
    (n, src, dst) = move
    for _ in range(n):
        crate = crates[src-1].pop()
        crates[dst-1].append(crate)

# part 1 mutates, so I just commented it out instead of fighting deepcopy or
# whatever.

# for move in moves: apply_move(crates, move)

# part 1
# for crate in crates:
#     print(crate[-1], end="")
# print()


def apply_move_multi(crates, move):
    (n, src, dst) = move
    src_crate = crates[src-1]
    chunk = src_crate[len(src_crate) - n:]

    assert n == len(chunk)
    crates[dst-1].extend(chunk)
    del src_crate[len(src_crate) - n:]


for move in moves:
    apply_move_multi(crates, move)


# part 2
for crate in crates:
    print(crate[-1], end="")
print()
