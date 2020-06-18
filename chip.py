import yildor

class Chip:
    def __init__(self, gem_type):
        self.gem_type = gem_type

def create_diamond():
    return Chip(yildor.diamond)

def create_sapphire():
    return Chip(yildor.sapphire)

def create_emerald():
    return Chip(yildor.emerald)

def create_ruby():
    return Chip(yildor.ruby)

def create_onyx():
    return Chip(yildor.onyx)