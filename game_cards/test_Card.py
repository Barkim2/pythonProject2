from unittest import TestCase
from Card import Card


class TestCard(TestCase):
    def setUp(self):
        self.c1 = Card(10, "Heart")

    def test_valid__init__(self):
        self.assertEqual(self.c1.value, 10)
        self.assertEqual(self.c1.suit, "Heart")
        self.c1 = Card(10, "Diamond")
        self.assertEqual(self.c1.suit, "Diamond")
        # test valid edge cases
        self.c1 = Card(1, "Spade")
        self.assertEqual(self.c1.suit, "Spade")
        self.assertEqual(self.c1.value, 1)
        self.c1 = Card(13, "Club")
        self.assertEqual(self.c1.suit, "Club")
        self.assertEqual(self.c1.value, 13)

    def test_invalid__init__type_value(self):
        with self.assertRaises(TypeError):
            c1 = Card("10", "Heart")

    def test_invalid__init__range_value(self):
        # edge cases
        with self.assertRaises(ValueError):
            c1 = Card(14, "Heart")
        with self.assertRaises(ValueError):
            c1 = Card(0, "Heart")

    def test_invalid__init__suit_value(self):
        with self.assertRaises(ValueError):
            c1 = Card(10, ["Heard", "clux", "diamons"])

    def test_valid_suit_to_number(self):
        self.assertEqual(self.c1.suit_to_number("Heart"), 3)

    def test_invalid_suit_to_number(self):
        self.assertNotEqual(self.c1.suit_to_number("Heart"), 2)

    def test_invalid_value_suit_to_number(self):
        with self.assertRaises(ValueError):
            c1 = Card(10, ["Heard", "clux", "diamons"])

    def test_valid__gt__type_card(self):
        self.assertEqual(type(self.c1), Card)

    def test_valid__gt__(self):
        # checks that 1 is equal more than 2-13 (the biggest card)
        self.c2 = Card(1, "Diamond")       # suit = 4
        self.c3 = Card(5, "Club")    # suit = 1
        self.assertTrue(self.c2.__gt__(self.c3))
        # checks the reverse case
        self.c2 = Card(5, "Club")  # suit = 4
        self.c3 = Card(1, "Diamond")  # suit = 1
        self.assertFalse(self.c2.__gt__(self.c3))
        # checks totally different cards
        self.c2 = Card(6, "Club")  # suit = 4
        self.c3 = Card(5, "Diamond")  # suit = 1
        self.assertTrue(self.c2.__gt__(self.c3))
        # checks when the value is equal, the biggest suit determine the biggest card
        self.c2 = Card(5, "Club")  # suit = 4
        self.c3 = Card(5, "Diamond")  # suit = 1
        self.assertTrue(self.c2.__gt__(self.c3))
        self.c2 = Card(5, "Diamond")  # suit = 4
        self.c3 = Card(5, "Club")  # suit = 1
        self.assertFalse(self.c2.__gt__(self.c3))
        # checks totally different cards
        self.c2 = Card(5, "Club")  # suit = 4
        self.c3 = Card(6, "Diamond")  # suit = 1
        self.assertFalse(self.c2.__gt__(self.c3))

    def test_invalid__gt__type(self):
        with self.assertRaises(TypeError):
            self.c1.__gt__(120)

    def test_valid__eq__(self):
        # checks if two cards are totally equal (two different decks)
        self.c2 = Card(10, "Heart")
        self.assertTrue(self.c1.__eq__(self.c2))
        # checks if only the value is equal (one deck)
        self.c2 = Card(11, "Heart")
        self.assertFalse(self.c1.__eq__(self.c2))
        self.c2 = Card(10, "Club")
        self.assertTrue(self.c1.__eq__(self.c2))

    def test_invalid__eq__type(self):
        with self.assertRaises(TypeError):
            self.c1.__eq__(120)
