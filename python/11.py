from dataclasses import dataclass, field
from collections import deque
from functools import reduce

# There's only 7, it's easier to parse by hand than write a parser.


@dataclass
class Monkey:
    items: deque[int]
    op: None  # (new: int, old: int) -> int
    test_divisible_by: int
    on_true: int
    on_false: int


def mul(n):
    return lambda old: old * n


def add(n):
    return lambda old: old + n


def sqr():
    return lambda old: old * old


real_monkeys = (
    Monkey(deque([80]), mul(5), 2, 4, 3),
    Monkey(deque([75, 83, 74]), add(7), 7, 5, 6),
    Monkey(deque([86, 67, 61, 96, 52, 63, 73]), add(5), 3, 7, 0),
    Monkey(deque([85, 83, 55, 85, 57, 70, 85, 52]), add(8), 17, 1, 5),
    Monkey(deque([67, 75, 91, 72, 89]), add(4), 11, 3, 1),
    Monkey(deque([66, 64, 68, 92, 68, 77]), mul(2), 19, 6, 2),
    Monkey(deque([97, 94, 79, 88]), sqr(), 5, 2, 7),
    Monkey(deque([77, 85]), add(6), 13, 4, 0),
)

test_monkeys = [
    Monkey(deque([79, 98]), mul(19), 23, 2, 3),
    Monkey(deque([54, 65, 75, 74]), add(6), 19, 2, 0),
    Monkey(deque([79, 60, 97]), sqr(), 13, 1, 3),
    Monkey(deque([74]), add(3), 17, 0, 1),
]


def round(monkeys: list[Monkey], counts: list[int]):
    for monkey_i in range(len(monkeys)):
        turn(monkeys, counts, monkey_i)


MOD_FACTOR = reduce(
    lambda a, m: a*m.test_divisible_by, real_monkeys, 1)


def turn(monkeys: list[Monkey], counts: list[int], monkey_i: int):
    monkey = monkeys[monkey_i]
    while monkey.items:
        counts[monkey_i] += 1

        item = monkey.items.popleft()
        item = monkey.op(item)
        # item = item // 3
        item = item % MOD_FACTOR

        if item % monkey.test_divisible_by == 0:
            dst = monkey.on_true
        else:
            dst = monkey.on_false

        monkeys[dst].items.append(item)


def business(monkeys, rounds):
    counts = [0] * len(monkeys)
    for i in range(rounds):
        round(monkeys, counts)

    counts.sort()
    return counts[-1] * counts[-2]


print(business(real_monkeys, 10000))
