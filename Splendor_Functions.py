import random

random.seed()

RANK_INDEX = 0
GEM_INDEX = 1
POINT_INDEX = 2
COST_INDEX = 3

DIAMOND_COST_INDEX = 0
SAPPHIRE_COST_INDEX = 1
EMERALD_COST_INDEX = 2
RUBY_COST_INDEX = 3
ONYX_COST_INDEX = 4


def row_header(card_datas):
    buffer = ""
    for i in range(len(card_datas)):
        if i > 0:
            buffer += "      "
        buffer += "┌────────────────────────┐"
    return buffer

def row_1(card_datas):
    buffer = ""
    for i in range(len(card_datas)):
        spaces = 22
        if i > 0:
            buffer += "      " 
        spaces -= len(card_datas[i][GEM_INDEX])
        buffer += "| "+str(card_datas[i][POINT_INDEX]) + (" " * spaces) +str(card_datas[i][GEM_INDEX])+"|"
    return buffer

def row_2(card_datas):
    buffer = ""
    for i in range(len(card_datas)):
        if i > 0:
            buffer += "      " 
        buffer += "|        Rank "+str(card_datas[i][RANK_INDEX])+"          |"
    return buffer

def row_3(card_datas):
    buffer = ""
    for i in range(len(card_datas)):
        if i > 0:
            buffer += "      " 
        buffer += "| "+str(card_datas[i][COST_INDEX][DIAMOND_COST_INDEX])+" Diamond(s)           |"
    return buffer

def row_4(card_datas):
    buffer = ""
    for i in range(len(card_datas)):
        if i > 0:
            buffer += "      " 
        buffer += "| "+str(card_datas[i][COST_INDEX][SAPPHIRE_COST_INDEX])+" Sapphire(s)          |"
    return buffer

def row_5(card_datas):
    buffer = ""
    for i in range(len(card_datas)):
        if i > 0:
            buffer += "      " 
        buffer += "| "+str(card_datas[i][COST_INDEX][EMERALD_COST_INDEX])+" Emerald(s)           |"
    return buffer

def row_6(card_datas):
    buffer = ""
    for i in range(len(card_datas)):
        if i > 0:
            buffer += "      " 
        buffer += "| "+str(card_datas[i][COST_INDEX][RUBY_COST_INDEX])+" Ruby(s)              |"
    return buffer

def row_7(card_datas):
    buffer = ""
    for i in range(len(card_datas)):
        if i > 0:
            buffer += "      " 
        buffer += "| "+str(card_datas[i][COST_INDEX][ONYX_COST_INDEX])+" Onyx(s)              |"
    return buffer

def row_footer(card_datas):
    buffer = ""
    for i in range(len(card_datas)):
        if i > 0:
            buffer += "      "
        buffer += "└────────────────────────┘"
    return buffer

def noble_footer(card_datas, num_players):
    buffer = ""
    for i in range(len(card_datas)):
        if num_players == 4:
            if i > 0:
                buffer += "   "
            buffer += "└────────────────────┘"
        elif num_players == 3:
            if i > 0:
                buffer += "      "
            buffer += "└────────────────────────┘"
        elif num_players == 2:
            if i > 0:
                buffer += "                         "
            buffer += "└──────────────────────┘"
    return buffer

def noble_header(card_datas, num_players):
    buffer = ""
    for i in range(len(card_datas)):
        if num_players == 4:
            if i > 0:
                buffer += "   "
            buffer += "┌────────────────────┐"
        elif num_players == 3:
            if i > 0:
                buffer += "      "
            buffer += "┌────────────────────────┐"
        elif num_players == 2:
            if i > 0:
                buffer += "                         "
            buffer += "┌──────────────────────┐"
    return buffer

