from collections import defaultdict
import poker_functions as pf


def simulate_games(num_games=100000, pick_count=5):
    deck = pf.generate_deck()
    counter = defaultdict(int)

    for _ in range(num_games):
        hand = pf.draw_hand(deck, pick_count)
        symbols, colors, symbol_counts = pf.get_hand_details(hand)

        if pf.is_royal_flush(symbols, colors):
            counter['Royal Flush'] += 1
        elif pf.is_straight_flush(symbols, colors):
            counter['Straight Flush'] += 1
        elif pf.has_same_values(symbol_counts, 4):
            counter['Vierling'] += 1
        elif pf.is_full_house(symbol_counts):
            counter['Full House'] += 1
        elif pf.is_flush(colors):
            counter['Flush'] += 1
        elif pf.is_street(symbols):
            counter['Straße'] += 1
        elif pf.is_two_pair(symbol_counts):
            counter['Zwei Paare'] += 1
        elif pf.has_same_values(symbol_counts, 3):
            counter['Drilling'] += 1
        elif pf.has_same_values(symbol_counts, 2):
            counter['Paar'] += 1

    return counter


if __name__ == '__main__':
    num_games = 1000000
    pick_count = int(input('How many cards should be drawn? '))
    counter = simulate_games(num_games, pick_count)

    for combination, count in counter.items():
        percent = (count / num_games) * 100
        print(f'{combination}: {percent:.2f}%')


# Royal Flush	    0.000154%
# Straight Flush	0.00139%
# Vierling	        0.0240%
# Full House	    0.1441%
# Flush	            0.197%
# Straße	        0.3925%
# Trilling	        2.1128%
# Doppelpaar	    4.7539%
# Paar	            42.2569%
