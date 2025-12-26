"Day 2"


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


def get_invalid_ids(start, stop):
    invalid_ids = []
    x = range(start, stop + 1)
    for i in x:
        text = str(i)
        size = len(text)

        if size % 2 == 0:
            halfsize = int(size/2)

        else:
            continue

        half = text[0:halfsize]
        if text[0:halfsize] == text[halfsize:]:
            invalid_ids.append(i)

    return invalid_ids


def get_invalid_ids_from_input(input_string, invalid_ids):
    ranges = parse_inputs(input_string)
    for r in ranges:
        start = r[0]
        stop = r[1]

        invalid_ids += get_invalid_ids(start, stop)
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

    ranges = parse_inputs(text_input)

    invalid_ids = []
    invalid_ids = get_invalid_ids_from_input(text_input, invalid_ids)

    print(f"invalid_ids: {invalid_ids}")
    print(f"sum of invalid_ids: {sum(invalid_ids)}")

    expected_sum = 1227775554
    assert sum(invalid_ids) == expected_sum



    filename = "day-2-input.txt"
    with open(filename, 'r') as f:
        contents = f.read()
    # ranges = parse_inputs(f)
    # f.close()

    invalid_ids = []
    invalid_ids = get_invalid_ids_from_input(contents, invalid_ids)
    f.close()

    invalid_id_sum = sum(invalid_ids)
    print(invalid_id_sum)







