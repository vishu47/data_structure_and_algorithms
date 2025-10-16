from Enemy import *


class Zombie(Enemy):

    def __init__(self, type_of_enemy, enemy_health, enemy_damage):
        # super means it will have all the attribute of parent class and initiate
        super().__init__(
            type_of_enemy=type_of_enemy,
            enemy_health=enemy_health,
            enemy_damage=enemy_damage
        )

    # all the method available in enemy will be available for this class  also