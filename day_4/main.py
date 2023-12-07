from collections import defaultdict

from inputs import *


def get_card_values(card):
    card_number_desc, rest = card.split(":")
    card_number = int(card_number_desc.strip().split(" ")[-1])
    winning_numbers, card_numbers = rest.split("|")
    winning_numbers = [int(num) for num in winning_numbers.strip().split(" ") if num != ""]
    card_numbers = [int(num) for num in card_numbers.strip().split(" ") if num != ""]
    return card_number, winning_numbers, card_numbers


def calculate_part_2(input_string):
    cards = input_string.split('\n')
    total = 0
    multiplier_map = {}
    for card in cards:
        card_number, winning_numbers, card_numbers = get_card_values(card)
        multiplier = multiplier_map.get(card_number, 1)
        print(f"We have {multiplier} copies of card {card_number}")
        winning_number_map = {num: True for num in winning_numbers}
        # Calculate score for one instance of this card
        this_card_score = 0
        for num in card_numbers:
            if num in winning_number_map:
                this_card_score += 1
        print(f"Score for card {card_number} is {this_card_score}")
        # Add this cards score and apply the multiple copies of the card (multiplier)
        total += multiplier
        # Update the multiplier for the next cards based on the score of this card
        for i in range(card_number + 1, card_number + this_card_score + 1):
            if i not in multiplier_map:
                multiplier_map[i] = 1 + multiplier
            else:
                multiplier_map[i] += multiplier
    print(total)


def calculate(input_string):
    cards = input_string.split('\n')
    total = 0
    for card in cards:
        card_number, winning_numbers, card_numbers = get_card_values(card)
        winning_number_map = {num: True for num in winning_numbers}
        this_card_total = 0
        for num in card_numbers:
            if num in winning_number_map:
                if this_card_total == 0:
                    this_card_total = 1
                else:
                    this_card_total *= 2
        total += this_card_total
    print(total)


if __name__ == '__main__':
    calculate_part_2(puzzle_input)
