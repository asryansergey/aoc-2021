from typing import List
from collections import Counter


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
            if x1 == x2 or y1 == y2:
                vent_points.append(((x1, y1), (x2, y2)))
    print(max_elem)
    return vent_points, max_elem


def count_overlapping_points_1(points, range_value) -> int:
    grid = [[0 for x in range(range_value)] for y in range(range_value)]
    for pair in points:
        point1, point2 = pair[:]
        if point1[0] == point2[0]:
            range_points = sorted([point1[1], point2[1]])
            for i in range(range_points[0], range_points[1] + 1):
                grid[point1[0]][i] += 1
            continue
        if point1[1] == point2[1]:
            range_points = sorted([point1[0], point2[0]])
            for i in range(range_points[0], range_points[1] + 1):
                grid[i][point1[1]] += 1
    overlap_count = 0
    for row in grid:
        for elem in row:
            if elem > 1:
                overlap_count += 1
    return overlap_count


if __name__ == "__main__":
    vent_points, max_elem = process_input("input.in")
    print("[1] Number of overlapping points: ", count_overlapping_points_1(vent_points, max_elem + 1))
