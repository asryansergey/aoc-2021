from math import atan2, pi


def process_input(file_name):
    vent_points = []
    max_elem = 0
    with open(file_name) as records:
        for point in records:
            current_point = [tuple(num.strip().split(",")) for num in point.split("->")]
            x1, y1 = [int(x) for x in current_point[0]]
            x2, y2 = [int(x) for x in current_point[1]]
            curr_max = max([x1, x2, y1, y2])
            if max_elem < curr_max:
                max_elem = curr_max
            vent_points.append(((x1, y1), (x2, y2)))
    return vent_points, max_elem


def mark_x_axis_points(grid, point1, point2):
    range_points = sorted([point1[1], point2[1]])
    for i in range(range_points[0], range_points[1] + 1):
        grid[point1[0]][i] += 1


def mark_y_axis_points(grid, point1, point2):
    range_points = sorted([point1[0], point2[0]])
    for i in range(range_points[0], range_points[1] + 1):
        grid[i][point1[1]] += 1


def mark_diagonal_points(grid, point1, point2):
    col = point1[1]
    for i in range(point1[0], point2[0] + 1):
        grid[i][col] += 1
        col = col + 1 if point1[1] < point2[1] else col - 1


def is_diagonal_45_degree(point1, point2):
    x = abs(point2[0] - point1[0])
    y = abs(point2[1] - point1[1])
    return atan2(y, x) == pi / 4


def count_overlapping_points_1(points, range_value) -> int:
    grid = [[0 for _ in range(range_value)] for _ in range(range_value)]
    for pair in points:
        point1, point2 = pair[:]
        if point1[0] == point2[0]:
            mark_x_axis_points(grid, point1, point2)
            continue

        if point1[1] == point2[1]:
            mark_y_axis_points(grid, point1, point2)

    return sum([1 for row in grid for x in row if x > 1])


def count_overlapping_points_2(points, range_value) -> int:
    grid = [[0 for _ in range(range_value)] for _ in range(range_value)]
    for pair in points:
        point1, point2 = pair[:]
        if point1[0] == point2[0]:
            mark_x_axis_points(grid, point1, point2)

        elif point1[1] == point2[1]:
            mark_y_axis_points(grid, point1, point2)

        else:
            if point1[0] > point2[0]:
                point1, point2 = point2, point1

            if is_diagonal_45_degree(point1, point2):
                mark_diagonal_points(grid, point1, point2)

    return sum([1 for row in grid for x in row if x > 1])


if __name__ == "__main__":
    vent_points, size = process_input("input.in")
    print("[1] Number of overlapping points: ", count_overlapping_points_1(vent_points, size + 1))
    print("[2] Number of overlapping points: ", count_overlapping_points_2(vent_points, size + 1))
