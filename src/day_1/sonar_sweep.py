from typing import List

def process_input(file_name):
    with open(file_name) as records:
        return [int(depth.strip()) for depth in records]

def count_increasing_depts_part1(depth_values: List[int]) -> int:
    zero_depth = depth_values[0]
    count = 0
    for elem in depth_values[1:]:
        if elem > zero_depth:
            count += 1
        zero_depth = elem
    return count

def count_increasing_depts_part2(depth_values: List[int]) -> int:
    zero_depth = sum(depth_values[:3])
    count = 0
    for idx, elem in enumerate(depth_values[1:]):
        trio_sum = sum(depth_values[idx:idx+3])
        if trio_sum > zero_depth:
            count += 1
        zero_depth = trio_sum
    return count


if __name__ == "__main__":
    records = process_input("./input.in")
    print("[1] Increasing depth count: ", count_increasing_depts_part1(records))
    print("[2] Increasing depth count: ", count_increasing_depts_part2(records))
