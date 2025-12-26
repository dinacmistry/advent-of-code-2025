"Day 3: Lobby part 1"


def parse_inputs(input_string):
    banks = []

    split_string = input_string.split("\n")
    for i in split_string:
        if len(i) > 0:
            banks.append(i)
    return banks


def find_top_n_values(number):
    # top two values
    digits = [int(i) for i in number]
    sorted_digits = sorted(digits)

    max_digit = sorted_digits[-1]
    max_digit_index = digits.index(max_digit)
    if max_digit_index == len(digits) - 1:
        max_digit = sorted_digits[-2]
        max_digit_index = digits.index(max_digit)

    following_digits = digits[max_digit_index+1:]

    # second highest digit after
    max_second_digit = max(following_digits)

    return max_digit, max_second_digit


def get_joltage(number):

    first_digit, second_digit = find_top_n_values(number)
    return first_digit * 10 + second_digit


def get_total_joltage(banks):
    joltages = []
    for number in banks:
        joltage = get_joltage(number)
        joltages.append(joltage)

    return joltages


if __name__ == '__main__':
    
    test_input = ""
    test_input += "987654321111111\n"
    test_input += "811111111111119\n"
    test_input += "234234234234278\n"
    test_input += "818181911112111\n"

    test_banks = parse_inputs(test_input)

    joltages = get_total_joltage(test_banks)
    print(f"test joltages: {joltages}")
    expected_joltage = 357
    assert sum(joltages) == expected_joltage, "Wrong joltage sum"


    # actual battery banks
    filename = "day-3-lobby-banks.txt"
    with open(filename, 'r') as f:
        contents = f.read()
    f.close()

    banks = parse_inputs(contents)
    joltages = get_total_joltage(banks)
    total_joltage = sum(joltages)
    print(f"total joltage: {total_joltage}")





