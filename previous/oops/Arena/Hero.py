from Weapon import *


class Hero:
    
    def __init__(self ,steps, enemy_damage, health = 10):
        self.enemy_damage  = enemy_damage
        self.health = health
        self.__type_of_hero = "Thor"
        self.weapon : Weapon = None
        self.has_weapon  = False
        
        
        
    def get_type_hero (self) : 
        return self.__type_of_hero
    
    def assign_weapon(self):
        
        
        print(f'{self.weapon , self.has_weapon  ,self.enemy_damage , self.weapon.attack_increase} pooooooo')
        if self.weapon is not None and not self.has_weapon:
            
            # heare i am using compositon of the classes means we can use anothe class inside in one class as an atrribute it is called composition
            self.enemy_damage += self.weapon.attack_increase
            self.has_weapon = True
            
            
    def talk(self):
        print(f'I am {self.__type_of_hero}')
    
    def attack(self):
        print(f'I am {self.__type_of_hero} attacks for {self.enemy_damage}')