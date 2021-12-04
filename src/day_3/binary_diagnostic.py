from typing import List


def process_input(file_name):
    with open(file_name) as records:
        return [depth.strip() for depth in records]


def calc_power_consumption_part_1(power_data: List[int]) -> int:
    gamma_rates, epsilion_rates = "", ""
    line_len = len(power_data[0])
    zero_count = 0
    for idx in range(line_len):
        zero_count = len([x for x in power_data if x[idx] == "0"])
        if len(power_data) - zero_count > zero_count:
            gamma_rates += "1"
            epsilion_rates += "0"
        else:
            epsilion_rates += "1"
            gamma_rates += "0"
    return int(gamma_rates, 2) * int(epsilion_rates, 2)


def calc_target_rating(power_data: List[int], start_idx: int, target: int) -> int:
    if len(power_data) == 1:
        return int(power_data[0], 2)

    line_len = len(power_data[0])
    zero_elems, one_elems = [], []
    for idx in range(start_idx, line_len):
        zero_elems = list(filter(lambda x: x[idx] == "0", power_data))
        one_elems = list(filter(lambda x: x[idx] == "1", power_data))
        one_count = (len(power_data) - len(zero_elems)) // (len(power_data) // 2)
        cond = one_count if target else 1 - one_count
        return (
            calc_target_rating(one_elems, start_idx + 1, target)
            if cond
            else calc_target_rating(zero_elems, start_idx + 1, target)
        )


def calc_power_consumption_part_2(power_data: List[int]) -> int:
    start_idx = 0
    oxygen_rating = calc_target_rating(power_data, start_idx, target=0)
    co2_rating = calc_target_rating(power_data, start_idx, target=1)
    return oxygen_rating * co2_rating


if __name__ == "__main__":
    records = process_input("./input.in")
    print("[1] Power consumption: ", calc_power_consumption_part_1(records))
    print("[2] Life support rating: ", calc_power_consumption_part_2(records))
