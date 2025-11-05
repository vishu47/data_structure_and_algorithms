from Enemy import *
import random

class Orge(Enemy):
    
    
    # this si zombie constructor
    def __init__(self , steps, enemy_damage , health = 10):
        # this is parent constructor 
        # when we implement inhritance we required to add super classes to get all the attr from the parent class
        # assign the properties
        super().__init__(
            type_of_enemy = "Orge",
            steps = steps,
            enemy_damage = enemy_damage,
            health = health,
        )
        
    def talk(self):
        print(f'***i will eat you***')    
    
    def move(self):
        print(f'i will move towords you with {self.steps} steps')    
    
    def attack(self):
        print(f'{self.get_type_of_enemy()} attack with {self.enemy_damage}')    
        
        
    # add special attack
    def special_attack(self):
        did_special_attack_work = random.random() < 0.2
        if did_special_attack_work :
           self.enemy_damage += 4
           print(f'orge attack has increaseed by 4') 