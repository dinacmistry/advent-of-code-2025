"Day 2: Invalid IDs part 2"
import numpy as np


def parse_inputs(input_string):
    ranges = []
    split_string = input_string.split(",")

    for i in split_string:
        if "-" in i:
            r = i.split("-")
            start = r[0]
            stop = r[1]
            start, stop = int(start), int(stop)
            ranges.append((start, stop))

        else:
            continue

    return ranges


def get_factors(n):
    factors = []

    # minimum factor = 1
    factors.append(1)

    # maximum factor besides n: bounded by n/2
    # but you can get this factor as the complimentary factor with 2

    # the maximum factor that you can't reach as the complimentary
    # factor of a smaller factor would be the sqrt of n
    max_factor_possible = int(np.floor(np.sqrt(n)))

    for i in range(2, max_factor_possible + 1):
        if n % i == 0:
            factors.append(i)
            factors.append(n//i)

    factors = set(factors)

    return factors


def get_invalid_id(number):
    text = str(number)
    size = len(text)
    factors = get_factors(size)

    is_invalid_id = False

    # don't include single digit numbers
    if size > 1:

        for f in factors:
            chunks = [text[i:i+f] for i in range(0, size, f)]
            target_chunk = chunks[0]
            result = all(item == target_chunk for item in chunks)
            if result:
                is_invalid_id = True
                break

    return is_invalid_id


def get_invalid_id_from_range(start, stop):

    invalid_ids = []

    x = range(start, stop + 1)
    for i in x:
        is_invalid_id = get_invalid_id(i)
        if is_invalid_id:
            invalid_ids.append(i)

    return invalid_ids


def get_invalid_ids_from_input(input_string, invalid_ids):
    ranges = parse_inputs(input_string)
    for r in ranges:
        start = r[0]
        stop = r[1]
        invalid_ids += get_invalid_id_from_range(start, stop)

    return invalid_ids


if __name__ == '__main__':

    # test input
    text_input = ""
    text_input += "11-22,"
    text_input += "95-115,"
    text_input += "998-1012,"
    text_input += "1188511880-1188511890,"
    text_input += "222220-222224,"
    text_input += "16988522-16988528,"
    text_input += "446443-446449,"
    text_input += "38593856-38593862,"
    text_input += "565653-565659,"
    text_input += "824824821-824824827,"
    text_input += "2121212118-2121212124"

    invalid_ids = []
    invalid_ids = get_invalid_ids_from_input(text_input, invalid_ids)

    print("sum of invalid ids in test set", sum(invalid_ids))

    expected_sum = 4174379265
    assert sum(invalid_ids) == expected_sum, "Wrong sum"

    filename = "day-2-input.txt"
    with open(filename, 'r') as f:
        contents = f.read()
    f.close()

    invalid_ids = []
    invalid_ids = get_invalid_ids_from_input(contents, invalid_ids)

    invalid_id_sum = sum(invalid_ids)
    print("sum of invalid ids", invalid_id_sum)




