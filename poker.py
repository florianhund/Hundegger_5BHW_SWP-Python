import random
from collections import defaultdict

colors = ("Karo", "Herz", "Pik", "Kreuz")
symbols = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14")
# 11 = Bube, 12 = Dame, 13 = König, 14 = Ass


def generate_deck():
    return [{"symbol": symbol, "color": color} for symbol in symbols for color in colors]


def draw_hand(deck):
    random.shuffle(deck)
    return deck[:5]


def get_hand_details(hand):
    symbols = [card["symbol"] for card in hand]
    colors = [card["color"] for card in hand]
    symbol_counts = {}

    for symbol in symbols:
        if symbol in symbol_counts:
            symbol_counts[symbol] += 1
        else:
            symbol_counts[symbol] = 1

    return symbols, colors, symbol_counts


def has_same_values(symbol_counts, count=2):
    return any(val == count for val in symbol_counts.values())


def is_two_pair(symbol_counts):
    return list(symbol_counts.values()).count(2) == 2


def is_full_house(symbol_counts):
    return has_same_values(symbol_counts, 2) and has_same_values(symbol_counts, 3)


def is_flush(colors):
    return len(set(colors)) == 1


def is_street(symbols):
    values = sorted([int(symbol) for symbol in symbols])
    return len(set(values)) == 5 and values[-1] - values[0] == 4


def is_straight_flush(symbols, colors):
    return is_flush(colors) and is_street(symbols)


def is_royal_flush(symbols, colors):
    return is_straight_flush(symbols, colors) and "14" in symbols


def simulate_games(num_games=100000):
    deck = generate_deck()
    counter = defaultdict(int)

    for _ in range(num_games):
        hand = draw_hand(deck)
        symbols, colors, symbol_counts = get_hand_details(hand)

        if is_royal_flush(symbols, colors):
            counter["Royal Flush"] += 1
        elif is_straight_flush(symbols, colors):
            counter["Straight Flush"] += 1
        elif has_same_values(symbol_counts, 4):
            counter["Vierling"] += 1
        elif is_full_house(symbol_counts):
            counter["Full House"] += 1
        elif is_flush(colors):
            counter["Flush"] += 1
        elif is_street(symbols):
            counter["Straße"] += 1
        elif is_two_pair(symbol_counts):
            counter["Zwei Paare"] += 1
        elif has_same_values(symbol_counts, 3):
            counter["Drilling"] += 1
        elif has_same_values(symbol_counts, 2):
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