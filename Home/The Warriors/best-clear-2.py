# https://py.checkio.org/mission/the-warriors/publications/przemyslaw.daniel/python-3/29-liner-no-looping-with-property/share/878831828a2bb732be602f39101723bb/#comment-63738
from random import randint


class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5

    @property
    def is_alive(self):
        return self.health > 0


class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7


def my_fight(unit_1, unit_2):
    my_steps_to_die = -(-unit_1.health // unit_2.attack)
    enemy_steps_to_die = -(-unit_2.health // unit_1.attack)

    print("my_steps_to_die=", my_steps_to_die, "enemy_steps_to_die=", enemy_steps_to_die)
    steps = min(my_steps_to_die, enemy_steps_to_die)
    print("steps=", steps)
    if my_steps_to_die >= enemy_steps_to_die:
        unit_1.health -= (steps-1)*unit_2.attack
        unit_2.health = 0
        print("WIN #1")
        return True

    unit_2.health -= steps*unit_1.attack
    unit_1.health = 0
    print("WIN #2")
    return False


def correct_fight2(unit_1, unit_2):
    while unit_1.is_alive and unit_2.is_alive:
        unit_2.health -= unit_1.attack
        if unit_2.is_alive:
            unit_1.health -= unit_2.attack
    unit_1.health = max(0, unit_1.health)
    unit_2.health = max(0, unit_2.health)
    return unit_1.is_alive


for i in range(100000):
    print("iteration=", i)

    quarkov_1, daniel_1 = Warrior(), Knight()
    quarkov_1.attack = randint(1, 10)
    quarkov_1.health = randint(50, 100)
    daniel_1.attack = randint(1, 10)
    daniel_1.health = randint(50, 100)

    quarkov_2, daniel_2 = Warrior(), Knight()
    quarkov_2.attack = quarkov_1.attack
    quarkov_2.health = quarkov_1.health
    daniel_2.attack = daniel_1.attack
    daniel_2.health = daniel_1.health

    print("quarkov_1=", vars(quarkov_1), "daniel_1=", vars(daniel_1))
    print("quarkov_2=", vars(quarkov_2), "daniel_2=", vars(daniel_2))

    result_1 = my_fight(quarkov_1, daniel_1)
    result_2 = correct_fight2(quarkov_2, daniel_2)
    print(result_1, result_2)

    print("my      solution=", quarkov_1.health, daniel_1.health)
    print("correct solution=", quarkov_2.health, daniel_2.health)

    assert quarkov_1.health == quarkov_2.health, "NHS sucks"
    assert daniel_1.health == daniel_2.health, "NHS sucks also here"
    print()