def noble_row_1(card_datas, num_players):
    buffer = ""
    for i in range(len(card_datas)):
        if num_players == 4:
            spaces = 13
            if i > 0:
                buffer += "   "
            buffer += "| "+str(card_datas[i][POINT_INDEX]) + (" " * spaces) +str(card_datas[i][GEM_INDEX])+"|"
        if num_players == 3:
            spaces = 17
            if i > 0:
                buffer += "      "
            buffer += "| "+str(card_datas[i][POINT_INDEX]) + (" " * spaces) +str(card_datas[i][GEM_INDEX])+"|"
        if num_players == 2:
            spaces = 15
            if i > 0:
                buffer += "                         "
            buffer += "| "+str(card_datas[i][POINT_INDEX]) + (" " * spaces) +str(card_datas[i][GEM_INDEX])+"|"
    return buffer

def noble_row_2(card_datas, num_players):
    buffer = ""
    for i in range(len(card_datas)):
        if num_players == 4:
            if i > 0:
                buffer += "   " 
            buffer += "|        Rank "+str(card_datas[i][RANK_INDEX])+"      |"
        if num_players == 3:
            if i > 0:
                buffer += "      " 
            buffer += "|        Rank "+str(card_datas[i][RANK_INDEX])+"          |"
        if num_players == 2:
            if i > 0:
                buffer += "                         " 
            buffer += "|        Rank "+str(card_datas[i][RANK_INDEX])+"        |"
    return buffer

def noble_row_3(card_datas, num_players):
    buffer = ""
    for i in range(len(card_datas)):
        if num_players == 4:
            if i > 0:
                buffer += "   " 
            buffer += "| "+str(card_datas[i][COST_INDEX][DIAMOND_COST_INDEX])+" Diamond(s)       |"
        if num_players == 3:
            if i > 0:
                buffer += "      " 
            buffer += "| "+str(card_datas[i][COST_INDEX][DIAMOND_COST_INDEX])+" Diamond(s)           |"
        if num_players == 2:
            if i > 0:
                buffer += "                         " 
            buffer += "| "+str(card_datas[i][COST_INDEX][DIAMOND_COST_INDEX])+" Diamond(s)         |"
    return buffer

def noble_row_4(card_datas, num_players):
    buffer  = ""
    for i in range(len(card_datas)):
        if num_players == 4:
            if i > 0:
                buffer += "   " 
            buffer += "| "+str(card_datas[i][COST_INDEX][SAPPHIRE_COST_INDEX])+" Sapphire(s)      |"
        if num_players == 3:
            if i > 0:
                buffer += "      " 
            buffer += "| "+str(card_datas[i][COST_INDEX][SAPPHIRE_COST_INDEX])+" Sapphire(s)          |"
        if num_players == 2:
            if i > 0:
                buffer += "                         " 
            buffer += "| "+str(card_datas[i][COST_INDEX][SAPPHIRE_COST_INDEX])+" Sapphire(s)        |"
    return buffer

def noble_row_5(card_datas, num_players):
    buffer  = ""
    for i in range(len(card_datas)):
        if num_players == 4:
            if i > 0:
                buffer += "   " 
            buffer += "| "+str(card_datas[i][COST_INDEX][EMERALD_COST_INDEX])+" Emerald(s)       |"
        if num_players == 3:
            if i > 0:
                buffer += "      " 
            buffer += "| "+str(card_datas[i][COST_INDEX][EMERALD_COST_INDEX])+" Emerald(s)           |"
        if num_players == 2:
            if i > 0:
                buffer += "                         " 
            buffer += "| "+str(card_datas[i][COST_INDEX][EMERALD_COST_INDEX])+" Emerald(s)         |"
    return buffer

def noble_row_6(card_datas, num_players):
    buffer  = ""
    for i in range(len(card_datas)):
        if num_players == 4:
            if i > 0:
                buffer += "   " 
            buffer += "| "+str(card_datas[i][COST_INDEX][RUBY_COST_INDEX])+" Ruby(s)          |"
        if num_players == 3:
            if i > 0:
                buffer += "      " 
            buffer += "| "+str(card_datas[i][COST_INDEX][RUBY_COST_INDEX])+" Ruby(s)              |"
        if num_players == 2:
            if i > 0:
                buffer += "                         " 
            buffer += "| "+str(card_datas[i][COST_INDEX][RUBY_COST_INDEX])+" Ruby(s)            |"
    return buffer

