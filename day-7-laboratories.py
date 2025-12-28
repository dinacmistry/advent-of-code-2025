"Day 7: Tachyons"


def parse_manifold(text):

    manifold = []
    split_string = text.split('\n')

    for i in split_string:
        # manifold.append(list(i))
        if len(i) > 0:
            manifold.append(i)

    return manifold


def split_beams(manifold):
    # pass

    # find where the beam starts
    first_array = manifold[0]
    beam_spot = first_array.index("S")
    print(first_array[beam_spot])


def analyze_manifold(manifold):

    count_of_split_beams = 0

    for n in range(len(manifold)):
        if n > 1:
            indices = []
            start_index = 0

            while True:
                try:
                    # search from the starting index
                    index = manifold[n].index("^", start_index)
                    indices.append(index)

                    # move the starting index ahead to find the next one
                    start_index = index + 1

                except ValueError:
                    # break out of the loop if "^" isn't found and ValueError
                    # gets raised because the starting index is too high to
                    # search the string in manifold[n]
                    break
            splitter_spots = indices
            # gets split
            for index in indices:
                if manifold[n-1][index] == "|":
                    count_of_split_beams += 1
    return count_of_split_beams



if __name__ == '__main__':
    
    text = ""
    text += ".......S.......\n"
    text += ".......|.......\n"
    text += "......|^|......\n"
    text += "......|.|......\n"
    text += ".....|^|^|.....\n"
    text += ".....|.|.|.....\n"
    text += "....|^|^|^|....\n"
    text += "....|.|.|.|....\n"
    text += "...|^|^|||^|...\n"
    text += "...|.|.|||.|...\n"
    text += "..|^|^|||^|^|..\n"
    text += "..|.|.|||.|.|..\n"
    text += ".|^|||^||.||^|.\n"
    text += ".|.|||.||.||.|.\n"
    text += "|^|^|^|^|^|||^|\n"
    text += "|.|.|.|.|.|||.|\n"

    manifold = parse_manifold(text)
    expected = 21
    test_answer = analyze_manifold(manifold)

    assert test_answer == expected, "wrong number of split beams"
    print("Number of split beams in test", test_answer)


    filename = "day-7-manifold.txt"
    with open(filename, 'r') as f:
        contents = f.read()
    f.close()

    manifold = parse_manifold(contents)
    # print(manifold)

    for a in manifold:
        print(a)
    # count_of_split_beams = analyze_manifold(manifold)
    # print("Number of split beams", count_of_split_beams)

    split_beams(manifold)



