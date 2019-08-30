# https://py.checkio.org/mission/the-defenders/publications/Oksana_Antropova/python-3/improved-with-best-ideas-from-top-solutions/
class Warrior:
    def __init__(self, health = 50, attack = 5):
        self.health = health
        self.attack = attack
    
    @property
    def is_alive(self):
        return self.health > 0
        
    def loose_health(self, damage):
        self.health -= damage 
        
    def hit(self, victim):
        victim.loose_health(self.attack)

class Knight(Warrior):
    def __init__(self):
        Warrior.__init__(self, attack = 7)
        
class Defender(Warrior):
    def __init__(self):
        Warrior.__init__(self, health = 60, attack = 3)
        self.defense = 2
        
    def loose_health(self, damage):
        Warrior.loose_health(self, max(damage - self.defense, 0)) 

def fight(unit_1, unit_2):
    bully, victim = unit_1, unit_2
    while True:
        bully.hit(victim)
        if not victim.is_alive:
            break
        bully, victim = victim, bully
    return unit_1.is_alive
    
class Army(list):
    def add_units(self, typ, number):
        for i in range(number):
            self.append(typ())
            
    def get_next(self):
        for unit in self:
            if unit.is_alive:
                return unit
        return None
        
    @property
    def has_alive_units(self):
        return bool(self.get_next())
            
class Battle:
    def fight(self, army1, army2):
        while army1.has_alive_units and army2.has_alive_units:
            fight(army1.get_next(), army2.get_next())
        return army1.has_alive_units

