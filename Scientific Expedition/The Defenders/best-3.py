class Army:

    def __init__(self):
        self.units = list()

    def add_units(self, unit_type, count):
        for _ in range(count):
            self.units.append(unit_type())

    def __getitem__(self, index):
        return self.units[index]

    def __delitem__(self, index):
        del self.units[index]

    def __str__(self):
        result = str(self.__class__) + "\n"
        result += '\n'.join( [str(unit) for unit in self.units] )
        return result

    def __len__(self):
        return len(self.units)

class Battle:

    def fight(self, army_1, army_2):
        while (len(army_1) and len(army_2)):
            attacker = army_1[0]
            victim = army_2[0]

            if fight(attacker, victim):
                del army_2[0]
            else:
                del army_1[0]

        return len(army_1) > 0

class Warrior:

    def __init__(self):
        self.attack =  5
        self.health = 50

    @property
    def is_alive(self):
        return self.health > 0

    def decrease_health(self, damage):
        self.health -= damage

    def __str__(self):
        return "  {}. Attack: {}. Health: {}.".format(self.__class__, self.attack, self.health)

class Knight(Warrior):

    def __init__(self):
        super().__init__()
        self.attack = 7

class Defender(Warrior):
    
    def __init__(self):
        super().__init__()
        self.attack = 3
        self.health = 60
        self.defense = 2

    def decrease_health(self, damage):
        self.health -= max(damage - self.defense, 0)

def fight(unit_1, unit_2):
    attacker, victim = unit_1, unit_2
    while (attacker.is_alive and victim.is_alive):
        victim.decrease_health(attacker.attack)
        victim, attacker = attacker, victim

    return unit_1.is_alive
