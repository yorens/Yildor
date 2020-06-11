class Bank:
    def __init__(self, num_diamond, num_sapphire, num_emerald, num_ruby, num_onyx):
        self.num_diamond = num_diamond
        self.num_sapphire = num_sapphire
        self.num_emerald = num_emerald
        self.num_ruby = num_ruby
        self.num_onyx = num_onyx
        self.max_num_diamond = num_diamond
        self.max_num_sapphire = num_sapphire
        self.max_num_emerald = num_emerald
        self.max_num_ruby = num_ruby
        self.max_num_onyx = num_onyx

    def balance(self, type_string):
        if type_string == "emerald":
            return self.num_emerald
        elif type_string == "diamond":
            return self.num_diamond
        elif type_string == "sapphire":
            return self.num_sapphire
        elif type_string == "ruby":
            return self.num_ruby
        elif type_string == "onyx":
            return self.num_onyx

    def withdraw_one_coin(self, type_string):
        if type_string == "emerald":
            self.num_emerald -= 1 
            if self.num_emerald <= 0:
                self.num_emerald = 0
        elif type_string == "diamond":
            self.num_diamond -= 1 
            if self.num_diamond <= 0:
                self.num_diamond = 0
        elif type_string == "sapphire":
            self.num_sapphire -= 1 
            if self.num_sapphire <= 0:
                self.num_sapphire = 0
        elif type_string == "ruby":
            self.num_ruby -= 1 
            if self.num_ruby <= 0:
                self.num_ruby = 0
        elif type_string == "onyx":
            self.num_onyx -= 1 
            if self.num_onyx <= 0:
                self.num_onyx = 0

    def add_chip_to_bank(self, type_string):
        if type_string == "emerald":
            self.num_emerald += 1 
            if self.num_emerald >= self.max_num_emerald:
                self.num_emerald = self.max_num_emerald
        elif type_string == "diamond":
            self.num_diamond += 1 
            if self.num_diamond >= self.max_num_diamond:
                self.num_diamond = self.max_num_diamond
        elif type_string == "sapphire":
            self.num_sapphire += 1 
            if self.num_sapphire >= self.max_num_sapphire:
                self.num_sapphire = self.max_num_sapphire
        elif type_string == "ruby":
            self.num_ruby += 1 
            if self.num_ruby >= self.max_num_ruby:
                self.num_ruby = self.max_num_ruby
        elif type_string == "onyx":
            self.num_onyx += 1 
            if self.num_onyx >= self.max_num_onyx:
                self.num_onyx = self.max_num_onyx