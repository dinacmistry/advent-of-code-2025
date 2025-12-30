"Day 8: Playground"
import numpy as np
import copy

def parse_input(input_string):
    positions = []
    split_string = input_string.split("\n")
    for i in split_string:
        pos = i.split(",")
        if len(pos) == 3:
            x,y,z = pos
            x,y,z = int(x), int(y), int(z)
            positions.append([x,y,z])
        elif len(pos) == 0:
            pass
        else:
            print(i)
            pass
    return positions

def get_distance_sqrd(p1, p2):
    distance_sqrd = sum([(p1[i] - p2[i]) ** 2 for i in range(len(p1))])
    return distance_sqrd


def find_circuit(junction, circuits):
    for c, circuit in enumerate(circuits):
        if junction in circuit:
            return c
    return None


def connect_junctions(junctions, merge_cap, top_n):
    # pairs of junction ids with their distances
    all_pairs_with_distances = []

    for i in range(len(junctions)):
        junction_i = junctions[i]
        for j in range(i+1, len(junctions)):
            junction_j = junctions[j]
            distance = get_distance_sqrd(junction_i, junction_j)
            all_pairs_with_distances.append([distance, i, j])

    # sort pairs by distance
    sorted_pairs_with_distances = copy.deepcopy(all_pairs_with_distances)
    sorted_pairs_with_distances.sort()

    # put all junctions into their own circuit by id not position
    circuits = [{i} for i in range(len(junctions))]

    for n in range(merge_cap):
        distance, i, j = sorted_pairs_with_distances[n]
        ci = find_circuit(i, circuits)
        cj = find_circuit(j, circuits)

        # if the circuits aren't the same, let's merge them
        if ci != cj:
            circuits[ci] = circuits[ci].union(circuits[cj])
            # now delete the second set because it got merged
            del circuits[cj]
    sorted_circuits = copy.deepcopy(circuits)
    sorted_circuits.sort(key = lambda circuit: len(circuit), reverse=True)

    top_n_circuit_lengths = [len(sorted_circuits[n]) for n in range(top_n)]
    return np.prod(top_n_circuit_lengths)

def connect_junctions_until_n_circuits(junctions):
    # pairs of junction ids with their distances
    all_pairs_with_distances = []
    for i in range(len(junctions)):
        junction_i = junctions[i]
        for j in range(i+1, len(junctions)):
            junction_j = junctions[j]
            distance = get_distance_sqrd(junction_i, junction_j)
            all_pairs_with_distances.append([distance, i, j])

    # sort pairs by distance
    # reverse order so we pop off the last pair in the list
    sorted_pairs_with_distances = copy.deepcopy(all_pairs_with_distances)
    sorted_pairs_with_distances.sort(reverse = True)

    # put all junctions into their own circuit by id not position
    circuits = [{i} for i in range(len(junctions))]

    # pop off the last value - it's the current pair with the smallest distance
    while len(circuits) > 1:
        distance, i, j = sorted_pairs_with_distances.pop()
        ci = find_circuit(i, circuits)
        cj = find_circuit(j, circuits)

        # if the circuits aren't the same, let's merge them
        if ci != cj:
            circuits[ci] = circuits[ci].union(circuits[cj])
            # now delete the second set because it got merged
            del circuits[cj]

    junction_i = junctions[i]
    junction_j = junctions[j]
    x_product = junction_i[0] * junction_j[0]
    return x_product


if __name__ == '__main__':
    
    test = "day-8-junction-boxes.txt"
    with open(test, 'r') as f:
        contents = f.read()
    f.close()
    junctions = parse_input(contents)
    junctions = list(junctions)

    merge_cap = 10
    top_n = 3

    expected = 40
    answer = connect_junctions(junctions, merge_cap, top_n)
    print(answer)
    assert answer == expected, "wrong product"


    filename = "day-8-junction-boxes-full.txt"
    with open(filename, 'r') as f:
        contents = f.read()
    f.close()
    junctions = parse_input(contents)
    junctions = list(junctions)

    merge_cap = 1000
    top_n = 3

    answer = connect_junctions(junctions, merge_cap, top_n)
    print("Product of three largest circuits", answer)


    x_product = connect_junctions_until_n_circuits(junctions)
    print("x product of last two junction boxes connected", x_product)
