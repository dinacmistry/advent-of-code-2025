"Day 10: Factory"
import copy
import numpy as np
import itertools
from collections import Counter

def parse_inputs(input_string):

    final_lights = []
    buttons = []
    joltages = []
    split_string = input_string.split("\n")

    for i in split_string:
        line = [l for l in i.split(" ") if l != '']

        if len(line) > 0:
            final_lights.append(list(line[0].strip("[]")))
            joltages.append([int(i) for i in line[-1].strip("{}").split(",")])
            button_set = [ [int(j) for j in i.strip("()").split(",")] for i in line[1:-1]]
            buttons.append(button_set)

    return final_lights, buttons, joltages


def press_button(light_rack, button):
    # print("light rack", light_rack)
    # print("button", button)
    if len(button) < 1:
        return light_rack
    else:
        update_lights = [-light_rack[n] if n in button else light_rack[n] for n, i in enumerate(light_rack)]
        # print(update_lights)
        return update_lights

def combine_buttons(choosen_buttons):
    combined_buttons = [light_index for button in choosen_buttons for light_index in button]
    index_count = Counter(combined_buttons)
    # print(combined_buttons)
    # print(index_count)
    new_combined_buttons = [i for i in index_count if index_count[i] % 2 == 1]
    return new_combined_buttons

def ways_to_press_buttons(button_set, num_buttons):
    ways = list(itertools.combinations_with_replacement(button_set, num_buttons))
    return ways


def ways_to_turn_on_lights(final_light_rack, button_set):

    num_lights = len(final_light_rack)
    initial_light_rack = ["." for i in range(num_lights)]
    initial_numerical_light_rack = [-1 if i == "." else 1 for i in initial_light_rack]
    final_numerical_light_rack = [-1 if i == "." else 1 for i in final_light_rack]

    # print(initial_numerical_light_rack)
    # print(final_numerical_light_rack)

    press_button(initial_numerical_light_rack, button_set[0])

    num_button_range = np.arange(0, 9)

    ways_that_work = []

    number_minimum_buttons_found = False

    for num_buttons in num_button_range:
        ways = ways_to_press_buttons(button_set, num_buttons)

        for way in ways:
            combined_buttons = combine_buttons(way)
            candidate_numerical_light_rack = press_button(initial_numerical_light_rack, combined_buttons)
            if np.array_equal(candidate_numerical_light_rack, final_numerical_light_rack):
                ways_that_work.append(way)
        if len(ways_that_work) > 0:
            number_minimum_buttons_found = True
        if number_minimum_buttons_found:
            break

    # print("\nways that work")
    # print(ways_that_work)
    # for way in ways_that_work:
    #     print(way)
    all_same_length = [ len(ways_that_work[0]) == len(way) for way in ways_that_work]
    if False in all_same_length:
        print("STOP")

    # if len(ways_that_work) > 0:
    #     print("number of ways to press buttons found")
    # else:
    #     print("number of ways to press buttons not found!")

    return ways_that_work


def get_minimum_number_of_button_presses(final_lights, buttons):

    minimum_buttons_to_press_for_all_lights = 0
    minimum_button_lengths = []
    for n, i in enumerate(final_lights):
        minimum_ways_for_light_rack = ways_to_turn_on_lights(final_lights[n], buttons[n])
        minimum_buttons_to_press_for_light_rack = len(minimum_ways_for_light_rack[0])
        minimum_buttons_to_press_for_all_lights += minimum_buttons_to_press_for_light_rack
        # print("light", n)
        # print(buttons[n])
        # print(minimum_buttons_to_press_for_light_rack)
        minimum_button_lengths.append(len(minimum_ways_for_light_rack[0]))

    # print(minimum_button_lengths)
    # print(sum(minimum_button_lengths))
    return minimum_buttons_to_press_for_all_lights


if __name__ == '__main__':
    
    filename = "day-10-indicator-lights-test.txt"

    with open(filename, 'r') as f:
        contents = f.read()
    f.close()


    final_lights, buttons, joltages = parse_inputs(contents)

    minimum_buttons_to_press_for_all_lights = get_minimum_number_of_button_presses(final_lights, buttons)
    print("\nTest set: minimum number of buttons to press", minimum_buttons_to_press_for_all_lights)

    expected = 7
    assert minimum_buttons_to_press_for_all_lights == expected, "wrong number of minimum buttons!"



    filename = "day-10-indicator-lights.txt"

    with open(filename, 'r') as f:
        contents = f.read()
    f.close()

    final_lights, buttons, joltages = parse_inputs(contents)

    minimum_buttons_to_press_for_all_lights = get_minimum_number_of_button_presses(final_lights, buttons)
    print("\nMinimum number of buttons to press", minimum_buttons_to_press_for_all_lights)





