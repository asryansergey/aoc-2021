from typing import List


def process_input(file_name):
    with open(file_name) as records:
        return [depth.strip() for depth in records]


def calc_power_consumption_part_1(power_data: List[int]) -> int:
    gamma_rates, epsilion_rates = "", ""
    line_len = len(power_data[0])
    zero_count = 0
    for idx in range(line_len):
        zero_count = 0
        for num in power_data:
            if num[idx] == "0":
                zero_count += 1
        one_count = len(power_data) - zero_count
        if one_count > zero_count:
            gamma_rates += "1"
            epsilion_rates += "0"
        else:
            epsilion_rates += "1"
            gamma_rates += "0"
    return int(gamma_rates, 2) * int(epsilion_rates, 2)


def calc_oxygen_rate(power_data: List[int], start_idx: int) -> int:
    if len(power_data) == 1:
        return int(power_data[0], 2)
    line_len = len(power_data[0])
    zero_count = 0
    ol, co2l = [], []
    for idx in range(start_idx, line_len):
        zero_count = 0
        for pos, num in enumerate(power_data):
            if num[idx] == "0":
                zero_count += 1
                co2l.append(num)
            else:
                ol.append(num)
        one_count = len(power_data) - zero_count
        if one_count >= zero_count:
            return calc_oxygen_rate(ol, start_idx + 1)
        else:
            return calc_oxygen_rate(co2l, start_idx + 1)


def calc_co2_rate(power_data: List[int], start_idx: int) -> int:
    if len(power_data) == 1:
        return int(power_data[0], 2)
    line_len = len(power_data[0])
    zero_count = 0
    ol, co2l = [], []
    for idx in range(start_idx, line_len):
        zero_count = 0
        for pos, num in enumerate(power_data):
            if num[idx] == "0":
                zero_count += 1
                co2l.append(num)
            else:
                ol.append(num)
        one_count = len(power_data) - zero_count
        if one_count >= zero_count:
            return calc_co2_rate(co2l, start_idx + 1)
        else:
            return calc_co2_rate(ol, start_idx + 1)


def calc_power_consumption_part_2(power_data: List[int]) -> int:
    return calc_oxygen_rate(power_data, 0) * calc_co2_rate(power_data, 0)


if __name__ == "__main__":
    records = process_input("./input.in")
    print("[1] Power consumption: ", calc_power_consumption_part_1(records))
    print("[2] Life support rating: ", calc_power_consumption_part_2(records))
