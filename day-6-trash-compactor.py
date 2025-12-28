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
    digits = [ [] for c in range(ncols)]

    for i in split_string:
        if ("+" in i) or ("*" in i):
            instructions = list(i)
        else:
            line = list(i)
            line = ['' if l == " " else l for l in line]
            for n, l in enumerate(line):
                if l != "":
                    digits[n].append(l)

    has_instructions = [l == "+" or l == "*" for l in instructions]
    has_instructions = np.arange(len(instructions))[has_instructions]

    numbers = []
    for c in range(ncols):
        col = digits[c]
        number = sum([int(i) * 10 ** (len(col) - (1 + n)) for n, i in enumerate(col)])
        numbers.append(number)

    return numbers, instructions, has_instructions



def cephalopod_homework(numbers, instructions):
    solutions = []

    for i in range(len(instructions)):
        if instructions[i] == "*":
            answer = np.prod(numbers[:, i])
        elif instructions[i] == "+":
            answer = sum(numbers[:, i])

        solutions.append(answer)
    return sum(solutions)

def fixed_cephalopod_homework(numbers, instructions, has_instructions):
    solutions = []
    for n in range(len(has_instructions) - 1):

        start = has_instructions[n]
        stop = has_instructions[n+1]
        instruction = instructions[start]

        answer = [numbers[i] for i in range(start, stop) if numbers[i] != 0]
        if instruction == "*":
            answer = np.prod(answer)
        elif instruction == "+":
            answer = np.sum(answer)
        solutions.append(answer)

    # last set of numbers
    start = has_instructions[-1]
    stop = len(numbers)
    instruction = instructions[start]

    answer = [numbers[i] for i in range(start, stop) if numbers[i] != 0]
    if instruction == "*":
        answer = np.prod(answer)
    elif instruction == "+":
        answer = np.sum(answer)
    solutions.append(answer)

    return solutions, sum(solutions)

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
    # print("Answer", answer)

    numbers, instructions, has_instructions = parse_like_cephalopod(test)
    # print(numbers)
    # print(instructions)
    # print(has_instructions)

    solutions, sum_of_solutions = fixed_cephalopod_homework(numbers, instructions, has_instructions)
    expected_sum = 3263827
    assert sum_of_solutions == expected_sum, "wrong sum"



    filename = "day-6-input.txt"
    with open(filename, 'r') as f:
        contents = f.read()
    f.close()

    numbers, instructions = parse_inputs(contents)
    answer = cephalopod_homework(numbers, instructions)
    print("Answer to part 1", answer)

    numbers, instructions, has_instructions = parse_like_cephalopod(contents)
    solutions, sum_of_solutions = fixed_cephalopod_homework(numbers, instructions, has_instructions)
    # print(solutions)
    print("Solution to part 2", sum_of_solutions)










