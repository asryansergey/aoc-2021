from typing import List


def process_input(file_name):
    with open(file_name) as records:
        return [int(num.strip()) for num in records.readline().split(",")]


def count_lanternfish_part_1(ages: List[int], days: int) -> int:
    for day in range(days):
        ages[:] = [age - 1 for age in ages if age != -1]
        for i, _ in enumerate(ages):
            if ages[i] == -1:
                ages[i] = 6
                ages.append(8)
    return len(ages)


if __name__ == "__main__":
    age_records = process_input("./input.in")
    print("[1] Number of fishes: ", count_lanternfish_part_1(age_records, days=80))
