import math
import logging


class MenuChoiceInput:
    # MenuChoiceInput creats a menu with choices.
    # Each choice is represented by a MenuItem

    def __init__(self, title, prompt):
        self.title = title
        self.prompt = prompt
        self.choice_as_int = 0
        self.menu_items = []

    def add_menu_item(self, menu_item):
        self.menu_items.append(menu_item)

    def get_choice(self):
        return self.choice_as_int

    def get_menu_choice(self):
        return self.menu_items[self.choice_as_int-1]

    def display(self):
        self.choice_as_int = 0
        total_padding_amount = 0
        padding_amount = 0
        # count up all the menu items to see how many
        # columns we need to build
        # each number takes four spaces (xx)
        # ( 1) Choose
        # (10) Choose
        number_columns = 3
        if len(self.menu_items) < 3:
            number_columns = 2

        # calculate the max size string in any menu item
        max_string_size = 0
        for m in self.menu_items:
            if len(m.prompt) > max_string_size:
                max_string_size = len(m.prompt)

        total_space_for_prompts = number_columns * max_string_size
        total_padding_amount = 75 - total_space_for_prompts
        padding_amount = math.floor(total_padding_amount/number_columns)
        total_column_width = max_string_size + 4 + padding_amount
        logging.debug("total_space_for_prompts: " +
                      str(total_space_for_prompts))
        logging.debug("total_padding_amount: " + str(total_padding_amount))
        logging.debug("padding_amount: " + str(padding_amount))
        logging.debug("total_column_width: " + str(total_column_width))
        logging.debug("padding: " + str(padding_amount))

        menu_index = 0
        menu_buffer = ""
        if self.title != "":
            menu_buffer = self.title + "\n"
        for m in self.menu_items:
            column = menu_index % number_columns
            display_menu_index = " " + str(menu_index+1)
            if menu_index == 9:
                display_menu_index = 10
            menu_buffer += "(" + str(display_menu_index) + ") " + m.prompt
            if column != number_columns-1:
                local_pad = total_column_width - len(m.prompt) - 4
                menu_buffer += (" " * local_pad)
            if column == number_columns-1:
                menu_buffer += "\n"
            menu_index += 1
        if menu_buffer != "":
            print(menu_buffer)
        valid_choice = False
        while not valid_choice:
            choice_as_string = input(self.prompt)
            if choice_as_string != "":
                try:
                    self.choice_as_int = int(choice_as_string)
                    if self.choice_as_int >= 1 and self.choice_as_int <= len(self.menu_items):
                        valid_choice = True
                except ValueError:
                    valid_choice = False
            if not valid_choice:
                print("Sorry, please try again.")
        return self


class MenuItem:
    # MenuItem creates a single choice in a MenuChoiceInput

    def __init__(self, prompt, function, index):
        self.prompt = prompt
        self.function = function
        self.index = index


class MenuStringInput:
    # MenuStringInput creats a menu that accepts string data only.

    def __init__(self, title, prompt):
        self.title = title
        self.prompt = prompt
        self.choice_as_string = ""

    def display(self):
        self.choice_as_string = ""
        if self.title != "":
            print(self.title + "\n")

        valid_choice = False
        while not valid_choice:
            self.choice_as_string = input(self.prompt).strip()
            if self.choice_as_string != "":
                valid_choice = True

            if not valid_choice:
                print("Sorry, please try again.")
        return self

    def get_choice(self):
        return self.choice_as_string


class MenuIntegerInput:
    # MenuStringInput creats a menu that accepts raw integer data only.

    def __init__(self, title, prompt):
        self.title = title
        self.prompt = prompt
        self.choice_as_int = 0

    def display(self):
        self.choice_as_int = 0
        if self.title != "":
            print(self.title + "\n")

        valid_choice = False
        while not valid_choice:
            choice_as_string = input(self.prompt).strip()
            if choice_as_string != "":
                try:
                    self.choice_as_int = int(choice_as_string)
                    valid_choice = True
                except ValueError:
                    valid_choice = False

            if not valid_choice:
                print("Sorry, please try again.")
        return self

    def get_choice(self):
        return self.choice_as_int


if __name__ == '__main__':
    # logging.basicConfig(filename='tmp/yildor.log',
    #                     format='%(asctime)s [%(levelname)s] %(filename)s:%(lineno)d %(message)s',
    #                     level=logging.DEBUG)
    menu1 = MenuChoiceInput("Do you want to...",
                            "Enter the number of your choice: ")
    menu1.add_menu_item(MenuItem("Choose chips", "c1", 1))
    menu1.add_menu_item(MenuItem("Choose card", "c2", 2))
    menu1.add_menu_item(MenuItem("Pay for reserved card", "c3", 3))
    menu1.display()
    print("you chose: " + str(menu1.get_choice()))
    menu2 = MenuChoiceInput(
        "Choose chips", "Enter the number of your choice: ")
    menu2.add_menu_item(MenuItem("Choose 2 diamonds", "c1", 1))
    menu2.add_menu_item(MenuItem("Choose 2 sapphires", "c2", 2))
    menu2.add_menu_item(MenuItem("Choose 2 emeralds", "c3", 3))
    menu2.add_menu_item(MenuItem("Choose 2 rubies", "c4", 4))
    menu2.add_menu_item(MenuItem("Choose 2 onyx", "c5", 5))
    menu2.add_menu_item(MenuItem("Choose 1 diamond", "c6", 6))
    menu2.add_menu_item(MenuItem("Choose 1 sapphire", "c7", 7))
    menu2.add_menu_item(MenuItem("Choose 1 emerald", "c8", 8))
    menu2.add_menu_item(MenuItem("Choose 1 ruby", "c9", 9))
    menu2.add_menu_item(MenuItem("Choose 1 onyx", "c10", 10))
    menu2.display()
    print("you chose: " + str(menu2.get_choice()))
    print("you chose: " + str(menu2.get_menu_choice().function))
    print("you chose: " + str(menu2.get_menu_choice().prompt))
    menu3 = MenuIntegerInput(
        "", "How many players are playing (please enter a number)? ")
    menu3.display()
    x = menu3.get_choice()
    list_of_players = []
    for i in range(x):
        player_menu = MenuStringInput("", "Enter the name for player " +
                                      str(i + 1) + ": ").display()
        name = player_menu.get_choice()
        list_of_players.append(name)
    print(list_of_players)
