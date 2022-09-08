from unittest import TestCase, mock
from unittest.mock import patch
from DeckOfCards import DeckOfCards
from Card import Card


class TestDeckOfCards(TestCase):
    def setUp(self):
        self.d1 = DeckOfCards()

    def test_valid__init__(self):
        # checks that the __init__ creates a full pack of the right cards
        self.assertEqual(len(self.d1.cards), 52)  # checks length of full list - 52
        suit_list = ["Diamond", "Spade", "Heart", "Club"]  # list of suits
        self.card1 = Card(1, "Diamond")
        # checks every card in the deck, by cards of a regular deck
        for i in range(4):
            self.card1.suit = suit_list[i]
            for j in range(13):
                self.card1.value = j + 1
                self.assertEqual(self.d1.cards[j], self.card1)

    def test_invalid__init__(self):
        pass

    def test_cards_shuffle(self):
        self.d2 = DeckOfCards()
        self.d1.cards_shuffle()
        self.assertNotEqual(self.d1.cards, self.d2)

    def test_deal_one(self):    #
        self.d1 = DeckOfCards()
        self.card1 = self.d1.deal_one()
        self.assertEqual(len(self.d1.cards), 51)
        self.assertNotIn(self.card1, self.d1.cards)
        # self.assertNotIn((7, "Heart"), self.p1.pack_cards)

    def test_invalid_deal_one(self):
        # checks a case when the player tries to deal a card
        # and the list of card is empty
        self.d1.cards.clear()   # turning list empty
        print(self.d1.cards)
        with self.assertRaises(ValueError):
            self.d1.deal_one()


