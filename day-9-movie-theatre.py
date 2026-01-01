"Day 9: Movie Theatre"
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

def get_tile_arrangement(tile_positions):
    arrangement = []
    nrows, ncols = 0, 0

    for t in tile_positions:
        col, row = t
        if row > nrows:
            nrows = row
        if col > ncols:
            ncols = col

    nrows += 1
    ncols += 2

    arrangement = ["".join((["."] * (ncols + 1))) for r in range(nrows + 1)]
    for a in range(len(arrangement)):
        arrangement[a] = list(arrangement[a])

    for t in tile_positions:
        col, row = t
        arrangement[row][col] = "#"

    for r in range(len(arrangement)):
        print("".join(arrangement[r]))

    return arrangement

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

def get_largest_rectangle(tile_positions):
    print(len(tile_positions))
    areas = []

    for i in range(len(tile_positions)):
        ci = tile_positions[i]
        for j in range(i + 1, len(tile_positions)):
            cj = tile_positions[j]

            area = make_rectangle(ci, cj)
            areas.append([area, ci, cj])

    sorted_areas = copy.deepcopy(areas)
    sorted_areas.sort(reverse = True)

    return sorted_areas[0]



def get_boundaries_of_polygon(tile_positions):
    polygon_lines = []

    for i in range(len(tile_positions)):
        # line = []
        j = (i + 1) % len(tile_positions)

        # line_of_tiles = [tile_positions[j][0] - tile_positions[i][0], tile_positions[j][1] - tile_positions[i][1]]

        # if line_of_tiles[0] < 0:
            # line_of_tiles[0] *= -1
        # if line_of_tiles[1] < 0:
            # line_of_tiles[1] *= -1

        delta_y = tile_positions[j][0] - tile_positions[i][0]
        delta_x = tile_positions[j][1] - tile_positions[i][1]

        print("x, y", delta_x, delta_y)

        if delta_x == 0:
            x = tile_positions[i][1]
            if delta_y > 0:
                min_y, max_y = tile_positions[i][0], tile_positions[j][0]
            else:
                min_y, max_y = tile_positions[j][0], tile_positions[i][0]

            print(min_y, max_y)

            for y in range(min_y, max_y + 1):
                # line.append([y, x])
                polygon_lines.append([y, x])


        if delta_y == 0:
            y = tile_positions[i][0]
            if delta_x > 0:
                min_x, max_x = tile_positions[i][1], tile_positions[j][1]
            else:
                min_x, max_x = tile_positions[j][1], tile_positions[i][1]
            for x in range(min_x, max_x + 1):
                # line.append([y, x])
                polygon_lines.append([y, x])

        # polygon_lines.append(line)

    # print("polygon_lines")
    # print(polygon_lines)

    return polygon_lines


def get_polygon_lines_compressed(tile_positions):
    polygon_lines = []
    for i in range(len(tile_positions)):
        j = (i+1) % len(tile_positions)

        yi, xi = tile_positions[i]
        yj, xj = tile_positions[j]
        # polygon_lines.append([xi, xj, yi, yj])
        polygon_lines.append([yi, xi, yj, xj])
        # polygon_lines.append()
    return polygon_lines



def define_rectangle(corner1, corner2):

    y1, x1 = corner1
    y2, x2 = corner2

    corner3 = [y1, x2]
    corner4 = [y2, x1]

    return corner3, corner4


def get_line_at_x(slope, intercept, x):
    return slope * x + intercept


# def get_point(slope, intercept, x):
    # y = get_line_at_x(slope, intercept, x)
def get_point(point):
    y, x = point
    if np.abs(y - int(y)) == 0:
        y = int(y)
    if np.abs(x - int(x)) == 0:
        x = int(x)
    point = [y, x]
    return point

def check_if_lines_cross(line1, line2):
    # x1, x2, slope1, intercept1 = line1
    # x3, x4, slope2, intercept2 = line2
    # x1, x2, y1, y2 = line1
    # x3, x4, y3, y4 = line2
    # x1, y1, x2, y2 = line1
    # y1, x1, y2, x2 = line1
    # y3, x3, y4, x4 = line2
    y2, x2, y1, x1 = line1
    y4, x4, y3, x3 = line2
    print("line1", line1)
    print("line2", line2)

    x_range_min = min(x3, x4)
    x_range_max = max(x3, x4)
    if x1 == x2:
        x_range_min = x1
        x_range_max = x2
    # y1 = get_line_at_x(slope1, intercept1, x1)
    # y2 = get_line_at_x(slope1, intercept1, x2)
    # y3 = get_line_at_x(slope2, intercept2, x3)
    # y4 = get_line_at_x(slope2, intercept2, x4)

    denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)

    if abs(denom) < 1e-9:
        return None

    # intersection
    px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / denom
    py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / denom

    if px >= x_range_min and px <= x_range_max:
        return py, px
    else:
        return None

def get_largest_coloured_rectangle(tile_positions, polygon_lines):

    areas = []

    compressed_polygen_lines = get_polygon_lines_compressed(tile_positions)
    print(tile_positions)

    # max range of x
    x_range_min = min([tile_positions[i][1] for i in range(len(tile_positions))])
    x_range_max = max([tile_positions[i][1] for i in range(len(tile_positions))])

    x_range = np.arange(x_range_min, x_range_max + 1)

    for i in range(len(tile_positions)):
        corner1 = tile_positions[i]
        if i > 0:
            break
        for j in range(i+1, len(tile_positions)):

            if j > 1:
                break
            corner2 = tile_positions[j]

            area = make_rectangle(corner1, corner2)

            corner3, corner4 = define_rectangle(corner1, corner2)
            print()
            print(corner1, corner2, corner3, corner4, "area", area)

            y3, x3 = corner3
            y4, x4 = corner4

            # check if corner3 is in polygon lines or is a polygon corner
            iscorner3_polygon_corner = False
            iscorner3_in_polygon_lines = False
            iscorner4_polygon_corner = False
            iscorner4_in_polygon_lines = False
            iscorner3_inside_polygon = False
            iscorner4_inside_polygon = False

            if corner3 in tile_positions:
                iscorner3_polygon_corner, iscorner3_inside_polygon = True, True

            if corner4 in tile_positions:
                iscorner4_polygon_corner, iscorner4_inside_polygon = True, True

            if corner3 in polygon_lines:
                iscorner3_in_polygon_lines, iscorner3_inside_polygon = True, True
            if iscorner4_in_polygon_lines:
                iscorner4_in_polygon_lines, iscorner4_inside_polygon = True, True

            if x3 != x4:
                slope = (y4-y3)/(x4-x3)
                intercept = y3 - slope * x3

            else:
                areas.append([area, corner1, corner2])

            # corner 3 to corner 4 is moving in the right direction along x
            # if x4 > x3:
            #     interval = 1
            # else:
            #     interval = -1
            crossing3_from_left, crossing3_from_right, crossing3_from_corner = [], [], []
            crossing4_from_left, crossing4_from_right, crossing4_from_corner = [], [], []
            print("corner3", corner3, y3, x3)
            print("corner4", corner4, y4, x4)

            if not iscorner3_in_polygon_lines:
                raytracing_intersections = []
                # draw a line from corner 3 to corner 4 and check if polygon boundary is crossed
                # line1 = x3, x4, y3, y4
                line1 = y3, x3, y4, x4
                # line1 = corner3[0], corner4
                # line 2 has to be every other line in the polygon 
                for line2 in compressed_polygen_lines:
                    # point = check_if_lines_cross(line1, line2, x_range_min, x_range_max)
                    point = check_if_lines_cross(line1, line2)
                    # print(area, corner3, corner4,point)
                    if point is not None:
                        point = get_point(point)
                        print("3 crossing line 2", line2, point, "line 1", line1)
                        areas.append([area, corner1, corner2])
                        py, px = point
                        if px < x3:
                            crossing3_from_left.append(point)
                        elif px > x3:
                            crossing3_from_right.append(point)
                        elif px == x3:
                            crossing3_from_corner.append(point)
                # if x3 != x4:
                #     if interval:
                #         line1 = x3, x4, y3, y4
                #         # line 2 has to be every other line in the polygon 
                #         for line2 in compressed_polygen_lines:
                #             point = check_if_lines_cross(line1, line2, x_range_min, x_range_max)
                #             print(point)

                    # print("range", [x for x in range(x3, x4 + 1 , interval)])
                    # for x in range(x3, x4 + 1, interval):
                    #     point = get_line_at_x(slope, intercept, x)
                    #     point = get_point(point)
                    #     if point in polygon_lines:
                    #         raytracing_intersections.append(point)
                    # # now lets go in the opposite direction and check
                    # # if the direction to x4 was increasing in x, go to the left and check up to x range min
                    # if interval > 0:
                    #     print("range left from 3", [x for x in range(x3, x_range_min-1, -1)], x_range_min)
                    #     for x in range(x3, x_range_min+0, -1):
                    #         point = get_line_at_x(slope, intercept, x)
                    #         point = get_point(point)
                    #         if point in polygon_lines:
                    #             raytracing_intersections.append(point)
                    # # if the direction to x4 was decreasing in x, go to the right and check up to x range max
                    # else:
                    #     print("range right from 3", [x for x in range(x3, x_range_max + 1, 1)])
                    #     for x in range(x3, x_range_max+1, 1):
                    #         point = get_line_at_x(slope, intercept, x)
                    #         point = get_point(point)
                    #         if x == 7:
                    #             print("here", point)
                    #         if point in polygon_lines:
                    #             raytracing_intersections.append(point)
                    # print(f"checking c3: crosses polygon boundary: {len(raytracing_intersections)} times")
                    # if len(raytracing_intersections) < 2:
                    #     pass
                    # else:
                    #     iscorner3_inside_polygon = True
                    # print(raytracing_intersections)
            print("corner3", crossing3_from_left, crossing3_from_right, crossing3_from_corner)

            if not iscorner4_in_polygon_lines:
                raytracing_intersections = []
                line1 = x3, x4, y3, y4
                # line 2 has to be every other line in the polygon 
                for line2 in compressed_polygen_lines:
                    # point = check_if_lines_cross(line1, line2, x_range_min, x_range_max)
                    point = check_if_lines_cross(line1, line2)

                    # print(area, corner3, corner4, point)
                    if point is not None:
                        point = get_point(point)
                        print("4 crossing line 2", line2, point, "line 1", line1)
                        areas.append([area, corner1, corner2])
                        py, px = point
                        if px < x4:
                            crossing4_from_left.append(point)
                        elif px > x4:
                            crossing4_from_right.append(point)
                        elif px == x4:
                            crossing4_from_corner.append(point)

            print("corner4", crossing4_from_left, crossing4_from_right, crossing4_from_corner)
                # if x3 != x4:
            #         print("range", [x for x in range(x4, x3 + 1 , interval)])
            #         for x in (x4, x3 + 1, -interval): # go left if x4 > x3, go right if x4 < x3
            #             point = get_line_at_x(slope, intercept, x)
            #             point = get_point(point)
            #             if point in polygon_lines:
            #                 raytracing_intersections.append(point)
            #         # now lets go in the opposite direction and check
            #         if interval > 0:
            #             print("range right from 4", [x for x in range(x4, x_range_max + 1, 1)])
            #             for x in range(x4, x_range_max + 1, 1): # go right
            #                 point = get_line_at_x(slope, intercept, x)
            #                 point = get_point(point)
            #                 if point in polygon_lines:
            #                     raytracing_intersections.append(point)
            #         else:
            #             print("range left from 4", [x for x in range(x4, x_range_min + 1, -1)])
            #             for x in range(x4, x_range_min + 1, 1): # go left
            #                 point = get_line_at_x(slope, intercept, x)
            #                 point = get_point(point)
            #                 if point in polygon_lines:
            #                     raytracing_intersections.append(point)
            #         print(f"checking c4: crosses polygon boundary: {len(raytracing_intersections)} times")
            #         if len(raytracing_intersections) < 2:
            #             pass
            #         else:
            #             iscorner4_inside_polygon = True
            #         print(raytracing_intersections)

            # if iscorner3_inside_polygon and iscorner4_inside_polygon:
            #     print("all 4 corners inside or on polygon boundary")
            #     print(corner1, corner2, corner3, corner4, 4)
            #     areas.append([area, corner1, corner2])

            # else:
            #     if not iscorner3_inside_polygon:
            #         print("corner3", corner3, "not inside polygon")
            #     if not iscorner4_inside_polygon:
            #         print("corner4", corner4, "not inside polygon")


    print("inside areas")
    # for a in areas:
        # print(a)

    print(x_range_min, x_range_max)


    print("you need a different way to check if two lines cross that's not using discretized forms of the lines")
    print("you need to define each line as a function and then check against that but almost there!")



























    return None




# def get_largest_colored_rectangle(tile_positions):


    # n_tiles_to_add = 0
    # tiles_to_add = []

    # for i in range(len(tile_positions)):

    #     j = (i + 1) % len(tile_positions)
    #     # print(i, j)
    #     print(i, tile_positions[i], tile_positions[j], 
    #         [tile_positions[i][0] - tile_positions[j][0], tile_positions[i][1] - tile_positions[j][1] ])

    #     line_of_tiles = [tile_positions[i][0] - tile_positions[j][0], tile_positions[i][1] - tile_positions[j][1]]
    #     if line_of_tiles[0] < 0:
    #         line_of_tiles[0] *= -1
    #     if line_of_tiles[1] < 0:
    #         line_of_tiles[1] *= -1

    #     n_tiles_to_add += max( line_of_tiles )

    #     delta_x = tile_positions[j][0] - tile_positions[i][0]
    #     delta_y = tile_positions[j][1] - tile_positions[i][1]

    #     if delta_x == 0:
    #         x = tile_positions[i][0]
    #         if delta_y > 0:
    #             min_y, max_y = tile_positions[i][1], tile_positions[j][1]
    #         else:
    #             min_y, max_y = tile_positions[j][1], tile_positions[i][1]
    #         for y in range(min_y, max_y + 1):
    #             tiles_to_add.append([x , y])

    #     if delta_y == 0:
    #         y = tile_positions[i][0]
    #         if delta_x:
    #             min_x, max_x = tile_positions[i][0], tile_positions[j][0]
    #         else:
    #             min_x, max_x = tile_positions[j][0], tile_positions[i][0]
    #         for x in range(min_x, max_x + 1):
    #             tiles_to_add.append([x, y])






        # if i > 50:
            # break
    # print(n_tiles_to_add)
    # print(len(tiles_to_add))

if __name__ == '__main__':
    
    filename = "day-9-test-tiles.txt"
    with open(filename, 'r') as f:
        contents = f.read()
    f.close()

    tile_positions = parse_inputs(contents)

    largest_rectangle = get_largest_rectangle(tile_positions)
    print("Area of largest rectangle is", largest_rectangle[0])

    expected = 50
    assert largest_rectangle[0] == expected, "wrong area"



    polygon_lines = get_boundaries_of_polygon(tile_positions)

    get_largest_coloured_rectangle(tile_positions, polygon_lines)

    # filename = "day-9-tiles.txt"
    # with open(filename, 'r') as f:
    #     contents = f.read()
    # f.close()

    # tile_positions = parse_inputs(contents)

    # largest_rectangle = get_largest_rectangle(tile_positions)
    # print("Area of largest rectangle is", largest_rectangle[0])


    # get_largest_coloured_rectangle(tile_positions, polygon_lines)


