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


def get_largest_rectangle(tile_positions):
    sorted_areas = get_all_rectangles(tile_positions)
    return sorted_areas[0]


def get_boundaries_of_polygon(tile_positions):
    polygon_lines = []

    for i in range(len(tile_positions)):
        j = (i + 1) % len(tile_positions)

        delta_y = tile_positions[j][0] - tile_positions[i][0]
        delta_x = tile_positions[j][1] - tile_positions[i][1]

        if delta_x == 0:
            x = tile_positions[i][1]
            if delta_y > 0:
                min_y, max_y = tile_positions[i][0], tile_positions[j][0]
            else:
                min_y, max_y = tile_positions[j][0], tile_positions[i][0]

            for y in range(min_y, max_y + 1):
                polygon_lines.append([y, x])

        if delta_y == 0:
            y = tile_positions[i][0]
            if delta_x > 0:
                min_x, max_x = tile_positions[i][1], tile_positions[j][1]
            else:
                min_x, max_x = tile_positions[j][1], tile_positions[i][1]
            for x in range(min_x, max_x + 1):
                polygon_lines.append([y, x])

    return polygon_lines


def get_polygon_lines_compressed(tile_positions):
    polygon_lines = []
    for i in range(len(tile_positions)):
        j = (i+1) % len(tile_positions)
        yi, xi = tile_positions[i]
        yj, xj = tile_positions[j]
        polygon_lines.append([yi, xi, yj, xj])
    return polygon_lines


def define_rectangle(corner1, corner2):

    y1, x1 = corner1
    y2, x2 = corner2

    corner3 = [y1, x2]
    corner4 = [y2, x1]

    return corner3, corner4


def get_line_at_x(slope, intercept, x):
    return slope * x + intercept


def get_point(point):
    y, x = point
    if np.abs(y - int(y)) == 0:
        y = int(y)
    if np.abs(x - int(x)) == 0:
        x = int(x)
    point = [y, x]
    return point


def check_if_lines_cross(line1, line2):
    y2, x2, y1, x1 = line1
    y4, x4, y3, x3 = line2

    x_range_min = min(x3, x4)
    x_range_max = max(x3, x4)
    y_range_min = min(y3, y4)
    y_range_max = max(y3, y4)
    if x3 == x4:
        x_range_min = x3
        x_range_max = x4
    if y3 == y4:
        y_range_min = y3
        y_range_max = y4

    denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)

    if abs(denom) < 1e-9:
        return None

    # intersection
    px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / denom
    py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / denom

    if (px >= x_range_min) and (px <= x_range_max) and (py >= y_range_min) and (py <= y_range_max):
        return py, px
    else:
        return None


def check_if_lines_cross_new(line1, line2):
    # line 2 is finite
    y2, x2, y1, x1 = line1
    y4, x4, y3, x3 = line2

    x_range_min = min(x3, x4)
    x_range_max = max(x3, x4)
    y_range_min = min(y3, y4)
    y_range_max = max(y3, y4)

    # line 1 will likely not be horizontal or vertical
    if x3 == x4: # line 2 is vertical
        if x1 != x2:
            slope = (y2 - y1)/(x2 - x1)
            intercept = y2 - (y2 - y1)/(x2 - x1) * x2
            # where line1 crosses line2 at x3
            y = get_line_at_x(slope, intercept, x3) # where line 1 maybe crosses line 2 at x3 = x4 
            if (y_range_min <= y <= y_range_max):
                return y, x3

    elif y3 == y4: # line 2 is horizontal
        if x1 != x2 and y2 != y1:
            slope = (y2 - y1)/(x2 - x1)
            intercept = y2 - (y2 - y1)/(x2 - x1) * x2
            x = (y3 - intercept) / slope # where line 1 maybe crosses line 2 at y3 = y4
            if (x_range_min <= x <= x_range_max):
                return y3, x

    return None

def ray_casting_point_in_polygon(point, polygon_vertices):
    y, x = point
    count = 0
    n = len(polygon_vertices)

    for i in range(n):

        p1y, p1x = polygon_vertices[i]
        p2y, p2x = polygon_vertices[(i + 1) % n]

        if p2y != p1y and p2x != p1x:
            if ( (p1x <= x <= p2x) or (p2x <= x <= p1x)) and (y <= (p2y - p1y) * (x - p1x) / (p2x - p1x) + p1y):
        # if p2y != p1y:
            # if ((p1y <= y <= p2y) or (p2y <= y <= p1y)) and (x <= (p2x - p1x) * (y - p1y) / (p2y - p1y) + p1x):
                count += 1

    return count % 2 == 1


