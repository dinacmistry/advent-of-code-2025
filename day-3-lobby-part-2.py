"Day 3: Lobby part 2"
import numpy as np

def parse_inputs(input_string):
    banks = []

    split_string = input_string.split("\n")
    for i in split_string:
        if len(i) > 0:
            banks.append(i)
    return banks


if __name__ == '__main__':

    test_input = ""
    test_input += "987654321111111\n"
    test_input += "811111111111119\n"
    test_input += "234234234234278\n"
    test_input += "818181911112111\n"

    test_banks = parse_inputs(test_input)



    
    filename = "day-3-lobby-banks.txt"
    with open(filename, 'r') as f:
        contents = f.read()
    f.close()

    banks = parse_inputs(contents)
    # for bank in banks:
