import sys
input = open(sys.argv[1], 'r').read().split("\n")


X = 1
cycles = 1

s = 0

display = [[], [], [], [], [], [], [], ]


def tick():
    global cycles
    if (cycles - 20) % 40 == 0:
        # print(cycles, X, signal_strength())
        global s
        s += signal_strength()

    global display

    column = (cycles - 1) % 40
    row = (cycles - 1) // 40

    print(row, column)

    if X in [column-1, column, column + 1]:
        display[row].append("#")
    else:
        display[row].append(".")

    cycles += 1


def addx(v):
    global X
    tick()
    tick()
    X += v


def noop():
    tick()


def execute(line):
    if line[0:4] == "noop":
        noop()
    elif line[0:4] == "addx":
        addx(int(line[4:]))


def signal_strength():
    # the cycle number multiplied by the value of the X register
    global cycles
    global X
    return cycles * X


for line in input:
    execute(line)

print(s)

for line in display:
    print(''.join(line))