def find_largest_rectangle_from_crossing(tile_positions, polygon_lines):
    all_areas = get_all_rectangles(tile_positions)
    compressed_polygen_lines = get_polygon_lines_compressed(tile_positions)
    # areas = all_areas[int(len(all_areas)/):]

    areas_inside = []

    for a in all_areas:
        area = a[0]
        corner1 = a[1]
        corner2 = a[2]

        b = corner1[1]
        d = corner2[1]

        if not (b == 48440 or d == 48440 or b == 50321 or d == 50321):
            continue
            # print(b, d)
        # print(a)

        if len(areas_inside) > 5:
            break

        corner3, corner4 = define_rectangle(corner1, corner2)

        if corner1 == corner3 and corner2 == corner4:
            areas_inside.append(a)

        iscorner3_polygon_corner = False
        iscorner3_in_polygon_lines = False
        iscorner3_inside_polygon_from_x = False
        iscorner3_inside_polygon_from_y = False
        iscorner3_inside_polygon = False

        iscorner4_polygon_corner = False
        iscorner4_in_polygon_lines = False
        iscorner4_inside_polygon_from_x = False
        iscorner4_inside_polygon_from_y = False
        iscorner4_inside_polygon = False

        if corner3 in tile_positions:
            iscorner3_polygon_corner, iscorner3_inside_polygon = True, True
        if corner4 in tile_positions:
            iscorner4_polygon_corner, iscorner4_inside_polygon = True, True
        if corner3 in polygon_lines:
            iscorner3_in_polygon_lines, iscorner3_inside_polygon = True, True
        if corner4 in polygon_lines:
            iscorner4_in_polygon_lines, iscorner4_inside_polygon = True, True

        crossing3_from_left, crossing3_from_right, crossing3_from_cornerx = [], [], []
        crossing3_from_bottom, crossing3_from_top, crossing3_from_cornery = [], [], []
        crossing4_from_left, crossing4_from_right, crossing4_from_cornerx = [], [], []
        crossing4_from_bottom, crossing4_from_top, crossing4_from_cornery = [], [], []

        y3, x3 = corner3
        y4, x4 = corner4

        # print("area", a, corner3, corner4, corner3 in polygon_lines, corner4 in polygon_lines)

        if not iscorner3_in_polygon_lines:
            line1 = corner4[0], corner4[1], corner3[0], corner3[1]
            for line2 in compressed_polygen_lines:
                point = check_if_lines_cross_new(line1, line2)
                if point is not None:
                    point = get_point(point)
                    # print(area, line1, line2, corner3, corner4, point)
                    if point in polygon_lines:
                        print("short cut!", a, corner3, corner4)
                        iscorner3_inside_polygon = True

                    py, px = point
                    if px < x3:
                        crossing3_from_left.append(point)
                    elif px > x3:
                        crossing3_from_right.append(point)
                    elif px == x3:
                        print("hi x3")
                        crossing3_from_cornerx.append(point)
                    if py < y3:
                        crossing3_from_bottom.append(point)
                    elif py > y3:
                        crossing3_from_top.append(point)
                    elif py == y3:
                        print("hi y3")
                        crossing3_from_cornery.append(point)

            if (len(crossing3_from_left) > 0) and (len(crossing3_from_right) > 0):
                if (len(crossing3_from_left) == 1) and (len(crossing3_from_right) == 1):
                    iscorner3_inside_polygon_from_x = True
            elif (len(crossing3_from_left) > 0) and (len(crossing3_from_cornerx) > 0):
                if (len(crossing3_from_left) == 1) and (len(crossing3_from_right) == 1): 
                    iscorner3_inside_polygon_from_x = True
            elif (len(crossing3_from_right) > 0) and (len(crossing3_from_cornerx) > 0):
                if (len(crossing3_from_right) == 1) and (len(crossing3_from_cornerx) == 1):
                    iscorner3_inside_polygon_from_x = True

            if (len(crossing3_from_bottom) > 0) and (len(crossing3_from_top) > 0):
                if (len(crossing3_from_bottom) == 1) and (len(crossing3_from_top) == 1):
                    iscorner3_inside_polygon_from_y = True
            elif (len(crossing3_from_bottom) > 0) and (len(crossing3_from_cornery) > 0):
                if (len(crossing3_from_bottom) == 1) and (len(crossing3_from_cornery) == 1):
                    iscorner3_inside_polygon_from_y = True  
            elif (len(crossing3_from_top) > 0) and (len(crossing3_from_cornery) > 0):
                if (len(crossing3_from_top) == 1) and (len(crossing3_from_cornery) == 1):
                    iscorner3_inside_polygon_from_y = True

        if not iscorner4_in_polygon_lines:
            line1 = corner3[0], corner3[1], corner4[0], corner4[1]
            for line2 in compressed_polygen_lines:
                point = check_if_lines_cross_new(line1, line2)
                if point is not None:
                    point = get_point(point)
                    # print(area, line1, line2, corner3, corner4, point)
                    if point in polygon_lines:
                        print("short cut 4!", a, corner3, corner4)
                        iscorner4_inside_polygon = True

                    py, px = point
                    if px < x4:
                        crossing4_from_left.append(point)
                    elif px > x4:
                        crossing4_from_right.append(point)
                    elif px == x4:
                        print("hi?")
                        crossing4_from_cornerx.append(point)
                    if py < y4:
                        crossing4_from_bottom.append(point)
                    elif py > y4:
                        crossing4_from_top.append(point)
                    elif py == y4:
                        print("hi y4")
                        crossing4_from_cornery.append(point)

            if (len(crossing4_from_left) > 0) and (len(crossing4_from_right) > 0):
                iscorner4_inside_polygon_from_x = True
            elif (len(crossing4_from_left) > 0) and (len(crossing4_from_cornerx) > 0):
                iscorner4_inside_polygon_from_x = True
            elif (len(crossing4_from_right) > 0) and (len(crossing4_from_cornerx) > 0):
                iscorner4_inside_polygon_from_x = True
            if (len(crossing4_from_bottom) > 0) and (len(crossing4_from_top) > 0):
                iscorner4_inside_polygon_from_y = True
            elif (len(crossing4_from_bottom) > 0) and (len(crossing4_from_cornery) > 0):
                iscorner4_inside_polygon_from_y = True
            elif (len(crossing4_from_top) > 0) and (len(crossing4_from_cornery) > 0):
                iscorner4_inside_polygon_from_y = True
        # print(len(crossing3_from_left), len(crossing3_from_right), len(crossing3_from_cornerx), len(crossing3_from_bottom), len(crossing3_from_top), len(crossing3_from_cornery))
        # print(len(crossing4_from_left), len(crossing4_from_right), len(crossing4_from_cornerx), len(crossing4_from_bottom), len(crossing4_from_top), len(crossing4_from_cornery))

        if iscorner3_inside_polygon_from_x and iscorner3_inside_polygon_from_y:
            iscorner3_inside_polygon = True

        if iscorner4_inside_polygon_from_x and iscorner4_inside_polygon_from_y:
            iscorner4_inside_polygon = True

        if iscorner3_inside_polygon and iscorner4_inside_polygon:
            areas_inside.append(a)

    for a in areas_inside:
        print("inside", a)

    return areas_inside


