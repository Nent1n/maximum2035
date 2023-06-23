
import random

class Tank:
    def __init__(self, model, health, armor, min_damage, max_damage):
        self.model = model
        self.health = health
        self.armor = armor
        self.damage = random.randint(min_damage, max_damage)

    def print_info(self):
        print(self.model, 'имеет', self.health, 'hp и', self.damage, 'урона')

    def health_down(self, enemy_damage):
        self.health -= enemy_damage
        print()
        print(self.model)
        print('По нам попали! У нас осталось', self.health, 'hp')

    def shot(self, enemy):
        if enemy.health <= 0 or self.damage >= enemy.health :
            enemy.health = 0
            print(enemy.model, 'уничтожен')
        else:
            print()
            print(self.model)
            print('Есть пробитие! По', enemy.model, 'нанесено', self.damage, 'hp')
            enemy.health_down(self.damage)

class SuperTank(Tank):
    def __init__(self, model, health, armor, min_damage, max_damage, forceArmor):
        super().__init__(model, health, armor, min_damage, max_damage)
        self.forceArmor = forceArmor

    def health_down(self, enemy_damage):
        super().health_down(enemy_damage//2)


tank1 = Tank('t-34', 100, 50, 10, 60)
tank2 = Tank('Maus', 50, 10, 5, 50)
sTank = SuperTank('BABAHA', 1000, 300, 50, 90, True)

sTank.print_info()
tank1.print_info()
tank2.print_info()

tank1.shot(sTank)

