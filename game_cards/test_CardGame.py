from unittest import TestCase
from CardGame import CardGame
from DeckOfCards import DeckOfCards


class TestCardGame(TestCase):
    def setUp(self):
        self.card_play_1 = CardGame("a", "b", 3, 3)  # check!!
        self.deck = DeckOfCards()

    def test_valid__init__(self):
        self.assertEqual(self.card_play_1.player1.name, "a")
        self.assertEqual(self.card_play_1.player2.name, "b")
        self.assertEqual(self.card_play_1.player1.num_of_cards, 26)
        self.assertEqual(self.card_play_1.player2.num_of_cards, 26)
        # print(self.deck.cards)
        # self.assertEqual(self.card_play_1.deck.cards, self.deck.cards)

    def test_invalid__init__type_name_1(self):
        with self.assertRaises(TypeError):
            card_game = CardGame([1, 2, 3], "b", 26, 26)

    def test_invalid__init__type_name_2(self):
        with self.assertRaises(TypeError):
            card_game = CardGame("a", [1, 2, 3], 26, 26)

    def test_invalid__init__type_num_1(self):
        with self.assertRaises(TypeError):
            card_game = CardGame("a", "b", "26", 26)

    def test_invalid__init__type_num_2(self):
        with self.assertRaises(TypeError):
            card_game = CardGame("a", "b", 26, "26")

    def test_invalid__init__value_num_1(self):
        with self.assertRaises(ValueError):
            card_game = CardGame("a", "b", 0, 26)
        with self.assertRaises(ValueError):
            card_game = CardGame("a", "b", 27, 26)

    def test_invalid__init__value_num_2(self):
        with self.assertRaises(ValueError):
            card_game = CardGame("a", "b", 26, 0)
        with self.assertRaises(ValueError):
            card_game = CardGame("a", "b", 26, 27)




    def test_invalid_new_game(self):
        # deck of cards = 0, all cards at the players
        print(self.card_play_1)
        print(self.card_play_1.deck.cards)
        # self.card_play_1.deck.deal_one()
        # print(self.card_play_1.deck.cards)

        # self.assertFalse(self.card_play_1.new_game())
        # self.fail()

    # @mock.patch('Card_Game.Card_Game.new_game', return_value= NotImplemented)
    def test_valid_get_winner(self):
        self.card_play_1.new_game()     # num of card 26 - player1, player2
        self.card_play_1.player2.get_card()     # num of cards p1 = 26, p2 = 25
        self.assertTrue(self.card_play_1.get_winner())
