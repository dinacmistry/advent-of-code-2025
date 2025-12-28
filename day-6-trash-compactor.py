"Day 6: Trash Compactor"
import numpy as np

def parse_inputs(input_string):
    numbers = []
    split_string = input_string.split("\n")

    instructions = []

    for i in split_string:
        line = i.split(" ")
        line = [x for x in line if x != ""]
        if ("+" in i) or ("*" in i):
            instructions = line
        else:
            line = [int(x) for x in line if x != ""]
            if len(line) > 0:
                numbers.append(line)

    numbers = np.array(numbers)
    return numbers, instructions


def parse_like_cephalopod(input_string):

    split_string = input_string.split("\n")

    ncols = len(split_string[0])
    print(ncols)

    numbers = [ [] for c in range(ncols)]
    # print(numbers)

    for i in split_string:
        if ("+" in i) or ("*" in i):
            instructions = list(i)

    has_instructions = [l == "+" or l == "*" for l in instructions]
    has_instructions = np.arange(len(instructions))[has_instructions]
    print(has_instructions)
    
    


def cephalopod_homework(numbers, instructions):
    solutions = []

    for i in range(len(instructions)):
        if instructions[i] == "*":
            answer = np.prod(numbers[:, i])
        elif instructions[i] == "+":
            answer = sum(numbers[:, i])

        solutions.append(answer)
    return sum(solutions)

def fixed_cephalopod_homework(numbers, instructions):
    solutions = []

    return sum(solutions)


if __name__ == '__main__':
    
    test = ""
    test += "123 328  51 64 \n"
    test += " 45 64  387 23 \n"
    test += "  6 98  215 314\n"
    test += "*   +   *   +  \n"


    numbers, instructions = parse_inputs(test)

    expected = 4277556
    answer = cephalopod_homework(numbers, instructions)
    assert answer == expected, 'wrong sum'
    print("Answer", answer)


    filename = "day-6-input.txt"
    with open(filename, 'r') as f:
        contents = f.read()
    f.close()

    numbers, instructions = parse_inputs(contents)
    answer = cephalopod_homework(numbers, instructions)
    print("Answer", answer)



    parse_like_cephalopod(test)

