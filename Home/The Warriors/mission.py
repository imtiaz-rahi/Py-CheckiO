
class Warrior:
    is_alive = True

    def __init__(self, health=50, attack =5):
        self.health = health
        self.attack = attack

    def take_hit(self, other):
        self.health -= other.attack
        self.is_alive = self.health > 0

    def __str__(self):
        return "H: " + str(self.health) + "; A: " + str(self.attack)


class Knight(Warrior):
    def __init__(self):
        super().__init__(50, 7)


def fight(unit_1, unit_2):
    while unit_1.is_alive and unit_2.is_alive:
        unit_2.take_hit(unit_1)
        if unit_1.is_alive and not unit_2.is_alive:
            return True
        unit_1.take_hit(unit_2)
        if unit_1.is_alive and not unit_2.is_alive:
            return True
    return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    print("Coding complete? Let's try tests!")
