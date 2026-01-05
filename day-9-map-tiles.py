"Day 9: Movie Theatre - map tiles to a reduced set"
import copy
import numpy as np

def parse_inputs(input_string):
    tile_positions = []
    split_string = input_string.split("\n")

    for i in split_string:
        line = i.split(",")
        if len(line) > 0:
            try:
                line = [int(x) for x in line]
                tile_positions.append(line)
            except:
                pass

    return tile_positions


def map_tiles(tile_positions):
    tile_positions = np.array(tile_positions)

    ytiles = tile_positions[:, 0]
    xtiles = tile_positions[:, 1]

    print(len(ytiles))
    print(len(xtiles))

    ytiles = np.unique(ytiles)
    xtiles = np.unique(xtiles)

    ytiles.sort()
    xtiles.sort()
    # print(ytiles)
    # print(xtiles)
    print(len(ytiles))
    print(len(xtiles))

    ymapping = dict()
    xmapping = dict()

    for n, t in enumerate(ytiles):
        # print(n, t)
        ymapping[t] = n

    for n, t in enumerate(xtiles):
        xmapping[t] = n

    # for k, v in ymapping.items():
        # print(k,v)

    new_tiles = []

    for n, t in enumerate(tile_positions):
        y, x = t

        new_y = ymapping[y]
        new_x = xmapping[x]

        new_tiles.append([new_y, new_x])


    np.savetxt('day-9-mapped-tiles.txt', new_tiles, fmt='%.0f', delimiter=',')



if __name__ == '__main__':

    filename = "day-9-tiles.txt"
    with open(filename, 'r') as f:
        contents = f.read()
    f.close()

    # part 1
    tile_positions = parse_inputs(contents)

    map_tiles(tile_positions)