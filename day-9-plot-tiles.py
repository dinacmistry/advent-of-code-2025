"Day 9: Plot movie theatre tiles"
import copy
import numpy as np
import matplotlib.pyplot as plt

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


def make_rectangle(c1, c2):

    col1, row1 = c1
    col2, row2 = c2

    delta_x = row1 + 1 - row2
    if delta_x < 0:
        delta_x *= -1

    delta_y = col1 + 1 - col2
    if delta_y < 0:
        delta_y *= -1
    area = delta_x * delta_y

    return area


def get_all_rectangles(tile_positions):
    areas = []

    for i in range(len(tile_positions)):
        ci = tile_positions[i]
        for j in range(i + 1, len(tile_positions)):
            cj = tile_positions[j]

            area = make_rectangle(ci, cj)
            areas.append([area, ci, cj])

    sorted_areas = copy.deepcopy(areas)
    sorted_areas = sorted(sorted_areas, key= lambda x: x[0], reverse = True)

    return sorted_areas


def plot_tile_boundary(tile_positions, nlines=None, figname='test'):

    fig, ax = plt.subplots()

    if nlines is not None and isinstance(nlines, int) and nlines > 0:
        tile_positions = [t for n, t in enumerate(tile_positions) if n <= nlines]

    # tile_positions.append([tile_positions[0][0], tile_positions[0][1]])
    tile_positions = np.array(tile_positions)

    ax.plot(tile_positions[:, 0], tile_positions[:, 1])

    all_areas = get_all_rectangles(tile_positions)


    colors = ['red', 'green', 'orange', 'purple', 'black',
    'deepskyblue', 'gold', 'salmon', 'aqua', 'lavender',
    'grey', 'pink', 'lime', 'brown']
    print()
    print(len(all_areas))
    n = 0
    # na = int(len(all_areas)/7.5)
    # na = 40200
    # na = 4600
    na = 0
    print("starting at",na)


    for rect in all_areas[na:]:
        area = rect[0]
        corner1 = rect[1]
        corner2 = rect[2]

    # for i in range(len(tile_positions)):
    #     tile_i = tile_positions[i]
    #     # corner1 = [int(tile_i[0]), int(tile_i[1])]
    #     corner1 = tile_i
        a = corner1[0]
        b = corner1[1]
        c = corner2[0]
        d = corner2[1]

        corners = []
        corners.append([a, b])
        corners.append([c, b])
        corners.append([c, d])
        corners.append([a, d])
        corners.append([a, b])
        corners = np.array(corners)
        n += 1

        if n < 100:
            if (47250 <= b <= 50400) or (47250 <= d <= 50400):
                if (b <= 48440 and d <=48440) or (b >= 50321 and d >= 50321):
                    if (b == 48440 or d == 48440 or b == 50321 or d == 50321):
                        print(rect)
            
                        ax.plot(corners[:, 0], corners[:, 1], color = colors[n % len(colors)])

    plt.tight_layout()
    # ax.set_ylim([28000, 72000])
    # ax.set_xlim([5000, 7000])
    # ax.set_xlim(90000, 95000)
    fig.savefig(f'{figname}.png')



if __name__ == '__main__':

    filename = "day-9-test-tiles.txt"
    with open(filename, 'r') as f:
        contents = f.read()
    f.close()

    tile_positions = parse_inputs(contents)

    # figname = 'test-small'
    # nlines = None
    # plot_tile_boundary(tile_positions, nlines, figname)

    # filename = "day-9-tiles.txt"
    # with open(filename, 'r') as f:
    #     contents = f.read()
    # f.close()

    # tile_positions = parse_inputs(contents)
    # # nlines = 100
    # nlines = None
    # plot_tile_boundary(tile_positions, nlines)


    # filename = "day-9-tiles-1.txt"
    # with open(filename, 'r') as f:
    #     contents = f.read()
    # f.close()

    # tile_positions = parse_inputs(contents)
    # nlines = None
    # figname = 'tiles-1'
    # plot_tile_boundary(tile_positions, nlines, figname)


    # filename = "day-9-tiles-2.txt"
    # with open(filename, 'r') as f:
    #     contents = f.read()
    # f.close()

    # tile_positions = parse_inputs(contents)
    # nlines = None
    # figname = 'tiles-2'
    # plot_tile_boundary(tile_positions, nlines, figname)

    filename = "day-9-mapped-tiles.txt"
    with open(filename, 'r') as f:
        contents = f.read()
    f.close()

    tile_positions = parse_inputs(contents)
    nlines = None
    figname = 'mapped-tiles'
    plot_tile_boundary(tile_positions, nlines, figname)