def find_largest_rectangle_from_ray_casting(tile_positions, polygon_lines):
    areas = get_all_rectangles(tile_positions)
    print(areas)
    compressed_polygen_lines = get_polygon_lines_compressed(tile_positions)

    largest_rectangle = None

    for a in areas:
        area = a[0]
        corner1 = a[1]
        corner2 = a[2]
        print(a)

        corner3, corner4 = define_rectangle(corner1, corner2)

        iscorner1_inside = ray_casting_point_in_polygon(corner1, tile_positions)
        iscorner2_inside = ray_casting_point_in_polygon(corner2, tile_positions)
        iscorner3_inside = ray_casting_point_in_polygon(corner3, tile_positions)
        iscorner4_inside = ray_casting_point_in_polygon(corner4, tile_positions)

        print(iscorner1_inside, iscorner2_inside, iscorner3_inside, iscorner4_inside)
        if iscorner1_inside and iscorner2_inside and iscorner3_inside and iscorner4_inside:
            largest_rectangle = area, corner1, corner2
            break

    print("largest", largest_rectangle)

    return largest_rectangle


def find_largest_rectangle_inside(tile_positions, polygon_lines):
    areas = get_all_rectangles(tile_positions)
    compressed_polygen_lines = get_polygon_lines_compressed(tile_positions)
    for t in tile_positions:
        print(t)

    largest_rectangle = None

    for a in areas:
        print(a)
        area = a[0]
        corner1 = a[1]
        corner2 = a[2]
        if area >= 4569730880:
            continue

        corner3, corner4 = define_rectangle(corner1, corner2)

        iscorner3_polygon_corner = False
        iscorner3_in_polygon_lines = False
        iscorner3_inside_polygon_from_x = False
        iscorner3_inside_polygon_from_y = False
        iscorner3_inside_polygon = False

        iscorner4_polygon_corner = False
        iscorner4_in_polygon_lines = False
        iscorner4_inside_polygon_from_x = False
        iscorner4_inside_polygon_from_y = False
        iscorner4_inside_polygon = False

        # if corner3 in tile_positions:
        #     iscorner3_polygon_corner = True
        # if corner4 in tile_positions:
        #     iscorner4_polygon_corner= True
        if corner3 in polygon_lines:
            iscorner3_in_polygon_lines = True
        if corner4 in polygon_lines:
            iscorner4_in_polygon_lines = True

        crossing3_from_left, crossing3_from_right, crossing3_from_cornerx = [], [], []
        crossing3_from_bottom, crossing3_from_top, crossing3_from_cornery = [], [], []
        crossing4_from_left, crossing4_from_right, crossing4_from_cornerx = [], [], []
        crossing4_from_bottom, crossing4_from_top, crossing4_from_cornery = [], [], []

        y3, x3 = corner3
        y4, x4 = corner4

        if not iscorner3_in_polygon_lines:
            line1 = corner4[0], corner4[1], corner3[0], corner3[1]
            for line2 in compressed_polygen_lines:
                point = check_if_lines_cross(line1, line2)
                if point is not None:
                    # point = get_point(point)
                    py, px = point
                    if px < x3:
                        crossing3_from_left.append(point)
                    elif px > x3:
                        crossing3_from_right.append(point)
                    elif px == x3:
                        crossing3_from_cornerx.append(point)
                    if py < y3:
                        crossing3_from_bottom.append(point)
                    elif py > y3:
                        crossing3_from_top.append(point)
                    elif py == y3:
                        crossing3_from_cornery.append(point)

            if (len(crossing3_from_left) > 0) and (len(crossing3_from_right) > 0):
                if (len(crossing3_from_left) == 1) and (len(crossing3_from_right) == 1):
                    iscorner3_inside_polygon_from_x = True
            # elif (len(crossing3_from_left) > 0) and (len(crossing3_from_cornerx) > 0):
            #     iscorner3_inside_polygon_from_x = True
            # elif (len(crossing3_from_right) > 0) and (len(crossing3_from_cornerx) > 0):
            #     iscorner3_inside_polygon_from_x = True

            if (len(crossing3_from_bottom) > 0) and (len(crossing3_from_top) > 0):
                if (len(crossing3_from_bottom) == 1) and (len(crossing3_from_top) == 1):
                    iscorner3_inside_polygon_from_y = True
            # elif (len(crossing3_from_bottom) > 0) and (len(crossing3_from_cornery) > 0):
            #     iscorner3_inside_polygon_from_y = True
            # elif (len(crossing3_from_top) > 0) and (len(crossing3_from_cornery) > 0):
            #     iscorner3_inside_polygon_from_y = True

        if not iscorner4_in_polygon_lines:
            line1 = corner3[0], corner3[1], corner4[0], corner4[1]
            for line2 in compressed_polygen_lines:
                point = check_if_lines_cross(line1, line2)
                if point is not None:
                    # point = get_point(point)
                    py, px = point
                    if px < x4:
                        crossing4_from_left.append(point)
                    elif px > x4:
                        crossing4_from_right.append(point)
                    elif px == x4:
                        crossing4_from_cornerx.append(point)
                    if py < y4:
                        crossing4_from_bottom.append(point)
                    elif py > y4:
                        crossing4_from_top.append(point)
                    elif py == y4:
                        crossing4_from_cornery.append(point)

            if (len(crossing4_from_left) > 0) and (len(crossing4_from_right) > 0):
                if (len(crossing4_from_left) % 2 == 1) and (len(crossing4_from_top) % 2 == 1):
                    iscorner4_inside_polygon_from_x = True
            # elif (len(crossing4_from_left) > 0) and (len(crossing4_from_cornerx) > 0):
            #     iscorner4_inside_polygon_from_x = True
            # elif (len(crossing4_from_right) > 0) and (len(crossing4_from_cornerx) > 0):
            #     iscorner4_inside_polygon_from_x = True

            if (len(crossing4_from_bottom) > 0) and (len(crossing4_from_top) > 0):
                if (len(crossing4_from_bottom) % 2 == 1) and (len(crossing4_from_top) % 2 == 1):
                    iscorner4_inside_polygon_from_y = True
            # elif (len(crossing4_from_bottom) > 0) and (len(crossing4_from_cornery) > 0):
            #     iscorner4_inside_polygon_from_y = True
            # elif (len(crossing4_from_top) > 0) and (len(crossing4_from_cornery) > 0):
            #     iscorner4_inside_polygon_from_y = True
                

        if iscorner3_inside_polygon_from_x and iscorner3_inside_polygon_from_y:
            iscorner3_inside_polygon = True

        if iscorner4_inside_polygon_from_x and iscorner4_inside_polygon_from_y:
            iscorner4_inside_polygon = True

        if iscorner3_inside_polygon and iscorner4_inside_polygon:
            largest_rectangle = [area, corner1, corner2]
            print(crossing3_from_left, crossing3_from_right, crossing3_from_cornerx)
            print(crossing3_from_bottom, crossing3_from_top, crossing3_from_cornery)
            print(crossing4_from_left, crossing4_from_right, crossing4_from_cornerx)
            print(crossing4_from_bottom, crossing4_from_top, crossing4_from_cornery)
            break

    print("hi")
    print(largest_rectangle)
    return largest_rectangle


