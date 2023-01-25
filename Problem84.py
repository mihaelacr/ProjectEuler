import random

from itertools import count


boardtxt = """go a1 cc1 a2 t1 r1 b1 ch1 b2 b3 jail c1 u1 c2 c3 r2 d1 cc2 d2 d3
              fp e1 ch2 e2 e3 r3 f1 f2 u2 f3 g2j g1 g2 cc3 g3 r4 ch3 h1 t2 h2"""
board = boardtxt.split()

JAIL = board.index("jail")
GO = board.index("go")

NPLACES = len(board)
NSIDES = 4

position = 0

chances = list(range(1, 17))
chests = list(range(1, 17))


def next_starting_with(cur_position, start_match):
    """Return the next position on the board starting with a given string"""
    next_idx = next(
        filter(
            lambda x: board[x % NPLACES].startswith(start_match),
            count(cur_position + 1),
        )
    )
    return next_idx % NPLACES


def community_chest(cur_position):
    # This will take from the top and put
    # to the bottom of the pile. I guess
    # that affects things a bit since there
    # will be a fixed gap until a card comes
    # back around, but just picking randomly
    # each times also gives the same results
    r = chests[0]
    chests.append(r)
    del chests[0]

    match r:
        case 1:
            return GO
        case 2:
            return JAIL
        case other:
            return cur_position


def chance(cur_position):
    r = chances[0]
    chances.append(r)
    del chances[0]

    match r:
        case 1:
            return GO
        case 2:
            return JAIL
        case 3:
            return board.index("c1")
        case 4:
            return board.index("e3")
        case 5:
            return board.index("h2")
        case 6:
            return board.index("r1")
        case 7 | 8:
            return next_starting_with(cur_position, "r")
        case 9:
            return next_starting_with(cur_position, "u")
        case 10:
            print(f"Back 3 before {board[cur_position]}")
            return (cur_position - 3) % NPLACES
        case _:
            return cur_position


def position_effect(cur_position):
    match board[cur_position]:
        case "g2j":
            return JAIL
        case "cc1" | "cc2" | "cc3":
            return community_chest(cur_position)
        case "ch1" | "ch2" | "ch3":
            return chance(cur_position)
        case _:
            return cur_position


def roll():
    d1 = random.randint(1, NSIDES)
    d2 = random.randint(1, NSIDES)
    return d1 + d2, d1 == d2


position_counts = {p: 0 for p in board}


for game in range(10):
    # Not sure shuffling really matters
    random.shuffle(chances)
    random.shuffle(chests)
    last_three_doubles_condition = [False, False, False]

    for i in range(500000):
        r, dubs = roll()

        last_three_doubles_condition.append(dubs)
        del last_three_doubles_condition[0]

        position = (position + r) % len(board)

        if all(last_three_doubles_condition):
            print("THREE DOUBLES :(")
            position = JAIL
            last_three_doubles_condition[-1] = False

        position_name = board[position]

        while True:
            changed_position = position_effect(position)

            if changed_position == position:
                break
            else:
                position = changed_position
                print(f"{i} Position changed to {board[position]}")

        position_counts[board[position]] += 1

freqs = [(v / sum(position_counts.values()), k) for k, v in position_counts.items()]
sorted_freqs = sorted(freqs, reverse=True)

print("Frequencies:")
for f in sorted_freqs[:5]:
    print(f[0], f[1], board.index(f[1]))
