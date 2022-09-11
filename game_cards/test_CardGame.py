from CardGame import CardGame
from unittest import TestCase


class TestCardGame(TestCase):
    def setUp(self):
        self.card_play_1 = CardGame("a", "b", 26, 26)  # * 3

    def test_valid__init__(self):
        # check if card_game object has built right
        self.assertEqual(self.card_play_1.player1.name, "a")
        self.assertEqual(self.card_play_1.player2.name, "b")
        self.assertEqual(self.card_play_1.player1.num_of_cards, 26)
        self.assertEqual(self.card_play_1.player2.num_of_cards, 26)
        # there is no need to check all names and number of cards
        # because it is already been tested in class Player
        self.assertTrue(self.card_play_1.new_game_happened)  # check that new_game worked
        self.assertEqual(self.card_play_1.deck.cards, [])  # list of cards is empty because new_game worked

    def test_invalid__init__value_num_1(self):
        with self.assertRaises(ValueError):
            card_game = CardGame("a", "b", 0, 26)
        with self.assertRaises(ValueError):
            card_game = CardGame("a", "b", 27, 26)

        with self.assertRaises(ValueError):
            card_game = CardGame("a", "b", 26, 0)
        with self.assertRaises(ValueError):
            card_game = CardGame("a", "b", 26, 27)

    def test_invalid__init__type(self):
        with self.assertRaises(TypeError):
            card_game = CardGame("a", "b", "a", 26)
        with self.assertRaises(TypeError):
            card_game = CardGame("a", "b", 27, [26,28,30])

    def test_valid_new_game(self):
        # adding cards from the deck to player 1 and player 2
        self.c1 = CardGame("bar", "ariel", 10, 10)
        self.assertTrue(self.card_play_1.new_game_happened)     # the function has been called from the __init__
        self.assertEqual(32, len(self.c1.deck.cards))
        self.assertEqual(10, len(self.c1.player1.pack_cards))
        self.assertEqual(10, len(self.c1.player2.pack_cards))

    def test_valid_get_winner_p1(self):
        # num of card 26 - player1, player2
        self.card_play_1.player2.get_card()     # num of cards p1 = 26, p2 = 25
        self.assertEqual(self.card_play_1.get_winner(), self.card_play_1.player1)

    def test_valid_get_winner_p2(self):
        # num of card 26 - player1, player2
        self.card_play_1.player1.get_card()  # num of cards p1 = 25, p2 = 26
        self.assertEqual(self.card_play_1.get_winner(), self.card_play_1.player2)

    def test_valid_get_winner_draw(self):
        # num of card is equal for both players - 26
        self.assertEqual(self.card_play_1.get_winner(), None)
