import random
from collections import Counter, defaultdict

colors = ["Karo", "Herz", "Pik", "Kreuz"]
symbols = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Bube", "Dame", "König", "Ass"]


def generate_card():
    deck = [(symbol, farbe) for symbol in symbols for farbe in colors]
    return deck


def draw_hand(deck):
    return random.sample(deck, 5)


def has_same_values(hand, count=2):
    values = [card[0] for card in hand]
    for value in values:
        if values.count(value) == count:
            return True
    return False


def is_full_house(hand):
    values = [card[0] for card in hand]
    counts = [values.count(value) for value in set(values)]
    return 2 in counts and 3 in counts


def is_flush(hand):
    colors = [card[1] for card in hand]
    return len(set(colors)) == 1


def is_street(hand):
    value_map = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "Bube": 11,
        "Dame": 12,
        "König": 13,
        "Ass": 14
    }

    values = sorted([value_map[card[0]] for card in hand])
    return values[-1] - values[0] == 4


def is_straight_flush(hand):
    return is_flush(hand) and is_street(hand)


def simulate_games(num_games=100000):
    deck = generate_card()
    counter = defaultdict(int)

    for _ in range(num_games):
        hand = draw_hand(deck)
        if is_straight_flush(hand):
            counter["Straight Flush"] += 1
        elif is_flush(hand):
            counter["Flush"] += 1
        elif is_street(hand):
            counter["Straße"] += 1
        elif has_same_values(hand, 4):
            counter["Vierling"] += 1
        elif is_full_house(hand):
            counter["Full House"] += 1
        elif has_same_values(hand, 3):
            counter["Drilling"] += 1
        elif has_same_values(hand, 2):
            counter["Paar"] += 1

    return counter


if __name__ == "__main__":
    num_games = 100000
    counter = simulate_games(num_games)

    for kombination, count in counter.items():
        percent = (count / num_games) * 100
        print(f"{kombination}: {percent:.2f}%")

    # Hier könnten theoretische Wahrscheinlichkeiten aus dem Netz recherchiert werden und verglichen werden.
