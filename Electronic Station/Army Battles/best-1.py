# https://py.checkio.org/mission/army-battles/publications/JimmyCarlos/python-3/army-battles/
class Warrior(object):
    def __init__(self):
        self.health = 50
        self.attack = 5

    @property
    def is_alive(self):
        """Boolean property to test if health is above 0."""
        return self.health > 0


###################################################################################################
###################################################################################################
class Knight(Warrior):
    def __init__(self):
        self.health = 50
        self.attack = 7

    @property
    def is_alive(self):
        """Boolean property to test if health is above 0."""
        return self.health > 0


###################################################################################################
###################################################################################################
class Army(object):
    def __init__(self):
        self.soldiers = []

    def add_units(self,soldierToAdd,soldierToAdd_amount):
        """Adds in a soldier object to the army."""
        if soldierToAdd == Warrior:
            for soldierToAdd_i in range(soldierToAdd_amount):
                self.soldiers.append(Warrior())
        elif soldierToAdd == Knight:
            for soldierToAdd_i in range(soldierToAdd_amount):
                self.soldiers.append(Knight())

    def __len__(self):
        return len(self.soldiers)
        

###################################################################################################
###################################################################################################
class Battle(object):
    def __init__(object):
        pass

    def fight(self,army1,army2):
        """Simulate a battle between two soldiers. Return True if army1 won or False if army2 won."""
        # Use assertion statements to check correct classes were passed in. 
        assert type(army1) == Army
        assert type(army2) == Army
        
        while len(army1) > 0 and len(army2) > 0:
            is_soldier1_won = fight(army1.soldiers[0],army2.soldiers[0])
            if is_soldier1_won:
                army2.soldiers.pop(0)
            else:
                army1.soldiers.pop(0)

        if len(army1) > 0:
            return True
        else:
            return False


###################################################################################################
###################################################################################################
def fight(soldier1,soldier2):
    """Simulate a battle between two soldiers. Return True if soldier1 won or False if soldier2 won."""
    # Use assertion statements to check correct classes were passed in. 
    assert type(soldier1) in {Warrior,Knight}
    assert type(soldier2) in {Warrior,Knight}
    
    warriorNextToAttack = "soldier1"

    roundIndex = 0 

    while True:
        roundIndex += 1
        if warriorNextToAttack == "soldier1":
            damageDealt = soldier1.attack
            soldier2.health -= damageDealt
            warriorNextToAttack = "soldier2"
            if not soldier2.is_alive: return True
        else:
            damageDealt = soldier2.attack
            soldier1.health -= damageDealt
            warriorNextToAttack = "soldier1"
            if not soldier1.is_alive: return False

