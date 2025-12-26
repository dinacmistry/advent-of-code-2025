"Day 1: Dial part 2"
import numpy as np
import timeit

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

        direction = i[0]
        step = i[1:]
        old_y = y
        if direction == "L":
            y = y - int(step)

        else:
            y = y + int(step)

        range_min = min(y, old_y)
        range_max = max(y, old_y)
        clicks_at_x = [x for x in range(range_min, range_max) if x % 100 == 0]
        number_of_clicks_per_step = len(clicks_at_x)

        if y != old_y:
            if y % 100 == 0:
                count_of_zeros += 1
            if old_y % 100 == 0:
                count_of_zeros += number_of_clicks_per_step - 1
            else:
                count_of_zeros += number_of_clicks_per_step

        y = y % 100

    return y, count_of_zeros

def get_new_password(instructions, starting_point):
    y = starting_point
    count_of_zeros = 0

    for n, i in enumerate(instructions):
        direction = i[0]
        step = i[1:]
        old_y = y
        if direction == "L":
            y = y - int(step)
        else:
            y = y + int(step)

        range_min = min(y, old_y)
        range_max = max(y, old_y)

        # find the nearest multiple of 100 above the minimum value
        closest_multiple_100 = -(-range_min // 100) * 100
        clicks_at_x = [x for x in range(closest_multiple_100, range_max + 1, 100)]
        number_of_clicks_per_step = len(clicks_at_x)

        if y != old_y:
            if old_y % 100 == 0:
                count_of_zeros += (number_of_clicks_per_step - 1)
            else:
                count_of_zeros += number_of_clicks_per_step 

        y = y % 100
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
    assert test_y == expected_y, "dial point wrong"
    assert test_password == expected_password, "password wrong"

    test_y, test_password = get_new_password(test_instructions, starting_point)
    assert test_y == expected_y, "dial point wrong in quicker method"
    assert test_password == expected_password, "password wrong in quicker method"


    # actual use
    starting_point = 50
    filename = "day-1-dial-input.txt"
    instructions = parse_input(filename)


    y, password = get_new_password(instructions, starting_point)
    print(f"y: {y}, password: {password}")

    # test speed
    def solution_1():
        y, password = get_password_0x434C49434B(instructions, starting_point)

    def solution_2():
        y, password = get_new_password(instructions, starting_point)
    


    execution_time_1 = timeit.timeit("solution_1", setup="from __main__ import solution_1", number=10000)
    execution_time_2 = timeit.timeit("solution_2", setup="from __main__ import solution_2", number=10000)

    print(execution_time_1)
    print(execution_time_2)




