from typing import List
from collections import defaultdict, Counter


def process_input(file_name):
    with open(file_name) as records:
        return [int(num.strip()) for num in records.readline().split(",")]


def count_lanternfish_part_1(population: List[int], days: int) -> int:
    for day in range(days):
        population[:] = [age - 1 for age in population if age != -1]
        for i, _ in enumerate(population):
            if population[i] == -1:
                population[i] = 6
                population.append(8)
    return len(population)


def count_lanternfish_part_2(population: List[int], days: int) -> int:
    population_counter = Counter(population)
    occurrences = [population_counter[idx] for idx in [x for x in range(9)]]
    for day in range(days):
        occurrences.append(occurrences[0])
        occurrences.pop(0)
        occurrences[6] += occurrences[8]
    return sum(occurrences)


if __name__ == "__main__":
    age_records = process_input("./input.in")
    print("[1] Number of lanternfishes: ", count_lanternfish_part_1(age_records, days=80))
    age_records = process_input("./input.in")
    print("[2] Number of lanternfishes: ", count_lanternfish_part_2(age_records, days=256))
