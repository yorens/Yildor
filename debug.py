import board
import deck
import game
import player
import players

if __name__ == '__main__':
    game = game.Game()
    game.start()
    game.debug_display()
    all_players_4 = players.Players()
    player_1 = player.Player("Yildiz")
    player_2 = player.Player("Steve")
    player_3 = player.Player("Aylin")
    player_4 = player.Player("Devran")
    all_players_4.add_player(player_1)
    all_players_4.add_player(player_2)
    all_players_4.add_player(player_3)
    all_players_4.add_player(player_4)
    all_players_4.display()

    all_players_3 = players.Players()
    all_players_3.add_player(player_1)
    all_players_3.add_player(player_2)
    all_players_3.add_player(player_3)
    all_players_3.display()

    all_players_2 = players.Players()
    all_players_2.add_player(player_1)
    all_players_2.add_player(player_2)
    all_players_2.display()
