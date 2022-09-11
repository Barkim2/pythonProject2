from CardGame import CardGame


# main:
name_1 = input("enter player_1 name: ")
name_2 = input("enter player_2 name: ")
card_game_1 = CardGame(name_1, name_2, 26, 26)
print(card_game_1)
print("-----------------------------------------------------------")
winner = True
for i in range(10):
    card_1 = card_game_1.player1.get_card()
    card_2 = card_game_1.player2.get_card()
    if card_1.__gt__(card_2):  # card_1 > card_2
        winner = True
        card_game_1.player1.add_card(card_2)
        card_game_1.player1.add_card(card_1)
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
if winner_player is None:
    print("draw")
else:
    print("the winner is:", winner_player.name)
    print("length of pack of cards:", len(winner_player.pack_cards))
    print(winner_player)