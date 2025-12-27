"Day 4: Printing part 1"
import numpy as np
import copy

def parse_inputs(input_string):
    rolls = []

    split_string = input_string.split("\n")
    for i in split_string:
        if len(i) > 0:
            rolls.append(i)

    return rolls

def convert_to_matrix(rolls):
    nrows = len(rolls)
    ncols  = len(rolls[0])

    matrix = np.zeros((nrows, ncols))

    for i in range(nrows):
        roll = rolls[i]
        roll = [r for r in roll]

        for j in range(ncols):
            spot = roll[j]
            if spot == '@':
                matrix[i][j] = 1

    return matrix


def get_adjacent_spots(i, j):

    adj_1 = i - 1, j
    adj_2 = i - 1, j + 1
    adj_3 = i, j + 1
    adj_4 = i + 1, j + 1
    adj_5 = i + 1, j
    adj_6 = i + 1, j - 1
    adj_7 = i, j - 1
    adj_8 = i - 1, j - 1

    adjacent_spots = (
        adj_1, adj_2, adj_3, adj_4,
        adj_5, adj_6, adj_7, adj_8
    )
    return adjacent_spots


def valid_spot(i, j, nrows, ncols):
    is_valid_spot = True
    if (i < 0) or (i >= nrows):
        is_valid_spot = False
    if (j < 0) or (j >= ncols):
        is_valid_spot = False

    return is_valid_spot


def get_valid_adjacent_spots(i, j, nrows, ncols):

    adjacent_spots = get_adjacent_spots(i, j)
    valid_adjacent_spots = []
    for adj in adjacent_spots:
        adj_i, adj_j = adj
        is_valid_spot = valid_spot(adj_i, adj_j, nrows, ncols)
        if is_valid_spot:
            valid_adjacent_spots.append(adj)

    return valid_adjacent_spots


def get_number_of_adjacent_rolls(i, j, nrows, ncols, matrix):

    valid_adjacent_spots = get_valid_adjacent_spots(i, j, nrows, ncols)

    number_of_adjacent_rolls = 0
    for adj in valid_adjacent_spots:
        adj_i, adj_j = adj
        number_of_adjacent_rolls += matrix[adj_i, adj_j]

    return int(number_of_adjacent_rolls)


def get_targeted_rolls(matrix, threshold):
    new_matrix = copy.deepcopy(matrix)

    nrows, ncols = matrix.shape
    for i in range(nrows):
        for j in range(ncols):

            number_of_adjacent_rolls = get_number_of_adjacent_rolls(i, j, nrows, ncols, matrix)
            if (number_of_adjacent_rolls < threshold) and (matrix[i, j]):
                new_matrix[i, j] = -1

    targeted_rolls = new_matrix < 0
    number_of_targeted_rolls = np.sum(targeted_rolls)

    return number_of_targeted_rolls




if __name__ == '__main__':
    
    test_input = ""
    test_input += "..@@.@@@@.\n"
    test_input += "@@@.@.@.@@\n"
    test_input += "@@@@@.@.@@\n"
    test_input += "@.@@@@..@.\n"
    test_input += "@@.@@@@.@@\n"
    test_input += ".@@@@@@@.@\n"
    test_input += ".@.@.@.@@@\n"
    test_input += "@.@@@.@@@@\n"
    test_input += ".@@@@@@@@.\n"
    test_input += "@.@.@@@.@.\n"


    rolls = parse_inputs(test_input)
    matrix = convert_to_matrix(rolls)

    nrows, ncols = matrix.shape
    threshold = 4

    number_of_targeted_rolls = get_targeted_rolls(matrix, threshold)
    print(number_of_targeted_rolls)
    expected_sum = 13

    assert number_of_targeted_rolls == expected_sum, "Wrong sum"


    # actual rolls
    filename = "day-4-printing-input.txt"
    with open(filename, 'r') as f:
        contents = f.read()
    f.close()

    rolls = parse_inputs(contents)

    matrix = convert_to_matrix(rolls)

    threshold = 4

    number_of_targeted_rolls = get_targeted_rolls(matrix, threshold)
    print(number_of_targeted_rolls)













