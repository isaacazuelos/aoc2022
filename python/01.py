import sys
input = open(sys.argv[1], 'r').read()
elves = (list(map(int, line.split("\n"))) for line in input.split("\n\n"))
calories = list(map(sum, elves))
calories.sort()
print(sum(calories[-3:]))
