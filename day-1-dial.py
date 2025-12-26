"Day 1: Dial"


def parse_input(filename):
    with open(filename, 'r') as f:
        contents = f.read()

    contents = contents.split("\n")
    empty = ['']
    contents = [i for i in contents if i not in empty]

    return contents


def get_password(instructions, starting_point):
    y = starting_point
    count_of_zeros = 0
    for n, i in enumerate(instructions):
        direction = i[0]
        step = i[1:]
        if direction == "L":
            y = y - int(step)

        else:
            y = y + int(step)

        y = y % 100

        if y == 0:
            count_of_zeros += 1

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
    expected_password = 3
    test_y, test_password = get_password(test_instructions, starting_point)
    # print(test_y, test_password)

    assert test_y == expected_y, "dial point wrong"
    assert test_password == expected_password, "password wrong"


    # actual use case
    starting_point = 50

    filename = "day-1-dial-input.txt" # actual instructions
    instructions = parse_input(filename)

    # print(instructions)
    # print(len(instructions))

    y, password = get_password(instructions, starting_point)
    print(f"y: {y}, password: {password}")