def noble_row_7(card_datas, num_players):
    buffer  = ""
    for i in range(len(card_datas)):
        if num_players == 4:
            if i > 0:
                buffer += "   " 
            buffer += "| "+str(card_datas[i][COST_INDEX][ONYX_COST_INDEX])+" Onyx(s)          |"
        if num_players == 3:
            if i > 0:
                buffer += "      " 
            buffer += "| "+str(card_datas[i][COST_INDEX][ONYX_COST_INDEX])+" Onyx(s)              |"
        if num_players == 2:
            if i > 0:
                buffer += "                         " 
            buffer += "| "+str(card_datas[i][COST_INDEX][ONYX_COST_INDEX])+" Onyx(s)            |"
    return buffer

DIAMOND_INDEX = 0
SAPPHIRE_INDEX = 1
EMERALD_INDEX = 2
RUBY_INDEX = 3
ONYX_INDEX = 4

def add_chips_to_bank(bank, chip_type, num_chips):
    index = -1
    if chip_type == "diamond":
        index = DIAMOND_INDEX
    elif chip_type == "sapphire":
        index = SAPPHIRE_INDEX
    elif chip_type == "emerald":
        index = EMERALD_INDEX
    elif chip_type == "ruby":
        index = RUBY_INDEX
    elif chip_type == "onyx":
        index = ONYX_INDEX

    chips = 0
    if index >= 0 and index <= ONYX_INDEX:
        chips = num_chips
        if bank[index] >= num_chips:
            bank[index] += chips
            
def remove_chips_from_bank(bank, chip_type, num_chips):
    index = -1
    if chip_type == "diamond":
        index = DIAMOND_INDEX
    elif chip_type == "sapphire":
        index = SAPPHIRE_INDEX
    elif chip_type == "emerald":
        index = EMERALD_INDEX
    elif chip_type == "ruby":
        index = RUBY_INDEX
    elif chip_type == "onyx":
        index = ONYX_INDEX
    
    chips = 0
    if index >= 0 and index <= ONYX_INDEX:
        chips = num_chips
        if bank[index] >= num_chips:
            bank[index] -= chips

    return chips

def initialize_bank(num_diamond, num_sapphire, num_emerald, num_ruby, num_onyx):
    bank = [num_diamond, num_sapphire, num_emerald, num_ruby, num_onyx] 
    return bank

def number_chips_in_bank(bank, chip_type):
    index = -1
    if chip_type == "diamond":
        index = DIAMOND_INDEX
    elif chip_type == "sapphire":
        index = SAPPHIRE_INDEX
    elif chip_type == "emerald":
        index = EMERALD_INDEX
    elif chip_type == "ruby":
        index = RUBY_INDEX
    elif chip_type == "onyx":
        index = ONYX_INDEX
    
    if index >=0 and index <= ONYX_INDEX:
        return bank[index]
    return 0

def bank_header(bank_data):
    buffer = ""
    for i in range(len(bank_data)):
        if i > 0:
            buffer += "        "
        buffer += "┌────────────────┐"
    return buffer

def bank_footer(bank_data):
    buffer = ""
    for i in range(len(bank_data)):
        if i > 0:
            buffer += "        "
        buffer += "└────────────────┘"
    return buffer

def bank_row_1(bank_data):
    buffer = ""
    buffer += "| "+str(bank_data[DIAMOND_INDEX])+" Diamond(s)   |"
    buffer += "        "
    buffer += "| "+str(bank_data[SAPPHIRE_INDEX])+" Sapphire(s)  |"
    buffer += "        "
    buffer += "| "+str(bank_data[EMERALD_INDEX])+" Emerald(s)   |"
    buffer += "        "
    buffer += "| "+str(bank_data[RUBY_INDEX])+" Ruby(s)      |"
    buffer += "        "
    buffer += "| "+str(bank_data[ONYX_INDEX])+" Onyx(s)      |"
    return buffer

    
    


CARD_ONE = 0
CARD_TWO = 1
CARD_THREE = 2
CARD_FOUR = 3

