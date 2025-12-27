"Day 3: Lobby part 2"
import numpy as np

def parse_inputs(input_string):
    banks = []

    split_string = input_string.split("\n")
    for i in split_string:
        if len(i) > 0:
            banks.append(i)
    return banks


def get_joltage(bank, expected_length):
    digits = []

    new_bank = bank

    while len(digits) < expected_length:

        explore_up_to = len(new_bank) - (expected_length - len(digits))

        explore_digits = [int(i) for i in new_bank[0:explore_up_to + 1]]
        next_digit = max(explore_digits)
        next_digit_index = new_bank[0:explore_up_to + 1].index(str(next_digit))

        new_bank = new_bank[next_digit_index + 1:]
        digits.append(next_digit)

    number = [i * 10 ** (len(digits) - (n + 1)) for n, i in enumerate(digits)]
    number = sum(number)
    return number



if __name__ == '__main__':

    test_input = ""
    test_input += "987654321111111\n"
    test_input += "811111111111119\n"
    test_input += "234234234234278\n"
    test_input += "818181911112111\n"

    test_banks = parse_inputs(test_input)


    expected_length = 12
    test_joltages = []

    for bank in test_banks:
        joltage = get_joltage(bank, expected_length)
        print(joltage)
        test_joltages.append(joltage)

    print("test joltage total", sum(test_joltages))

    expected_joltage = 3121910778619
    assert sum(test_joltages) == expected_joltage, "wrong sum"

    
    filename = "day-3-lobby-banks.txt"
    with open(filename, 'r') as f:
        contents = f.read()
    f.close()


    # actual battery banks
    expected_length = 12
    joltages = []
    banks = parse_inputs(contents)
    for bank in banks:
        joltage = get_joltage(bank, expected_length)
        joltages.append(joltage)

    print('total battery joltage', sum(joltages))


