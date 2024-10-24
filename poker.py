import random
from collections import defaultdict


colors = ("Karo", "Herz", "Pik", "Kreuz")
symbols = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14")
# 11 = Bube, 12 = Dame, 13 = König, 14 = Ass


def generate_deck():
    deck = [
        {"symbol": symbol, "color": color} for symbol in symbols for color in colors
    ]
    return deck


def draw_hand(deck):
    random.shuffle(deck)
    return deck[:5]


def get_symbols(hand):
    return [card["symbol"] for card in hand]


def get_colors(hand):
    return [card["color"] for card in hand]


def has_same_values(hand, count=2):
    values = get_symbols(hand)
    for value in values:
        if values.count(value) == count:
            return True
    return False


def is_two_pair(hand):
    values = get_symbols(hand)
    pairs = set()

    for value in values:
        if values.count(value) == 2:
            pairs.add(value)

    return len(pairs) == 2


def is_full_house(hand):
    return has_same_values(hand, 2) and has_same_values(hand, 3)


def is_flush(hand):
    colors = get_colors(hand)
    return len(set(colors)) == 1


def is_street(hand):
    values = sorted([int(card["symbol"]) for card in hand])
    if len(set(values)) != 5:
        return False
    return values[-1] - values[0] == 4


def is_straight_flush(hand):
    return is_flush(hand) and is_street(hand)


def is_royal_flush(hand):
    return is_straight_flush(hand) and "14" in get_symbols(hand)


def simulate_games(num_games=100000):
    deck = generate_deck()
    counter = defaultdict(int)

    for _ in range(num_games):
        # optimize code to evaluate symbols and colors only once
        # to prevent for loop in every check
        hand = draw_hand(deck)

        if is_royal_flush(hand):
            counter["Royal Flush"] += 1
        elif is_straight_flush(hand):
            counter["Straight Flush"] += 1
        elif has_same_values(hand, 4):
            counter["Vierling"] += 1
        elif is_full_house(hand):
            counter["Full House"] += 1
        elif is_flush(hand):
            counter["Flush"] += 1
        elif is_street(hand):
            counter["Straße"] += 1
        elif is_two_pair(hand):
            counter["Zwei Paare"] += 1
        elif has_same_values(hand, 3):
            counter["Drilling"] += 1
        elif has_same_values(hand, 2):
            counter["Paar"] += 1

    return counter


if __name__ == "__main__":
    num_games = 100000
    counter = simulate_games(num_games)

    for combination, count in counter.items():
        percent = (count / num_games) * 100
        print(f"{combination}: {percent:.2f}%")


# Royal Flush	    0.000154%
# Straight Flush	0.00139%
# Vierling	        0.0240%
# Full House	    0.1441%
# Flush	            0.197%
# Straße	        0.3925%
# Trilling	        2.1128%
# Doppelpaar	    4.7539%
# Paar	            42.2569%
