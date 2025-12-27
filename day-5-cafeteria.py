"Day 5: Cafeteria"
import numpy as np

def parse_ingredient_ranges(input_string):
    ingredient_ranges = []
    split_string = input_string.split("\n")
    for i in split_string:
        if "-" in i:
            r = i.split("-")
            start = r[0]
            stop = r[1]
            start, stop = int(start), int(stop)
            ingredient_ranges.append((start, stop))


    return ingredient_ranges


def parse_available_ingredients(input_string):
    available_ingredients = set()
    split_string = input_string.split("\n")
    for i in split_string:
        if "-" not in i:
            if len(i) > 0:
                available_ingredients.add(int(i))

    return available_ingredients


def get_all_fresh_ingredients(ingredient_ranges):
    all_fresh_ingredients = set()

    for irange in ingredient_ranges:
        start, stop = irange

        all_fresh_ingredients = all_fresh_ingredients.union([i for i in range(start, stop + 1)])

    return all_fresh_ingredients


def get_all_fresh_and_available_ingredients(ingredient_ranges, available_ingredients):
    all_fresh_and_available = []
    ingredient_ranges = np.array(ingredient_ranges)

    for n, a in enumerate(available_ingredients): 
        ranges_lower_than_a = ingredient_ranges[:, 0] <= a
        ranges_higher_than_a = ingredient_ranges[:, 1] >= a

        compare_results = [a == b and a == True for a, b in zip(ranges_lower_than_a, ranges_higher_than_a)]
        
        is_fresh_and_available = np.sum(compare_results)
        if is_fresh_and_available:
            all_fresh_and_available.append(a)

    return all_fresh_and_available


if __name__ == '__main__':
    
    ingredient_ranges_text = ""
    ingredient_ranges_text += "3-5\n"
    ingredient_ranges_text += "10-14\n"
    ingredient_ranges_text += "16-20\n"
    ingredient_ranges_text += "12-18\n"


    available_text = ""
    available_text += "1\n"
    available_text += "5\n"
    available_text += "8\n"
    available_text += "11\n"
    available_text += "17\n"
    available_text += "32\n"

    ingredient_ranges = parse_ingredient_ranges(ingredient_ranges_text)
    print(ingredient_ranges)

    available_ingredients = parse_available_ingredients(available_text)
    print(available_ingredients)

    all_fresh_ingredients = get_all_fresh_ingredients(ingredient_ranges)
    print(all_fresh_ingredients)

    all_fresh_and_available = get_all_fresh_and_available_ingredients(ingredient_ranges, available_ingredients)
    print(all_fresh_and_available)

    print(len(all_fresh_and_available))




    filename = "day-5-cafeteria-input.txt"
    with open(filename, 'r') as f:
        contents = f.read()
    f.close()

    ingredient_ranges = parse_ingredient_ranges(contents)
    ingredient_ranges = np.array(ingredient_ranges)
    available_ingredients = parse_available_ingredients(contents)

    print(len(ingredient_ranges))

    all_fresh_and_available = get_all_fresh_and_available_ingredients(ingredient_ranges, available_ingredients)

    print("actual number of fresh and available ingredients", len(all_fresh_and_available))




