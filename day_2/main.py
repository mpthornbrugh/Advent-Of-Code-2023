from inputs import *


def get_game_pieces(game):
    game_pieces = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    pieces = game.split(",")
    for piece in pieces:
        amount, color = piece.strip().split(" ")
        game_pieces[color] += int(amount)
    return game_pieces


def compare_pieces(game_pieces, allowed_pieces):
    for color, amount in game_pieces.items():
        if amount > allowed_pieces[color]:
            return False
    return True


def check_if_valid(game_round, allowed_pieces):
    game_definition, games = game_round.split(":", 1)
    game_number = int(game_definition.strip().split(" ")[-1])
    games = games.split(";")
    allowed = True
    for game in games:
        if allowed:
            this_game_pieces = get_game_pieces(game)
            allowed = compare_pieces(this_game_pieces, allowed_pieces)
    if allowed:
        return game_number
    else:
        return 0


def get_minimum_pieces(game_round):
    minimum_pieces = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    game_definition, games = game_round.split(":", 1)
    game_number = int(game_definition.strip().split(" ")[-1])
    games = games.split(";")
    for game in games:
        this_game_pieces = get_game_pieces(game)
        for color, amount in this_game_pieces.items():
            if amount > minimum_pieces[color]:
                minimum_pieces[color] = amount
    return minimum_pieces


def calculate_cube_piecies(pieces):
    # multiply red, green and blue
    return pieces["red"] * pieces["green"] * pieces["blue"]


def calculate(input_string):
    allowed_pieces = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    game_rounds = input_string.strip().split("\n")
    total = 0
    for game_round in game_rounds:
        minimum_pieces = get_minimum_pieces(game_round)
        cube_pieces = calculate_cube_piecies(minimum_pieces)
        total += cube_pieces
    print(total)


if __name__ == "__main__":
    calculate(puzzle_input)