def get_rectangles_inside(tile_positions, polygon_lines):

    areas = []
    compressed_polygen_lines = get_polygon_lines_compressed(tile_positions)

    for i in range(len(tile_positions)):
        corner1 = tile_positions[i]

        for j in range(i + 1, len(tile_positions)):
            corner2 = tile_positions[j]

            area = make_rectangle(corner1, corner2)
            corner3, corner4 = define_rectangle(corner1, corner2)

            iscorner3_polygon_corner = False
            iscorner3_in_polygon_lines = False
            iscorner3_inside_polygon = False
            iscorner4_polygon_corner = False
            iscorner4_in_polygon_lines = False
            iscorner4_inside_polygon = False

            if corner3 in tile_positions:
                iscorner3_polygon_corner, iscorner3_inside_polygon = True, True
            if corner4 in tile_positions:
                iscorner4_polygon_corner, iscorner4_inside_polygon = True, True
            if corner3 in polygon_lines:
                iscorner3_in_polygon_lines, iscorner3_inside_polygon = True, True
            if corner4 in polygon_lines:
                iscorner4_in_polygon_lines, iscorner4_inside_polygon = True, True

            crossing3_from_left, crossing3_from_right, crossing3_from_corner = [], [], []
            crossing4_from_left, crossing4_from_right, crossing4_from_corner = [], [], []

            y3, x3 = corner3
            y4, x4 = corner4

            if not iscorner3_in_polygon_lines:
                line1 = corner4[0], corner4[1], corner3[0], corner3[1]
                for line2 in compressed_polygen_lines:
                    point = check_if_lines_cross(line1, line2)
                    if point is not None:
                        point = get_point(point)
                        py, px = point
                        if px < x3:
                            crossing3_from_left.append(point)
                        elif px > x3:
                            crossing3_from_right.append(point)
                        elif px == x3:
                            crossing3_from_corner.append(point)
                if (len(crossing3_from_left) > 0) and (len(crossing3_from_right) > 0):
                    iscorner3_inside_polygon = True
                elif (len(crossing3_from_left) > 0) and (len(crossing3_from_corner) > 0):
                    iscorner3_inside_polygon = True
                elif (len(crossing3_from_right) > 0) and (len(crossing3_from_corner) > 0):
                    iscorner3_inside_polygon = True

            if not iscorner4_in_polygon_lines:
                line1 = corner4[0], corner4[1], corner3[0], corner3[1]
                for line2 in compressed_polygen_lines:
                    point = check_if_lines_cross(line1, line2)
                    if point is not None:
                        point = get_point(point)
                        py, px = point
                        if px < x4:
                            crossing4_from_left.append(point)
                        elif px > x4:
                            crossing4_from_right.append(point)
                        elif px == x4:
                            crossing4_from_corner.append(point)
                if (len(crossing4_from_left) > 0) and (len(crossing4_from_right) > 0):
                    iscorner4_inside_polygon = True
                elif (len(crossing4_from_left) > 0) and (len(crossing4_from_corner) > 0):
                    iscorner4_inside_polygon = True
                elif (len(crossing4_from_right) > 0) and (len(crossing3_from_corner) > 0):
                    iscorner4_inside_polygon = True

            # if both new corners are inside the polygon then the entire rectangle is too!
            if iscorner3_inside_polygon and iscorner4_inside_polygon:
                areas.append([area, corner1, corner2])
                # print(i, j, areas[-1])

    return areas


