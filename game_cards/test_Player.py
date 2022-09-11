from unittest import TestCase
from Player import Player
from Card import Card
from DeckOfCards import DeckOfCards


class TestPlayer(TestCase):
    def setUp(self):
        self.p1 = Player("a", 26)

    def test_valid__init__(self):
        self.assertEqual(self.p1.name, "a")
        self.assertEqual(self.p1.num_of_cards, 26)
        self.assertEqual(self.p1.pack_cards, [])

    def test_invalid__init__type_num(self):
        with self.assertRaises(TypeError):
            p1 = Player("a", 1.23)

    def test_invalid__init__value_name(self):
        with self.assertRaises(ValueError):
            p1 = Player("a", 0)
        with self.assertRaises(ValueError):
            p1 = Player("a", 53)
        with self.assertRaises(ValueError):
            p1 = Player("a", -1)

    def test_valid__init__range_number(self):
        self.p1 = Player("a", 9)
        self.assertEqual(self.p1.num_of_cards, 26)
        self.p1 = Player("a", 10)
        self.assertEqual(self.p1.num_of_cards, 10)
        self.p1 = Player("a", 11)
        self.assertEqual(self.p1.num_of_cards, 11)
        self.p1 = Player("a", 27)
        self.assertEqual(self.p1.num_of_cards, 26)

    def test_valid_set_hand(self):
        # dividing number of cards to p1, checks that the number of cards
        # of the player and the number of card left in the pack
        self.deck = DeckOfCards()
        self.p1 = Player("a", 20)
        self.p1.set_hand(self.deck)
        self.assertEqual(len(self.p1.pack_cards), 20)  # checks amount of p1 cards
        self.assertEqual(len(self.deck.cards), 32)  # checks amount of cards at the deck

    def test_invalid_set_hand_value_empty_deck(self):
        # checks a case when deck of cards is empty
        # ant the player tries to divide cards from it
        self.deck = DeckOfCards()
        self.deck.cards.clear()     # turning the list of cards empty
        with self.assertRaises(ValueError):
            self.p1.set_hand(self.deck)

    def test_invalid_set_hand_type(self):
        # checks a case when the received element is not of class DeckOfCards\
        with self.assertRaises(TypeError):
            self.p1.set_hand("deck1")

    def test_valid_get_card(self):
        # len = 0 invalid, empty list
        self.c1 = Card(7, "Heart")
        self.p1.add_card(self.c1)
        self.p1.get_card()
        self.assertNotIn((7, "Heart"), self.p1.pack_cards)

    def test_invalid_get_card_empty_deck(self):
        # checks a case when deck of cards is empty,
        # and a plater tries to get card
        self.p1.pack_cards.clear()  # turning the list of cards empty
        with self.assertRaises(ValueError):
            self.p1.get_card()

    def test_valid_add_card(self):
        self.c1 = Card(7, "Heart")
        self.p1.add_card(self.c1)
        self.assertIn(self.c1, self.p1.pack_cards)

    def test_invalid_add_card(self):
        with self.assertRaises(TypeError):
            self.p1.add_card(120)
