from Splendor_Functions import *


# Sample game
print("Game Starting")
game = create_2_player_game("Jessie", "Steven")
start_game(game)
draw_board(game)
print("Player 1 takes turn 1")
time.sleep(3)
# player 1
remove_chips_from_bank(game[1][4], "diamond", 1)
remove_chips_from_bank(game[1][4], "emerald", 1)
remove_chips_from_bank(game[1][4], "ruby", 1)
game[2][0][2][0] += 1
game[2][0][2][2] += 1
game[2][0][2][3] += 1
draw_board(game)
print("Player 2 takes turn 1")
time.sleep(3)
# player 2
remove_chips_from_bank(game[1][4], "onyx", 2)
game[2][1][2][0] += 1
game[2][1][2][2] += 1
game[2][1][2][3] += 1
draw_board(game)
time.sleep(3)
# player 1
remove_chips_from_bank(game[1][4], "sapphire", 1)
remove_chips_from_bank(game[1][4], "onyx", 1)
remove_chips_from_bank(game[1][4], "ruby", 1)
game[2][0][2][1] += 1
game[2][0][2][4] += 1
game[2][0][2][3] += 1
draw_board(game)
time.sleep(3)
# player 2
remove_chips_from_bank(game[1][4], "sapphire", 1)
remove_chips_from_bank(game[1][4], "onyx", 1)
remove_chips_from_bank(game[1][4], "ruby", 1)
game[2][1][2][1] += 1
game[2][1][2][4] += 1
game[2][1][2][3] += 1
draw_board(game)
time.sleep(3)
# player 1
remove_chips_from_bank(game[1][4], "diamond", 1)
remove_chips_from_bank(game[1][4], "sapphire", 1)
remove_chips_from_bank(game[1][4], "onyx", 1)
game[2][0][2][0] += 1
game[2][0][2][1] += 1
game[2][0][2][4] += 1
draw_board(game)
time.sleep(3)
# player 2
remove_chips_from_bank(game[1][4], "diamond", 1)
remove_chips_from_bank(game[1][4], "sapphire", 1)
remove_chips_from_bank(game[1][4], "onyx", 1)
game[2][1][2][0] += 1
game[2][1][2][1] += 1
game[2][1][2][4] += 1
draw_board(game)
time.sleep(3)
# player 1
purchase_next_available_card(game, 1)
draw_board(game)
time.sleep(3)
# player 2
purchase_next_available_card(game, 2)
draw_board(game)
