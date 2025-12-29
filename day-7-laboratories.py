"Day 7: Tachyons"
import copy

def parse_manifold(text):

    manifold = []
    split_string = text.split('\n')

    for i in split_string:
        if len(i) > 0:
            manifold.append(i)

    return manifold


def split_beams(manifold):

    # find where the beam starts
    first_array = manifold[0]
    beam_spot = first_array.index("S")
    analyzed_manifold = copy.deepcopy(manifold)

    # propagate the beam to the next
    next_index = 1
    line = list(manifold[next_index])
    if line[beam_spot] == ".":
        line[beam_spot] = "|"
    line = "".join(line)
    analyzed_manifold[next_index] = line


    for n in range(1, len(analyzed_manifold) - 1):

        beam_spots = []
        splitter_spots = []
        for i in range(len(analyzed_manifold[n])):
            if analyzed_manifold[n][i] == "|":
                beam_spots.append(i)
            if analyzed_manifold[n + 1][i] == "^":
                splitter_spots.append(i)

        next_beam_spots = []
        for i in beam_spots:
            if i in splitter_spots:
                if (i - 1 >= 0) and analyzed_manifold[n+1][i - 1] == ".":
                    next_beam_spots.append(i - 1)
                if (i + 1 < len(analyzed_manifold[n + 1])) and analyzed_manifold[n+1][i+1] == ".":
                    next_beam_spots.append(i + 1)
            else:
                if analyzed_manifold[n+1][i] == ".":
                    next_beam_spots.append(i)

        next_beam_spots = set(next_beam_spots)
        next_beam_spots = sorted(next_beam_spots)

        next_line = list(analyzed_manifold[n + 1])
        for i in next_beam_spots:
            next_line[i] = "|"
        next_line = "".join(next_line)
        analyzed_manifold[n+1] = next_line

    return analyzed_manifold

def quantum_tachyon_timelines(manifold):
    split_manifold = copy.deepcopy(manifold)

    beam_spot = split_manifold[0].index("S")
    next_index = 1
    next_line = list(split_manifold[next_index])
    for i in [beam_spot]:
        if next_line[i] == ".":
            next_line[i] = 1
    split_manifold[next_index] = next_line


    for n in range(1, len(split_manifold) - 1):
        beam_spots = []
        splitter_spots = []
        for i in range(len(split_manifold[n])):
            if isinstance(split_manifold[n][i], int):
                beam_spots.append(i)
            if split_manifold[n + 1][i] == "^":
                splitter_spots.append(i)


        next_line = list(split_manifold[n + 1])
        for i in beam_spots:
            if i in splitter_spots:
                if (i - 1 >= 0):
                    if next_line[i - 1] == ".":
                        next_line[i - 1] = split_manifold[n][i]
                    elif isinstance(next_line[i-1], int):
                        next_line[i - 1] += split_manifold[n][i]
                    elif next_line[i - 1] == "^":
                        pass
                if (i + 1 < len(split_manifold[n + 1])):
                    if next_line[i + 1] == ".":
                        next_line[i + 1] = split_manifold[n][i]
                    elif next_line[i + 1] == "^":
                        pass
                    elif isinstance(next_line[i + 1], int):
                        next_line[i + 1] += split_manifold[n][i]
            elif i not in splitter_spots:
                if next_line[i] == ".":
                    next_line[i] = split_manifold[n][i]
                elif isinstance(next_line[i], int):
                    next_line[i] += split_manifold[n][i]
        split_manifold[n + 1] = next_line

    count_of_timelines = sum([i for i in split_manifold[-1] if isinstance(i, int)])
    return count_of_timelines




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


    filename = "day-7-small-manifold.txt"
    pre_split_text = parse_manifold(filename)
    with open(filename, 'r') as f:
        contents = f.read()
    f.close()

    manifold = parse_manifold(contents)
    split_beams_manifold = split_beams(manifold)
    split_beams_manifold_test = parse_manifold(text)

    assert split_beams_manifold == split_beams_manifold_test, "wrong split manifold"

    expected = 21
    test_answer = analyze_manifold(split_beams_manifold_test)

    assert test_answer == expected, "wrong number of split beams"
    print("Number of split beams in test", test_answer)

    assert analyze_manifold(split_beams_manifold) == expected, "wrong split manifolds"


    count_of_timelines = quantum_tachyon_timelines(manifold)
    expected_timelines = 40

    assert count_of_timelines == expected_timelines, f"wrong count of timelines {count_of_timelines}"



    filename = "day-7-manifold.txt"
    with open(filename, 'r') as f:
        contents = f.read()
    f.close()

    manifold = parse_manifold(contents)
    split_beams_manifold = split_beams(manifold)
    count_of_split_beams = analyze_manifold(split_beams_manifold)
    print("count of split beams", count_of_split_beams)

    count_of_timelines = quantum_tachyon_timelines(manifold)
    print("count of timelines", count_of_timelines)



