import sys
input = open(sys.argv[1], 'r').read()

games = list(map(lambda g: (g[0], g[2]), input.split("\n")))


def score(game):
    # 1 for Rock, 2 for Paper, and 3 for Scissors
    # 0 if you lost, 3 if the round was a draw, and 6 if you won

    (them, us) = game
    # A for Rock, B for Paper, and C for Scissors
    them = ord(them) - ord('A') + 1

    # X for Rock, Y for Paper, and Z for Scissors
    us = ord(us) - ord('X') + 1

    # There's a modulus math trick in here somewhere -- us - them % 4 + 1 or
    # something similar.

    winner = None  # in case I missed a case
    if us == them:
        winner = 3
    elif us == 1 and them == 3:
        winner = 6
    elif us == 2 and them == 1:
        winner = 6
    elif us == 3 and them == 2:
        winner = 6
    else:
        winner = 0

    return winner + us


# part 1
print(sum(map(score, games)))


def score2(game):
    # 1 for Rock, 2 for Paper, and 3 for Scissors

    (them, winner) = game
    # A for Rock, B for Paper, and C for Scissors
    them = ord(them) - ord('A') + 1

    # X for Rock, Y for Paper, and Z for Scissors
    winner = (ord(winner) - ord('X')) * 3

    us = None
    if winner is 0:  # we lost
        us = them - 1
        if us == 0:
            us = 3
    elif winner is 3:  # we tied
        us = them
    else:  # we won!
        us = them + 1
        if us == 4:
            us = 1

    return winner + us


# part 1
print(sum(map(score2, games)))