def create_player(name):
    hand = []
    chips = [0, 0, 0, 0, 0]
    wild_chips = 0
    reserved_cards = []
    nobles = []
    return [name, hand, chips, wild_chips, reserved_cards, nobles]

def player_points(player):
    x = 0
    for card in player[1]:
        x += card[POINT_INDEX]
    for card in player[5]:
        x += card[POINT_INDEX]
    return x 

def player_cards(player, card_type):
    x = 0
    for card in player[1]:
        if card[1] == card_type:
            x += 1
    return x

def player_chips(player):
    num_dia = player[2][0]
    num_sap = player[2][1]
    num_emr = player[2][2]
    num_rby = player[2][3]
    num_onx = player[2][4]
    return(num_dia, num_sap, num_emr, num_rby, num_onx)

def purchase_next_available_card(game, player_number):
    cards = game[1][3]
    card_to_buy = -1
    for i in range(len(cards)):
        card = cards[i]
        cost = card_cost_as_list(card)
        if cost[0] <= game[2][player_number-1][2][0] and cost[1] <= game[2][player_number-1][2][1] and cost[2] <= game[2][player_number-1][2][2] and cost[3] <= game[2][player_number-1][2][3] and cost[4] <= game[2][player_number-1][2][4]:
            card_to_buy = i
            break
    
    if card_to_buy >= 0:
        card = cards[card_to_buy]
        cost = card_cost_as_list(card)
        game[1][3].remove(card)
        game[2][player_number-1][1].append(card)
        game[1][3].append(game[0][3][0])
        if cost[0] > 0:
            add_chips_to_bank(game[1][4], "diamond", cost[0])
            game[2][player_number-1][2][0] -= [2][0]
        if cost[1] > 0:
            add_chips_to_bank(game[1][4], "sapphire", cost[1])
            game[2][player_number-1][2][1] -= cost[1]
        if cost[2] > 0:
            add_chips_to_bank(game[1][4], "emerald", cost[2])
            game[2][player_number-1][2][2] -= cost[2]
        if cost[3] > 0:
            add_chips_to_bank(game[1][4], "ruby", cost[3])
            game[2][player_number-1][2][3] -= cost[3]
        if cost[4] > 0:
            add_chips_to_bank(game[1][4], "onyx", cost[4])
            game[2][player_number-1][2][4] -= cost[4]
    


