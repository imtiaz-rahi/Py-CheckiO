class Warrior(object): # Represented in diagrams by single sword
    def __init__(self):
        self.health = 50
        self.attack = 5
        self.defense = 0

    @property
    def is_alive(self):
        """Boolean property to test if health is above 0."""
        return self.health > 0


###################################################################################################
###################################################################################################
class Knight(Warrior): # Represented in diagrams by double swords
    def __init__(self):
        self.health = 50
        self.attack = 7
        self.defense = 0

    @property
    def is_alive(self):
        """Boolean property to test if health is above 0."""
        return self.health > 0


###################################################################################################
###################################################################################################
class Defender(Warrior): # Represented in diagrams by a sword and shield
    def __init__(self):
        self.health = 60
        self.attack = 3
        self.defense = 2

    @property
    def is_alive(self):
        """Boolean property to test if health is above 0."""
        return self.health > 0


###################################################################################################
###################################################################################################
# Ok, so this guy seems to not exist, but instead his class is created when the tester is called.
# I think his health is 50, attack is 1 and defense is 0. However, we cannot define his defense.
##class Rookie(Warrior):
##    pass
    
###################################################################################################
###################################################################################################
class Army(object):
    def __init__(self):
        self.soldiers = []

    def add_units(self,soldierToAdd,soldierToAdd_amount):
        """Adds in a soldier object to the army, a required amount of times."""
        for soldierToAdd_i in range(soldierToAdd_amount):
            self.soldiers.append(soldierToAdd())

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

        # Keep track of how many fights have taken place.
        fightIndex = 0
        
        while len(army1) > 0 and len(army2) > 0:
            # Have a fight between the first soldiers of each army.
            fightIndex += 1
            fight(army1.soldiers[0],army2.soldiers[0])

            # Remove the dead soldier.
            if army1.soldiers[0].is_alive:
                army2.soldiers.pop(0)
            else:
                army1.soldiers.pop(0)

            print(fightIndex)
            print([x.health for x in army1.soldiers])
            print([x.health for x in army2.soldiers])
            print()

        # Has army1 won?
        return len(army1) > 0


###################################################################################################
###################################################################################################
def fight(soldier1,soldier2):
    """Simulate a battle between two soldiers. Return True if soldier1 won or False if soldier2 won."""
    # Remember order of whose turn is next.
    warriorNextToAttack = "soldier1"

    # Keep track of how many rounds of fighting have taken place.
    roundIndex = 0 

    # Main fight loop.
    while True:
        roundIndex += 1
        print(roundIndex,soldier1.health,soldier2.health)

        # Decide who is to attack, and let them have one attack, breaking the loop if the hit is fatal.
        if warriorNextToAttack == "soldier1":
            damageDealt = soldier1.attack
            if type(soldier2) == Defender: damageDealt = max(damageDealt - soldier2.defense, 0)
            soldier2.health -= damageDealt
            warriorNextToAttack = "soldier2"
            if not soldier2.is_alive: return True
        else:
            damageDealt = soldier2.attack
            if type(soldier1) == Defender: damageDealt = max(damageDealt - soldier1.defense, 0)
            soldier1.health -= damageDealt
            warriorNextToAttack = "soldier1"
            if not soldier1.is_alive: return False


###################################################################################################
###################################################################################################
