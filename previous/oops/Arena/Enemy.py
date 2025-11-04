class Enemy:
    
    def __init__(self, type_of_enemy,steps, enemy_damage, health = 10):
        self.steps = steps 
        self.__type_of_enemy = type_of_enemy 
        self.health = health 
        self.enemy_damage = enemy_damage 
    
    def get_type_of_enemy(self):
        return self.__type_of_enemy
    
    def talk(self):
        print(f'I {self.__type_of_enemy}. Be prepared to fight')

    def walk_forword(self):
        print(f'{self.__type_of_enemy} moves {self.steps} towords you with {self.health}')
        
    def attack(self):
        print(f'{self.__type_of_enemy} attack with {self.enemy_damage}')
        
        
    def special_attack(self):
        print(f'Not have special attack')