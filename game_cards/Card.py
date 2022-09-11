class Card:     # ex.1

    def __init__(self, value: int, suit: str):
        # Initialize values in the object of 'Card'
        if type(value) != int:       # checks if the value is not a number
            raise TypeError("Value of Card must be of type int!")
        if value < 1 or value > 13:  # checks if the value is valid (1-13)
            raise ValueError("Value of Card is only between 1-13!")
        if suit != "Diamond" and suit != "Spade" and suit != "Heart" and suit != "Club":
            # checks if suit of card is valid(one of the forth above)
            raise ValueError("suit of card must be one of these(of type string): 'Diamond', 'Spade', 'Heart', 'Club'")
        self.value = value
        self.suit = suit

    def suit_to_number(self, suit: str):
        # this function receive a suit as a string checks if it is valid, convert it to int
        # by the correct order and return it
        # checks if the suit is one of the valid card
        if suit != "Diamond" and suit != "Spade" and suit != "Heart" and suit != "Club":
            raise ValueError("suit of card must be one of these(of type string): 'Diamond', 'Spade', 'Heart', 'Club'")
        suit_list = ["Diamond", "Spade", "Heart", "Club"]
        # suit values: Diamond=1 Spade=2 Heart=3 Club=4
        suit_number = 0
        for i in range(len(suit_list)):
            if suit == suit_list[i]:    # suit value is value of list[i]
                suit_number = i + 1     # number of suit is value of list[i] + 1
        return suit_number

    def __gt__(self, other):
        # check which card has a bigger total value (value+suit)
        if type(other) != Card:     # check if received value is not Card
            raise TypeError("received value must be of type Card ")
        # converting str suit to a number (1-4)
        num_suit_other = self.suit_to_number(other.suit)
        num_suit_self = self.suit_to_number(self.suit)
        if self.value == 1 and other.value > 1:     # self_v: 1 (Ace)  other_v: 2-13 -> self
            return True
        if other.value == 1 and self.value > 1:     # self_v: 2-13  other_v: 1 (Ace) -> other
            return False
        # both numbers different from 1
        if self.value > other.value:
            return True
        if self.value == other.value:               # self_v = other_v then check self_suit
            if num_suit_self > num_suit_other:      # self_s > other_s -> self
                return True
            return False                            # self_s < other_s -> other
        if self.value < other.value:
            return False                            # self_v < other_v -> other

    def __eq__(self, other):
        # checks if two cards are equal
        if type(other) != Card:     # check if received value is not Card
            raise TypeError("received value must be of type Card ")
        # checks if two cards are totally equal (two different decks)
        if self.value == other.value:
            if self.suit == other.suit:
                return True
            # checks if two cards has the same value (one deck)
            return True
        return False

    def __str__(self):
        return f"value of card: {self.value}  suit of card: {self.suit}"

    def __repr__(self):
        return f"value of card: {self.value}  suit of card: {self.suit}"
