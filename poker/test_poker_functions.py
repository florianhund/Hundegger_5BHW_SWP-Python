import unittest
import poker_functions as pf


class TestCardFunctions(unittest.TestCase):
    def test_generate_deck(self):
        deck = pf.generate_deck()
        self.assertEqual(len(deck), 52)
        self.assertIn({"symbol": "2", "color": "Karo"}, deck)

    def test_draw_hand(self):
        deck = pf.generate_deck()
        hand = pf.draw_hand(deck, 5)
        self.assertEqual(len(hand), 5)
        self.assertTrue(all(card in deck for card in hand))

    def test_get_hand_details(self):
        hand = [
            {"symbol": "2", "color": "Karo"},
            {"symbol": "3", "color": "Herz"},
            {"symbol": "2", "color": "Pik"},
        ]
        symbols, colors, symbol_counts = pf.get_hand_details(hand)
        self.assertEqual(symbols, ["2", "3", "2"])
        self.assertEqual(colors, ["Karo", "Herz", "Pik"])
        self.assertEqual(symbol_counts, {"2": 2, "3": 1})

    def test_has_same_values(self):
        self.assertTrue(pf.has_same_values({"2": 2, "3": 1}, 2))
        self.assertFalse(pf.has_same_values({"2": 1, "3": 1}, 2))

    def test_is_two_pair(self):
        self.assertTrue(pf.is_two_pair({"2": 2, "3": 2}))
        self.assertFalse(pf.is_two_pair({"2": 3, "3": 1}))

    def test_is_full_house(self):
        self.assertTrue(pf.is_full_house({"2": 3, "3": 2}))
        self.assertFalse(pf.is_full_house({"2": 3, "3": 1}))

    def test_is_flush(self):
        self.assertTrue(pf.is_flush(["Herz", "Herz", "Herz", "Herz", "Herz"]))
        self.assertFalse(pf.is_flush(["Herz", "Karo", "Herz", "Herz", "Herz"]))

    def test_is_street(self):
        self.assertTrue(pf.is_street(["10", "11", "12", "13", "14"]))
        self.assertFalse(pf.is_street(["10", "11", "12", "13", "15"]))

    def test_is_straight_flush(self):
        self.assertTrue(
            pf.is_straight_flush(
                ["10", "11", "12", "13", "14"], ["Herz", "Herz", "Herz", "Herz", "Herz"]
            )
        )
        self.assertFalse(
            pf.is_straight_flush(
                ["10", "11", "12", "13", "14"], ["Herz", "Karo", "Herz", "Herz", "Herz"]
            )
        )

    def test_is_royal_flush(self):
        self.assertTrue(
            pf.is_royal_flush(
                ["10", "11", "12", "13", "14"], ["Herz", "Herz", "Herz", "Herz", "Herz"]
            )
        )
        self.assertFalse(
            pf.is_royal_flush(
                ["9", "10", "11", "12", "13"], ["Herz", "Herz", "Herz", "Herz", "Herz"]
            )
        )


if __name__ == "__main__":
    unittest.main()
