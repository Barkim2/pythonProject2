from Card import Card       # ex.2
import random


class DeckOfCards:
    def __init__(self):
        # creates a list of cards
        self.cards = []
        suit_list = ["Diamond", "Spade", "Heart", "Club"]      # list of suits
        suit_counter = 0
        suit = suit_list[0]
        i = 0
        # builds 13 cards (values is i 1-13) and changes the type of every 13 cards
        while suit_counter <= 3:
            i = i + 1
            c = Card(i, suit)
            self.cards.append(c)    # insert the card i = value, suit(str)
            if i == 13:
                # after 13 cards of same type - change type to the next par in the list
                i = 0
                suit_counter += 1   # change of type
                if suit_counter == 4:   # there are only 4 types (list[0]-list[3])
                    break
                suit = suit_list[suit_counter]

    def __str__(self):
        return f"list of cards: {self.cards}"

    # def __repr__(self):
    #     return f"list of cards: {self.cards}"

    def cards_shuffle(self):
        # shuffle the cards in the list using python function (shuffle from random)
        random.shuffle(self.cards)

    def deal_one(self):
        # raffle an index in the range all the
        # list's par (raffle index and not a value)
        len_of_list = len(self.cards)
        index = random.randint(0, len_of_list-1)
        # remove a card from the list by his index
        c = self.cards.pop(index)
        return c
