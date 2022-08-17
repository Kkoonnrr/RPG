

class Weapon:
    def __init__(self, weapon_type="", name="", modifier=None, damage=0, strength_needed=0, accuracy=0, weapon_range=0,
                 penetration=0):
        if modifier is None:
            modifier = []
        self.weapon_type = weapon_type
        self.penetration = penetration
        self.weapon_range = weapon_range
        self.accuracy = accuracy
        self.strength_needed = strength_needed
        self.damage = damage
        self.modifier = modifier
        self.name = name


class Łuk(Weapon):
    def __init__(self, weapon_type="", name="", modifier=None, damage=0, strength_needed=0, accuracy=0, weapon_range=0,
                 penetration=0):
        super().__init__(weapon_type, name, modifier, damage, strength_needed, accuracy, weapon_range, penetration)
        if modifier is None:
            modifier = []


class Ammunicja(Weapon):
    def __init__(self, weapon_type="", name="", modifier=None, damage=0, strength_needed=0, accuracy=0, weapon_range=0,
                 penetration=0):
        super().__init__(weapon_type, name, modifier, damage, strength_needed, accuracy, weapon_range, penetration)
        if modifier is None:
            modifier = []
