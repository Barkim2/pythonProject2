from Card import Card
from DeckOfCards import DeckOfCards
from Player import Player
from CardGame import CardGame

# c1 = Card(12,"D")
# c2 = Card(5,"H")
#
# # print(c2)
# # print(c1.__gt__(c2))
# # print(c1.__eq__(c2))
# #
# d1 = DeckOfCards()
# # # d1.cards_shuffle()
# # print(d1.deal_one())
# # print("======================")
# # print(d1)
#
# player1 = Player("q", 26)
# player1.set_hand(d1)
# print(player1)

# main:
name_1 = input("enter player_1 name: ")
name_2 = input("enter player_2 name: ")
card_game_1 = CardGame(name_1, name_2, 26, 26)
print(card_game_1)
print("-----------------------------------------------------------")
winner = True
for i in range(15):
    card_1 = card_game_1.player1.get_card()
    card_2 = card_game_1.player2.get_card()
    if card_1.__gt__(card_2):  # card_1 > card_2
        winner = True
        card_game_1.player1.add_card(card_1)
        card_game_1.player1.add_card(card_2)
    if card_2.__gt__(card_1):  # card_2 > card_1
        winner = False
        card_game_1.player2.add_card(card_1)
        card_game_1.player2.add_card(card_2)
    print("card_1:", card_1)
    print("card_2:", card_2)
    if winner:
        print(card_game_1.player1)
        print("len of list player1:", len(card_game_1.player1.pack_cards))
    else:
        print(card_game_1.player2)
        print("len of list player2:", len(card_game_1.player2.pack_cards))
    print("-----------------------------------------------------------")
winner_player = card_game_1.get_winner()
if winner_player == None:
    print("draw")
print("the winner is:") # + name
print(winner_player)