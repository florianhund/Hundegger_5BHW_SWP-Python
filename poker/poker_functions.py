import random


def generate_deck():
    """
    Generate a standard deck of 52 cards with symbols and colors.
    """
    colors = ("Karo", "Herz", "Pik", "Kreuz")
    symbols = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14")
    # 11 = Bube, 12 = Dame, 13 = König, 14 = Ass

    return [
        {"symbol": symbol, "color": color} for symbol in symbols for color in colors
    ]


def draw_hand(deck, card_amount=5):
    """
    Shuffle the deck and draw a specified number of cards (default: 5).
    """
    random.shuffle(deck)
    return deck[:card_amount]


def get_hand_details(hand):
    """
    Extract symbols, colors, and symbol counts from the hand.
    """
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
    """
    Check if any symbol appears the specified number of times.
    """
    return any(val == count for val in symbol_counts.values())


def is_two_pair(symbol_counts):
    """
    Check if the hand contains exactly two pairs of symbols.
    """
    return list(symbol_counts.values()).count(2) == 2


def is_full_house(symbol_counts):
    """
    Check if the hand is a full house (three of a kind and a pair).
    """
    return has_same_values(symbol_counts, 2) and has_same_values(symbol_counts, 3)


def is_flush(colors):
    """
    Check if all cards in the hand have the same color.
    """
    return len(set(colors)) == 1


def is_street(symbols):
    """
    Check if the hand is a straight (five consecutive symbols).
    """
    values = sorted([int(symbol) for symbol in symbols])
    return len(set(values)) == 5 and values[-1] - values[0] == 4


def is_straight_flush(symbols, colors):
    """
    Check if the hand is a straight flush (straight and flush).
    """
    return is_flush(colors) and is_street(symbols)


def is_royal_flush(symbols, colors):
    """
    Check if the hand is a royal flush (10, J, Q, K, A of the same color).
    """
    return is_straight_flush(symbols, colors) and "14" in symbols
