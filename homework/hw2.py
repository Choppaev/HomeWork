# Реализация класса SuperHero
class SuperHero:
    def __init__(self, hp):
        self.hp = hp

    def increase_hp(self):
        self.hp = self.hp ** 2


# Реализация класса AirHero наследника класса SuperHero
class AirHero(SuperHero):
    def __init__(self, hp, damage):
        super().__init__(hp)
        self.damage = damage
        self.fly = False

    def increase_hp(self):
        super().increase_hp()
        self.fly = True

    def fly_in(self, true_phrase):
        if self.fly:
            print(f"Fly in the {true_phrase}")


# Реализация класса EarthHero наследника класса SuperHero
class EarthHero(SuperHero):
    def __init__(self, hp, damage):
        super().__init__(hp)
        self.damage = damage
        self.fly = False

    def increase_hp(self):
        super().increase_hp()
        self.fly = True

    def fly_in(self, true_phrase):
        if self.fly:
            print(f"Fly in the {true_phrase}")


# Реализация класса Villain наследника класса EarthHero
class Villain(EarthHero):
    def __init__(self, hp, damage):
        super().__init__(hp, damage)
        self.people = "monster"

    def gen_x(self):
        pass

    def crit(self, power):
        self.damage = self.damage ** power


# Создание объектов
air_hero = AirHero(100, 10)
earth_hero = EarthHero(200, 20)
villain = Villain(300, 30)

# Вызов новых методов
air_hero.increase_hp()
air_hero.fly_in("sky")
earth_hero.increase_hp()
earth_hero.fly_in("ground")

# Применение метода crit на объекте другого класса
villain.crit(2, air_hero.damage)