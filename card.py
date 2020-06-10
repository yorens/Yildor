class Card:
    def __init__(self, rank, point_value, gem_type, diamond_cost, sapphire_cost, emerald_cost, ruby_cost, onyx_cost):
        self.rank = rank
        self.point_value = point_value
        self.gem_type = gem_type
        cost_string = str(diamond_cost) + str(sapphire_cost) + str(emerald_cost) + str(ruby_cost) + str(onyx_cost)
        self.cost_string = cost_string