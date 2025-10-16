class Enemy:
    type_of_enemy: str
    enemy_health: int = 10
    enemy_damage = 1

    def __init__(self, type_of_enemy, enemy_health=10, enemy_damage=1):
        ## encapsulation method to make public attribute to private and can
        ## not be changed after class initiated and can not be over ride for setting and getting this value we need separate function we called then setter and getter
        ## now it is private attribute
        self.__type_of_enemy = type_of_enemy

        self.enemy_health = enemy_health
        self.enemy_damage = enemy_damage

    def get_type_of_enemy(self):
        return self.__type_of_enemy


    def talk(self):
        print(f'i am {self.__type_of_enemy}. Be prepared to fight.')

    def walk_forward(self):
        print(f'{self.__type_of_enemy} moving forward with {self.enemy_health}')

    def attack(self):
        print(f'{self.__type_of_enemy} attacking with damage {self.enemy_damage}')
