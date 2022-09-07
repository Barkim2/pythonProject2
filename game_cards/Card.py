class Card:     # ex.1

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

    def __gt__(self, other):  # 1 ->14
        # check which card has a bigger total value (value/suit)
        num_suit_other = self.suit_to_number(other.suit)
        num_suit_self = self.suit_to_number(self.suit)
        if self.value == 1 and other.value > 1:
            return True
        if self.value == 1 and other.value == 1:
            if num_suit_self > num_suit_other:
                return True
            return False
        if other.value == 1 and self.value > 1:
            return False
        if self.value == 1 and other.value == 1:
            if num_suit_other > num_suit_self:  # convert to numbers
                return False
            return True
        if self.value > other.value:
            return True
        if self.value == other.value:
            if num_suit_self > num_suit_other:
                return True
            return False
        return False


    def __eq__(self, other):
        # check if value of cards is the same
        if self.value == other.value:
            return True
        return False

    def __str__(self):
        return f"value of card: {self.value}  suit of card: {self.suit}"

    def __repr__(self):
        return f"value of card: {self.value}  suit of card: {self.suit}"
