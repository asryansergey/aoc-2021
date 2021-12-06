from typing import List


def process_input(file_name):
    with open(file_name) as records:
        game_numbers = [int(num) for num in records.readline().split(",")]
        cards = []
        current_card = []
        for line in records.readlines()[1:]:
            if line == "\n":
                cards.append(current_card.copy())
                current_card.clear()
            else:
                current_card.append(
                    [[int(x.strip()), 0] for x in line.split(" ") if x != ""]
                )
        cards.append(current_card.copy())
        return game_numbers, cards

def update_cards(number_called: int, cards: List[List[List[List[int]]]]):
    for card in cards:
        for line in card:
            for elem in line:
                if number_called == elem[0]:
                    elem[1] = 1

def calc_winning_board_value(random_numbers: List[int], cards: List[List[List[List[int]]]]) -> dict[int, int]:
    wins = {}
    trace = []
    for key_idx, num in enumerate(random_numbers):
        for card_num, card in enumerate(cards):
            if card_num in trace:
                continue
            for idx, line in enumerate(card):
                if all([x[1] for x in line]):
                    score = sum([sum([x[0] for x in row if x[1] == 0]) for row in card])
                    wins[key_idx] = score * random_numbers[key_idx - 1]
                    trace.append(card_num)

            for i in range(5):
                win = True
                for line in card:
                    if line[i][1] == 0:
                        win = False
                        break
                if win:
                    score = sum([sum([x[0] for x in row if x[1] == 0]) for row in card])
                    wins[key_idx] = score * random_numbers[key_idx - 1]
                    trace.append(card_num)

        update_cards(num, cards)
    return wins


if __name__ == "__main__":
    random_numbers, cards = process_input("./input.in")
    wins = calc_winning_board_value(random_numbers, cards)
    first_idx = min(list(wins))
    first_win_score = wins[first_idx]
    print("[1] First win score: ", first_win_score)
    last_idx = max(list(wins))
    last_win_score = wins[last_idx]
    print("[2] Last win score: ", last_win_score)
