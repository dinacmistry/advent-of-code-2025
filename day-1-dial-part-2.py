"Day 1: Dial part 2"
import numpy as np


def parse_input(filename):
    with open(filename, 'r') as f:
        contents = f.read()

    contents = contents.split("\n")
    empty = ['']
    contents = [i for i in contents if i not in empty]

    return contents

def get_password_0x434C49434B(instructions, starting_point):
    y = starting_point
    count_of_zeros = 0
    for n, i in enumerate(instructions):
        # print("old", n, i, y)
        print()
        direction = i[0]
        step = i[1:]
        old_y = y
        if direction == "L":
            y = y - int(step)

        else:
            y = y + int(step)

        print("new", n, i, y, old_y)
        range_min = min(y, old_y)
        range_max = max(y, old_y)
        clicks_at_x = [x for x in range(range_min, range_max) if x % 100 == 0]
        print("clicks_at_x", clicks_at_x)
        number_of_clicks_per_step = len(clicks_at_x)

        y = y % 100
        print("final", n, i, y, old_y, range_min, range_max, clicks_at_x)

        if y == 0:
            count_of_zeros += 1
            print("adding 1", count_of_zeros)
        else:
            count_of_zeros += number_of_clicks_per_step
            print("adding", number_of_clicks_per_step, count_of_zeros)

    return y, count_of_zeros


if __name__ == '__main__':
    
    starting_point = 50

    # testing against easy case
    test_instructions = [
    "L68", 
    "L30",
    "R48",
    "L5",
    "R60",
    "L55",
    "L1",
    "L99",
    "R14",
    "L82",
    ]


expected_y = 32
expected_password = 6

test_y, test_password = get_password_0x434C49434B(test_instructions, starting_point)
print(test_y, test_password)



