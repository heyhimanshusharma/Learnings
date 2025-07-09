class Monster:
    # attributes
    health = 100
    energy = 78

    # methods
    def attack(self, amount):
        print("The monster has attacked")
        print(f"{amount} damage was dealt")
        monster.energy -= 20
        print(monster.energy)

    # method 2
    def move(mself, speed):
        print("Monster has moved")
        print(f'It has a speed of {speed}')


monster = Monster()
monster.attack(40)
monster.move(90)