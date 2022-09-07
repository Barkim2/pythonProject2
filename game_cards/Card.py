class Card:     # ex.1

    def __init__(self, value: int, suit: str):
        # Initialize values in the object card
        self.value = value
        self.suit = suit    # name/ number

    def __gt__(self, other):  # 1 ->14
        # check which card has a bigger total value (value/suit)
        new_value = 0
        if self.value == 1 and other.value != 1:  #
            return True
        if self.value == 1 and other.value == 1:
            if self.suit > other.suit:
                return True
            return False
        if self.value > other.value:
            return True
        if self.value == other.value:
            if self.suit > other.suit:
                return True
            return False
        return False

    def __eq__(self, other):
        # check if value of cards is the same
        if self.value == other.value:
            return True
        return False
        # same suit?

    def __str__(self):
        return f"value of card: {self.value}  suit of card: {self.suit}"

    def __repr__(self):
        return f"value of card: {self.value}  suit of card: {self.suit}"
