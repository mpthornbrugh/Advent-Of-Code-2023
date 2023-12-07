from inputs import *


individual_card_values = {
    "A": "14",
    "K": "13",
    "Q": "12",
    # "J": "11",
    "T": "10",
    "9": "09",
    "8": "08",
    "7": "07",
    "6": "06",
    "5": "05",
    "4": "04",
    "3": "03",
    "2": "02",
    "J": "01",
}


def get_hand_rank(cards_count):
    # Part 2
    # Jokers count towards the best ranking
    joker_count = cards_count.get("J", 0)

    if (len(cards_count) == 1) or (len(cards_count) == 2 and "J" in cards_count):
        # 5 of a kind
        return 7
    elif len(cards_count) == 2 and "J" not in cards_count:
        # If either of the 2 counts is 4, it's 4 of a kind
        if 4 in cards_count.values():
            return 6
        # Otherwise a full house
        else:
            return 5
    elif len(cards_count) == 3 and "J" in cards_count:
        # If we have 3 different card types, but enough jokers to make a 4 of a kind, it's 4 of a kind
        if (4 - joker_count) in cards_count.values():
            return 6
        # Otherwise it's a full house
        else:
            return 5
    elif len(cards_count) == 3 and "J" not in cards_count:
        # If any of the 3 counts is 3, it's 3 of a kind
        if 3 in cards_count.values():
            return 4
        # Otherwise it's 2 pairs
        else:
            return 3
    elif len(cards_count) == 4 and "J" in cards_count:
        # If we have 4 different card types, but enough jokers to make a 3 of a kind, it's 3 of a kind
        if (3 - joker_count) in cards_count.values():
            return 4
        # Otherwise it's 2 pairs
        else:
            return 3
    elif joker_count > 0:
        # If we have jokers, it's a pair
        return 2
    elif len(cards_count) == 4:
        # If we don't have 5 different cards, it's a pair
        return 2
    else:
        # If we have 5 different cards, it's a high card
        return 1


def get_value(hand):
    cards_value = []
    cards_count = {}
    for card_num, card in enumerate(hand):
        card_value = individual_card_values.get(card[0])
        cards_value.append(card_value)
        cards_count[card] = cards_count.get(card, 0) + 1
    rank = get_hand_rank(cards_count)
    return int(str(rank) + "".join(cards_value))


def get_total_value(hand_values):
    result = 0
    for hand_num, hand_value in enumerate(hand_values):
        result += (hand_num + 1) * hand_value["bid"]
    return result


def calculate(input_string):
    hands = input_string.split("\n")
    hand_values = []
    for hand in hands:
        hand, bid = hand.split(" ")
        hand_value = get_value(hand)
        hand_values.append({
            "hand": hand,
            "bid": int(bid),
            "value": hand_value
        })
    # Sort the hand values by the value
    hand_values.sort(key=lambda x: x["value"])
    print(get_total_value(hand_values))


if __name__ == "__main__":
    # calculate(example_input)
    calculate(puzzle_input)
