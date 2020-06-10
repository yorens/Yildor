from Splendor_Functions import * 

rank_1_deck = []

# Sample game
print("Game Starting")
game = create_2_player_game("Jessie", "Steven")
rank_1_deck.append(create_card(1, "diamond", 0, 3, 1, 0, 0, 1))
rank_1_deck.append(create_card(1, "sapphire", 0, 0, 1, 3, 1, 0))
rank_1_deck.append(create_card(1, "emerald", 0, 2, 1, 0, 0, 0))
rank_1_deck.append(create_card(1, "ruby", 0, 1, 1, 1, 0, 1))
rank_1_deck.append(create_card(1, "onyx", 0, 1, 2, 1, 1, 0))
rank_1_deck.append(create_card(1, "onyx", 0, 1, 2, 1, 1, 0))
rank_1_deck.append(create_card(1, "onyx", 0, 1, 2, 1, 1, 0))
rank_1_deck.append(create_card(1, "onyx", 0, 1, 2, 1, 1, 0))
rank_1_deck.append(create_card(1, "onyx", 0, 1, 2, 1, 1, 0))
rank_1_deck.append(create_card(1, "onyx", 0, 1, 2, 1, 1, 0))
rank_1_deck.append(create_card(1, "diamond", 1, 0, 0, 4, 0, 0))
rank_1_deck.append(create_card(1, "diamond", 0, 0, 2, 0, 0, 2))
rank_1_deck.append(create_card(1, "diamond", 0, 0, 3, 0, 0, 0))
rank_1_deck.append(create_card(1, "diamond", 0, 0, 1, 1, 1, 1))
rank_1_deck.append(create_card(1, "diamond", 0, 0, 0, 0, 2, 1))
rank_1_deck.append(create_card(1, "diamond", 0, 0, 2, 2, 0, 1))
rank_1_deck.append(create_card(1, "diamond", 0, 0, 1, 2, 1, 1))
rank_1_deck.append(create_card(1, "diamond", 0, 3, 1, 0, 0, 1))
rank_1_deck.append(create_card(1, "sapphire", 1, 0, 0, 0, 4, 0))
rank_1_deck.append(create_card(1, "sapphire", 0, 1, 0, 0, 0, 2))
rank_1_deck.append(create_card(1, "sapphire", 0, 0, 0, 0, 0, 3))
rank_1_deck.append(create_card(1, "sapphire", 0, 1, 0, 1, 1, 1))
rank_1_deck.append(create_card(1, "sapphire", 0, 0, 0, 2, 0, 2))
rank_1_deck.append(create_card(1, "sapphire", 0, 1, 0, 2, 2, 0))
rank_1_deck.append(create_card(1, "sapphire", 0, 0, 1, 3, 1, 0))
rank_1_deck.append(create_card(1, "sapphire", 0, 1, 0, 1, 2, 1))
rank_1_deck.append(create_card(1, "emerald", 1, 0, 0, 0, 0, 4))
rank_1_deck.append(create_card(1, "emerald", 0, 0, 2, 0, 2, 0))
rank_1_deck.append(create_card(1, "emerald", 0, 0, 1, 0, 2, 2))
rank_1_deck.append(create_card(1, "emerald", 0, 2, 1, 0, 0, 0))
rank_1_deck.append(create_card(1, "emerald", 0, 1, 1, 0, 1, 1))
rank_1_deck.append(create_card(1, "emerald", 0, 1, 1, 0, 1, 2))
rank_1_deck.append(create_card(1, "emerald", 0, 0, 0, 0, 3, 0))
rank_1_deck.append(create_card(1, "emerald", 0, 1, 3, 1, 0, 0))
rank_1_deck.append(create_card(1, "ruby", 1, 4, 0, 0, 0, 0))
rank_1_deck.append(create_card(1, "ruby", 0, 2, 1, 1, 0, 1))
rank_1_deck.append(create_card(1, "ruby", 0, 3, 0, 0, 0, 0))
rank_1_deck.append(create_card(1, "ruby", 0, 1, 1, 1, 0, 1))
rank_1_deck.append(create_card(1, "ruby", 0, 2, 0, 1, 0, 2))
rank_1_deck.append(create_card(1, "ruby", 0, 0, 2, 1, 0, 0))
rank_1_deck.append(create_card(1, "ruby", 0, 2, 0, 0, 2, 0))
rank_1_deck.append(create_card(1, "ruby", 0, 1, 0, 0, 1, 3))
rank_1_deck.append(create_card(1, "onyx", 1, 0, 4, 0, 0, 0))
rank_1_deck.append(create_card(1, "onyx", 0, 1, 1, 1, 1, 0))
rank_1_deck.append(create_card(1, "onyx", 0, 0, 0, 3, 0, 0))
rank_1_deck.append(create_card(1, "onyx", 0, 1, 2, 1, 1, 0))
rank_1_deck.append(create_card(1, "onyx", 0, 0, 0, 1, 3, 1))
rank_1_deck.append(create_card(1, "onyx", 0, 0, 0, 2, 1, 0))
rank_1_deck.append(create_card(1, "onyx", 0, 2, 2, 0, 1, 0))
rank_1_deck.append(create_card(1, "onyx", 0, 2, 0, 2, 0, 0))


