class Card:     # ex.1

     # function check out str valid/invalid

    def __init__(self, value: int, suit: str):
        # Initialize values in the object card
        # card value is between 1-13
        # float
        if type(value) != int:
            raise TypeError("value of card must be int!")
        if value < 1 or value > 13:
            raise ValueError("card value is between 1-13!")
        if type(suit) != str:
            raise TypeError("suit of card must be str!")
        if suit != "Diamond" and suit != "Spade" and suit != "Heart" and suit != "Club":
            raise ValueError("suit of card must be one of these: 'Diamond', 'Spade', 'Heart', 'Club'")
        self.value = value
        self.suit = suit

    def suit_to_number(self, suit: str):
        # this function receive a suit as a string, and convert it to int
        # check if the suit is valid
        if type(suit) != str:
            raise TypeError("suit of card must be str!")
        if suit != "Diamond" and suit != "Spade" and suit != "Heart" and suit != "Club":
            raise ValueError("suit of card must be one of these: 'Diamond', 'Spade', 'Heart', 'Club'")
        suit_list = ["Diamond", "Spade", "Heart", "Club"]
        suit_number = 0
        for i in range(len(suit_list)):
            if suit == suit_list[i]:    # suit value is value of list[i]
                suit_number = i + 1     # number of suit is value of list[i] + 1
        return suit_number

    def __gt__(self, other):
        # check which card has a bigger total value (value/suit)
        if type(other) != Card:
            raise TypeError("received value must be of type Card ")
        num_suit_other = self.suit_to_number(other.suit)
        num_suit_self = self.suit_to_number(self.suit)
        if self.value == 1 and other.value > 1:     # self_v: 1  other_v: 2-13 -> self
            return True
        if other.value == 1 and self.value > 1:
            return False
        # both numbers different from 1
        if self.value > other.value:
            return True
        if self.value == other.value:               # self_v = other_v then check self_suit
            if num_suit_self > num_suit_other:      # self_s > other_s -> self
                return True
            return False                            # self_s < other_s -> other
        if self.value < other.value:
            return False                                # self_v < other_v -> other


    def __eq__(self, other):
        # check if value of cards is the same
        if self.value == other.value:
            return True
        return False

    def __str__(self):
        return f"value of card: {self.value}  suit of card: {self.suit}"

    def __repr__(self):
        return f"value of card: {self.value}  suit of card: {self.suit}"
