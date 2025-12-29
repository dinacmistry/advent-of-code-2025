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
            print("error")
    # positions = np.array(positions)
    return positions

def get_distance_sqrd(p1, p2):
    distance_sqrd = sum([(p1[i] - p2[i]) ** 2 for i in range(len(p1))])
    return distance_sqrd


def find_circuit(junction, circuits):
    for c, circuit in enumerate(circuits):
        if junction in circuit:
            return c
    else None


if __name__ == '__main__':
    
    test = "day-8-junction-boxes.txt"
    with open(test, 'r') as f:
        contents = f.read()
    f.close()
    positions = parse_input(contents)

    print(positions)
    positions = list(positions)

    all_pairs = []

    for i in range(len(positions)):
        pos_i = positions[i]
        for j in range(i+1, len(positions)):
            # print(i, j)
            pos_j = positions[j]
            all_pairs.append((pos_i, pos_j))

    sorted_pairs = copy.deepcopy(all_pairs)
    sorted_pairs.sort(key=lambda pair: get_distance_sqrd(pair[0], pair[1]))
    # print(sorted_pairs)


    merge_cap = 10

    # put all junctions into their own circuit
    circuits = [set(p) for p in positions]



    # for n, (i, j) in enumerate(sorted_pairs):

    #     print(n, i, j, get_distance_sqrd(i, j))
    #     # for chain in chains:
        #     if (i in chain) or (j in chain):
        #         chain.add(i)
        #         chain.add(j)




        # if n > merge_cap:
        #     break

        


    # print(sorted(positions))
    # print(np.sort(positions, axis=1))