def get_largest_rectangle_inside(areas):
    sorted_areas = copy.deepcopy(areas)
    sorted_areas.sort(reverse = True)

    return sorted_areas[0][0]


if __name__ == '__main__':
    
    filename = "day-9-test-tiles.txt"
    with open(filename, 'r') as f:
        contents = f.read()
    f.close()

    tile_positions = parse_inputs(contents)

    largest_rectangle = get_largest_rectangle(tile_positions)
    print("Area of largest rectangle is", largest_rectangle[0])

    expected = 50
    area_of_largest_rectangle = largest_rectangle[0]
    assert area_of_largest_rectangle == expected, "wrong area"


    # part two
    polygon_lines = get_boundaries_of_polygon(tile_positions)
    rectangles_inside = get_rectangles_inside(tile_positions, polygon_lines)

    area_of_largest_rectangle = get_largest_rectangle_inside(rectangles_inside)
    print(area_of_largest_rectangle)
    expected = 24
    assert area_of_largest_rectangle == expected, "wrong area within coloured tiles"

    # find_largest_rectangle_inside(tile_positions, polygon_lines)
    # find_largest_rectangle_from_ray_casting(tile_positions, polygon_lines)

    areas_inside = find_largest_rectangle_from_crossing(tile_positions, polygon_lines)
    for a in areas_inside:
        print(a)

    filename = "day-9-tiles.txt"
    with open(filename, 'r') as f:
        contents = f.read()
    f.close()

    # part 1
    tile_positions = parse_inputs(contents)
    polygon_lines = get_boundaries_of_polygon(tile_positions)
    largest_rectangle = get_largest_rectangle(tile_positions)
    print("Area of largest rectangle is", largest_rectangle[0])


    # part 2 - super slow
    # polygon_lines = get_boundaries_of_polygon(tile_positions)
    # rectangles_inside = get_rectangles_inside(tile_positions, polygon_lines)
    # area_of_largest_rectangle = get_largest_rectangle_inside(rectangles_inside)
    # print("Area of largest rectangle", area_of_largest_rectangle)
    # find_largest_rectangle_inside(tile_positions, polygon_lines)
    # find_largest_rectangle_from_ray_casting(tile_positions, polygon_lines)
    # find_largest_rectangle_from_crossing(tile_positions, polygon_lines)


    # filename = "day-9-tiles-1.txt"
    # with open(filename, 'r') as f:
    #     contents = f.read()
    # f.close()

    # # part 1
    # tile_positions = parse_inputs(contents)
    # polygon_lines = get_boundaries_of_polygon(tile_positions)

    # areas_inside = find_largest_rectangle_from_crossing(tile_positions, polygon_lines)

    # top half
    print("\nPart 1")
    filename = "day-9-tiles-1.txt"
    with open(filename, 'r') as f:
        contents = f.read()
    f.close()

    tile_positions = parse_inputs(contents)
    polygon_lines = get_boundaries_of_polygon(tile_positions)
    largest_rectangle = get_largest_rectangle(tile_positions)

    find_largest_rectangle_from_crossing(tile_positions, polygon_lines)



    # bottom half
    print("\nPart 2")
    filename = "day-9-tiles-2.txt"
    with open(filename, 'r') as f:
        contents = f.read()
    f.close()

    tile_positions = parse_inputs(contents)
    polygon_lines = get_boundaries_of_polygon(tile_positions)
    largest_rectangle = get_largest_rectangle(tile_positions)

    find_largest_rectangle_from_crossing(tile_positions, polygon_lines)