# rank_1_cards_dealt = [rank_1_deck[0], rank_1_deck[1], rank_1_deck[2], rank_1_deck[3]]
game[0][3] = rank_1_deck

start_game_with_deck(game)
# draw_board(game)
# time.sleep(3)
print("Player 1 takes turn 1")
# player 1
remove_chips_from_bank(game[1][4], "diamond", 1)
remove_chips_from_bank(game[1][4], "emerald", 1)
remove_chips_from_bank(game[1][4], "ruby", 1)
game[2][0][2][0] += 1
game[2][0][2][2] += 1
game[2][0][2][3] += 1
# draw_board(game)
# time.sleep(3)
print("Player 2 takes turn 1")
# player 2
remove_chips_from_bank(game[1][4], "onyx", 2)
game[2][1][2][4] += 2
# draw_board(game)
# time.sleep(3)
print("Player 1 takes turn 2")
# player 1
remove_chips_from_bank(game[1][4], "sapphire", 1)
remove_chips_from_bank(game[1][4], "onyx", 1)
remove_chips_from_bank(game[1][4], "ruby", 1)
game[2][0][2][1] += 1
game[2][0][2][4] += 1
game[2][0][2][3] += 1
# draw_board(game)
# time.sleep(3)
print("Player 2 takes turn 2")
# player 2
remove_chips_from_bank(game[1][4], "sapphire", 1)
remove_chips_from_bank(game[1][4], "onyx", 1)
remove_chips_from_bank(game[1][4], "ruby", 1)
game[2][1][2][1] += 1
game[2][1][2][4] += 1
game[2][1][2][3] += 1
# draw_board(game)
# time.sleep(3)
print("Player 1 takes turn 3")
# player 1
remove_chips_from_bank(game[1][4], "diamond", 1)
remove_chips_from_bank(game[1][4], "sapphire", 1)
remove_chips_from_bank(game[1][4], "onyx", 1)
game[2][0][2][0] += 1
game[2][0][2][1] += 1
game[2][0][2][4] += 1
# draw_board(game)
# time.sleep(3)
print("Player 2 takes turn 3")
# player 2
remove_chips_from_bank(game[1][4], "diamond", 1)
remove_chips_from_bank(game[1][4], "sapphire", 1)
remove_chips_from_bank(game[1][4], "onyx", 1)
game[2][1][2][0] += 1
game[2][1][2][1] += 1
game[2][1][2][4] += 1
# draw_board(game)
# time.sleep(3)
print("Player 1 takes turn 4")
# player 1
remove_chips_from_bank(game[1][4], "diamond", 2)
game[2][0][2][0] += 2
draw_board(game)
# time.sleep(3)
print("Player 2 takes turn 4")
# player 2
purchase_next_available_card(game, 2)
game = add_chips_to_bank(game, "diamond", 1)
game = add_chips_to_bank(game, "ruby", 1)
game = add_chips_to_bank(game, "onyx", 3)
draw_board(game)