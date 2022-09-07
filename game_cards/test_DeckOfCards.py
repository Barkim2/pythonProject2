from unittest import TestCase
from DeckOfCards import DeckOfCards
from Card import Card


class TestDeckOfCards(TestCase):
    def setUp(self):
        self.d1 = DeckOfCards()

    def test_valid__init__(self):
        self.assertEqual(len(self.d1.cards), 52)
    # for

    def test_invalid__init__(self):
        # ["Diamond", "Spade", "Heart", "Club"]
        # self.assertNotEqual()
        # 52 max
        pass

    def test_cards_shuffle(self):
        self.d2 = DeckOfCards()
        self.d1.cards_shuffle()
        self.assertNotEqual(self.d1.cards, self.d2)

    def test_deal_one(self):
        self.fail()     # len = 0

