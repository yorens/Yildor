import player

FOUR_PLAYER_BUFFER = "      "
THREE_PLAYER_BUFFER = "                 "
TWO_PLAYER_BUFFER = "                         "


class Players:
    def __init__(self):
        self.players = []

    def __getitem__(self, key):
        return self.players[key]

    def add_player(self, player):
        self.players.append(player)

    def display(self):
        print(self.row_header())
        print(self.row_1())
        print(self.row_2())
        print(self.row_3())
        print(self.row_4())
        print(self.row_5())
        print(self.row_6())
        print(self.row_7())
        print(self.row_8())
        print(self.row_footer())

    def row_header(self):
        buffer = ""
        length = len(self.players)
        for player in self.players:
            if length == 4:
                if player != self.players[0]:
                    buffer += FOUR_PLAYER_BUFFER
            if length == 3:
                if player != self.players[0]:
                    buffer += THREE_PLAYER_BUFFER
            if length == 2:
                if player != self.players[0]:
                    buffer += TWO_PLAYER_BUFFER
            buffer += "┌────────────────────────┐"
        return buffer

    def row_1(self):
        return 0

    def row_2(self):
        return 0

    def row_3(self):
        return 0

    def row_4(self):
        return 0

    def row_5(self):
        return 0

    def row_6(self):
        return 0

    def row_7(self):
        return 0

    def row_8(self):
        return 0

    def row_footer(self):
        buffer = ""
        length = len(self.players)
        for player in self.players:
            if length == 4:
                if player != self.players[0]:
                    buffer += FOUR_PLAYER_BUFFER
            if length == 3:
                if player != self.players[0]:
                    buffer += THREE_PLAYER_BUFFER
            if length == 2:
                if player != self.players[0]:
                    buffer += TWO_PLAYER_BUFFER
            buffer += "└────────────────────────┘"
        return buffer