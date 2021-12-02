from typing import List, Tuple


def process_input(file_name):
    with open(file_name) as records:
        return [
            (cmd.split(" ")[0].strip(), int(cmd.split(" ")[1].strip()))
            for cmd in records
        ]


def calc_position_values_part_1(cmds: List[Tuple[str, int]]):
    h, d = 0, 0
    for op, val in cmds:
        if op == "forward":
            h += val
        else:
            d = d - val if op == "up" else d + val
    return d * h


def calc_position_values_part_2(cmds: List[Tuple[str, int]]):
    aim, h, d = 0, 0, 0
    for op, val in cmds:
        if op == "forward":
            h += val
            d += aim * val
        else:
            aim = aim - val if op == "up" else aim + val
    return d * h


if __name__ == "__main__":
    commands = process_input("./input.in")
    print("[1] horizontal * depth", calc_position_values_part_1(commands))
    print("[2] horizontal * depth", calc_position_values_part_2(commands))
