# Three 1's => 1000 points
# Three 6's =>  600 points
# Three 5's =>  500 points
# Three 4's =>  400 points
# Three 3's =>  300 points
# Three 2's =>  200 points
# One   1   =>  100 points
# One   5   =>   50 point


def score(dice):

    # make counters for die rolls, points, and scoring
    points = 0

    die_counter = {
        1 : 0,
        2 : 0,
        3 : 0,
        4 : 0,
        5 : 0,
        6 : 0
    }

    triplets = {
        1 : 1000,
        6 : 600,
        5 : 500,
        4 : 400,
        3 : 300,
        2 : 200,
    }

    singles = {
        1 : 100,
        5 : 50
    }

    # count the die rolls
    for die in dice:
        die_counter[die] += 1

    # score the triplets
    for digit in die_counter.keys():
        if die_counter[digit] >= 3:
            points += triplets[digit]  # count the points
            die_counter[digit] -= 3  # subtract it from the counter

    # score the singles that are left
    for digit in die_counter.keys():
        if die_counter[digit] >= 1:
            try:
                points += singles[digit] * die_counter[digit]
            except KeyError:
                pass

    return points

print(score([2, 3, 4, 6, 2])) # 0
print(score([1, 5, 1, 3, 4])) # 250
print(score([6, 3, 1, 1, 4]))   # 200