def display_player_hands(players):
    num_players = len(players)
    start_buffer = ""
    in_between_buffer = ""
    p1points = player_points(players[0])
    p2points = player_points(players[1])
    num_dp1 = player_cards(players[0], "diamond")
    num_sp1 = player_cards(players[0], "sapphire")
    num_ep1 = player_cards(players[0], "emerald")
    num_rp1 = player_cards(players[0], "ruby")
    num_op1 = player_cards(players[0], "onyx")
    p1chips = player_chips(players[0])
    p2chips = player_chips(players[1])
    num_dp2 = player_cards(players[1], "diamond")
    num_sp2 = player_cards(players[1], "sapphire")
    num_ep2 = player_cards(players[1], "emerald")
    num_rp2 = player_cards(players[1], "ruby")
    num_op2 = player_cards(players[1], "onyx")
    if num_players == 1:
        start_buffer += "                                                   "
        hand_top =  start_buffer+"┌────────────────────────┐"
        hand_row_1 = start_buffer+"|   "+players[0][0]+" has "+str(p1points)+" points  |"
        hand_row_2 = start_buffer+"|_____Cards_____Chips____|"
        hand_row_3 = start_buffer+"| Dia.| "+str(num_dp1)+"    |    "+str(p1chips[0])+"      |"
        hand_row_4 = start_buffer+"| Sap.| "+str(num_sp1)+"    |    "+str(p1chips[1])+"      |"
        hand_row_5 = start_buffer+"| Emr.| "+str(num_ep1)+"    |    "+str(p1chips[2])+"      |"
        hand_row_6 = start_buffer+"| Rby.| "+str(num_rp1)+"    |    "+str(p1chips[3])+"      |"
        hand_row_7 = start_buffer+"| Onx.| "+str(num_op1)+"    |    "+str(p1chips[4])+"      |"
        hand_bottom = start_buffer+"└────────────────────────┘"
    if num_players == 2:
        start_buffer += "                                "
        in_between_buffer += "      "
        hand_top =  start_buffer+"┌────────────────────────┐"+in_between_buffer+"┌────────────────────────┐"
        hand_row_1 = start_buffer+"|   "+players[0][0]+" has "+str(p1points)+" points  |"+in_between_buffer+"|   "+players[1][0]+" has "+str(p2points)+" points  |"
        hand_row_2 = start_buffer+"|_____Cards_____Chips____|"+in_between_buffer+"|_____Cards_____Chips____|"
        hand_row_3 = start_buffer+"| Dia.| "+str(num_dp1)+"    |    "+str(p1chips[0])+"      |"+in_between_buffer+"| Dia.| "+str(num_dp2)+"    |    "+str(p2chips[0])+"      |"
        hand_row_4 = start_buffer+"| Sap.| "+str(num_sp1)+"    |    "+str(p1chips[1])+"      |"+in_between_buffer+"| Sap.| "+str(num_sp2)+"    |    "+str(p2chips[1])+"      |"
        hand_row_5 = start_buffer+"| Emr.| "+str(num_ep1)+"    |    "+str(p1chips[2])+"      |"+in_between_buffer+"| Emr.| "+str(num_ep2)+"    |    "+str(p2chips[2])+"      |"
        hand_row_6 = start_buffer+"| Rby.| "+str(num_rp1)+"    |    "+str(p1chips[3])+"      |"+in_between_buffer+"| Rby.| "+str(num_rp2)+"    |    "+str(p2chips[3])+"      |"
        hand_row_7 = start_buffer+"| Onx.| "+str(num_op1)+"    |    "+str(p1chips[4])+"      |"+in_between_buffer+"| Onx.| "+str(num_op2)+"    |    "+str(p2chips[4])+"      |"
        hand_bottom = start_buffer+"└────────────────────────┘"+in_between_buffer+"└────────────────────────┘"
    print(hand_top)
    print(hand_row_1)
    print(hand_row_2)
    print(hand_row_3)
    print(hand_row_4)
    print(hand_row_5)
    print(hand_row_6)
    print(hand_row_7)
    print(hand_bottom)

def create_card(rank, gem, points, diamond_cost, sapphire_cost, emerald_cost, ruby_cost, onyx_cost):
    cost_string = str(sapphire_cost) + str(emerald_cost) + str(ruby_cost) + str(onyx_cost) + str(diamond_cost)
    return (rank, gem, points, cost_string)

def card_cost_as_list(card):
    cost = []
    for c in card[3]:
        cost.append(int(c))
    return cost

