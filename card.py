class Card:
    def __init__(self, rank, point_value, gem_type, diamond_cost=0, sapphire_cost=0, emerald_cost=0, ruby_cost=0, onyx_cost=0):
        self.rank = rank
        self.point_value = point_value
        self.gem_type = gem_type
        self.diamond_cost = diamond_cost
        self.sapphire_cost = sapphire_cost
        self.emerald_cost = emerald_cost
        self.ruby_cost = ruby_cost
        self.onyx_cost = onyx_cost

    def set_cost_diamond(self, value):
        self.diamond_cost = value
        return self

    def set_cost_sapphire(self, value):
        self.sapphire_cost = value
        return self

    def set_cost_emerald(self, value):
        self.emerald_cost = value
        return self

    def set_cost_ruby(self, value):
        self.ruby_cost = value
        return self

    def set_cost_onyx(self, value):
        self.onyx_cost = value
        return self

    def cost_diamond(self):
        return self.diamond_cost

    def cost_sapphire(self):
        return self.sapphire_cost

    def cost_emerald(self):
        return self.emerald_cost

    def cost_ruby(self):
        return self.ruby_cost

    def cost_onyx(self):
        return self.onyx_cost

    def get_gem_type(self):
        return self.gem_type

    def get_point_value(self):
        return self.point_value

    def get_rank(self):
        return self.rank

    def number_of_gem_costs(self):
        # TODO
        return 0