def start_game(game):
    rank_1_deck = game[0][3]
    rank_2_deck = game[0][2]
    rank_3_deck = game[0][1]
    noble_deck = game[0][0]
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
    rank_2_deck.append(create_card(2, "diamond", 1, 2, 3, 0, 3, 0))
    rank_2_deck.append(create_card(2, "diamond", 1, 0, 0, 3, 2, 2))
    rank_2_deck.append(create_card(2, "diamond", 2, 0, 0, 1, 4, 2))
    rank_2_deck.append(create_card(2, "diamond", 2, 0, 0, 0, 5, 3))
    rank_2_deck.append(create_card(2, "diamond", 2, 0, 0, 0, 5, 0))
    rank_2_deck.append(create_card(2, "diamond", 3, 6, 0, 0, 0, 0))
    rank_2_deck.append(create_card(2, "sapphire", 1, 0, 2, 3, 0, 3))
    rank_2_deck.append(create_card(2, "sapphire", 1, 0, 2, 2, 3, 0))
    rank_2_deck.append(create_card(2, "sapphire", 2, 5, 3, 0, 0, 0))
    rank_2_deck.append(create_card(2, "sapphire", 2, 2, 0, 0, 1, 4))
    rank_2_deck.append(create_card(2, "sapphire", 2, 0, 5, 0, 0, 0))
    rank_2_deck.append(create_card(2, "sapphire", 3, 0, 6, 0, 0, 0))
    rank_2_deck.append(create_card(2, "emerald", 1, 2, 3, 0, 0, 2))
    rank_2_deck.append(create_card(2, "emerald", 1, 3, 0, 2, 3, 0))
    rank_2_deck.append(create_card(2, "emerald", 2, 4, 2, 0, 0, 1))
    rank_2_deck.append(create_card(2, "emerald", 2, 0, 0, 5, 0, 0))
    rank_2_deck.append(create_card(2, "emerald", 2, 0, 5, 3, 0, 0))
    rank_2_deck.append(create_card(2, "emerald", 3, 0, 0, 6, 0, 0))
    rank_2_deck.append(create_card(2, "ruby", 1, 2, 0, 0, 2, 3))
    rank_2_deck.append(create_card(2, "ruby", 1, 0, 3, 0, 2, 3))
    rank_2_deck.append(create_card(2, "ruby", 2, 1, 4, 2, 0, 0))
    rank_2_deck.append(create_card(2, "ruby", 2, 3, 0, 0, 0, 5))
    rank_2_deck.append(create_card(2, "ruby", 2, 0, 0, 0, 0, 5))
    rank_2_deck.append(create_card(2, "ruby", 3, 0, 0, 0, 6, 0))
    rank_2_deck.append(create_card(2, "onyx", 1, 3, 0, 3, 0, 2))
    rank_2_deck.append(create_card(2, "onyx", 1, 3, 2, 2, 0, 0))
    rank_2_deck.append(create_card(2, "onyx", 2, 0, 1, 4, 2, 0))
    rank_2_deck.append(create_card(2, "onyx", 2, 5, 0, 0, 0, 0))
    rank_2_deck.append(create_card(2, "onyx", 2, 0, 0, 5, 3, 0))
    rank_2_deck.append(create_card(2, "onyx", 3, 0, 0, 0, 0, 6))
    rank_3_deck.append(create_card(3, "diamond", 3, 0, 3, 3, 5, 3))
    rank_3_deck.append(create_card(3, "diamond", 4, 3, 0, 0, 3, 6))
    rank_3_deck.append(create_card(3, "diamond", 4, 0, 0, 0, 0, 7))
    rank_3_deck.append(create_card(3, "diamond", 5, 3, 0, 0, 0, 7))
    rank_3_deck.append(create_card(3, "sapphire", 3, 3, 0, 3, 3, 5))
    rank_3_deck.append(create_card(3, "sapphire", 4, 6, 3, 0, 0, 3))
    rank_3_deck.append(create_card(3, "sapphire", 4, 7, 0, 0, 0, 0))
    rank_3_deck.append(create_card(3, "sapphire", 5, 7, 3, 0, 0, 0))
    rank_3_deck.append(create_card(3, "emerald", 3, 5, 3, 0, 3, 3))
    rank_3_deck.append(create_card(3, "emerald", 4, 3, 6, 3, 0, 0))
    rank_3_deck.append(create_card(3, "emerald", 4, 0, 7, 0, 0, 0))
    rank_3_deck.append(create_card(3, "emerald", 5, 0, 7, 3, 0, 0))
    rank_3_deck.append(create_card(3, "ruby", 3, 3, 5, 3, 0, 3))
    rank_3_deck.append(create_card(3, "ruby", 4, 0, 0, 7, 0, 0))
    rank_3_deck.append(create_card(3, "ruby", 4, 0, 3, 6, 3, 0))
    rank_3_deck.append(create_card(3, "ruby", 5, 0, 0, 7, 3, 0))
    rank_3_deck.append(create_card(3, "onyx", 3, 3, 3, 5, 3, 0))
    rank_3_deck.append(create_card(3, "onyx", 4, 0, 0, 0, 7, 0))
    rank_3_deck.append(create_card(3, "onyx", 4, 0, 0, 3, 6, 3))
    rank_3_deck.append(create_card(3, "onyx", 5, 0, 0, 0, 7, 3))
    noble_deck.append(create_card(4, "noble", 3, 3, 0, 0, 3, 3))
    noble_deck.append(create_card(4, "noble", 3, 0, 3, 3, 3, 0))
    noble_deck.append(create_card(4, "noble", 3, 3, 3, 0, 0, 3))
    noble_deck.append(create_card(4, "noble", 3, 0, 0, 3, 3, 3))
    noble_deck.append(create_card(4, "noble", 3, 3, 3, 3, 0, 0))
    noble_deck.append(create_card(4, "noble", 3, 0, 0, 4, 4, 0))
    noble_deck.append(create_card(4, "noble", 3, 4, 0, 0, 0, 4))
    noble_deck.append(create_card(4, "noble", 3, 4, 4, 0, 0, 0))
    noble_deck.append(create_card(4, "noble", 3, 0, 0, 0, 4, 4))
    noble_deck.append(create_card(4, "noble", 3, 0, 4, 4, 0, 0))
    random.shuffle(noble_deck)
    random.shuffle(rank_3_deck)
    random.shuffle(rank_2_deck)
    random.shuffle(rank_1_deck)
    for i in range(len(game[2]) + 1):
        game[1][0].append(noble_deck[i])
    del game[0][0][0]
    del game[0][0][0]
    del game[0][0][0]
    del game[0][0][0]
    game[1][1] = [rank_3_deck[0], rank_3_deck[1], rank_3_deck[2], rank_3_deck[3]]
    del game[0][1][0]
    del game[0][1][0]
    del game[0][1][0]
    del game[0][1][0]
    game[1][2] = [rank_2_deck[0], rank_2_deck[1], rank_2_deck[2], rank_2_deck[3]]
    del game[0][2][0]
    del game[0][2][0]
    del game[0][2][0]
    del game[0][2][0]
    game[1][3] = [rank_1_deck[0], rank_1_deck[1], rank_1_deck[2], rank_1_deck[3]]
    del game[0][3][0]
    del game[0][3][0]
    del game[0][3][0]
    del game[0][3][0]
    game[1][4] = initialize_bank(7, 7, 7, 7, 7)






def print_row(card_datas):
    print(row_header(card_datas))
    print(row_1(card_datas))
    print(row_2(card_datas))
    print(row_3(card_datas))
    print(row_4(card_datas))
    print(row_5(card_datas))
    print(row_6(card_datas))
    print(row_7(card_datas))
    print(row_footer(card_datas))

def print_noble_lines(card_datas, num_players):
    print(noble_header(card_datas, num_players))
    print(noble_row_1(card_datas, num_players))
    print(noble_row_2(card_datas, num_players))
    print(noble_row_3(card_datas, num_players))
    print(noble_row_4(card_datas, num_players))
    print(noble_row_5(card_datas, num_players))
    print(noble_row_6(card_datas, num_players))
    print(noble_row_7(card_datas, num_players))
    print(noble_footer(card_datas, num_players))

def print_bank_lines(bank_data):
    print(bank_header(bank_data))
    print(bank_row_1(bank_data))
    print(bank_footer(bank_data))


def draw_board(game):
    print_noble_lines(game[1][0], len(game[2]))
    print_row(game[1][1])
    print_row(game[1][2])
    print_row(game[1][3])
    print_bank_lines(game[1][4])
    display_player_hands(game[2])

def create_2_player_game(player_1_name, player_2_name):
    noble_deck = []
    rank_3_deck = []
    rank_2_deck = []
    rank_1_deck = []
    nobles_dealt = [] 
    rank_3_cards_dealt = []
    rank_2_cards_dealt = []
    rank_1_cards_dealt = []
    bank = []
    players = []
    players.append(create_player(player_1_name))
    players.append(create_player(player_2_name))
    decks = [noble_deck, rank_3_deck, rank_2_deck, rank_1_deck]
    board = [nobles_dealt, rank_3_cards_dealt, rank_2_cards_dealt, rank_1_cards_dealt, bank]
    game = [decks, board, players]
    return game