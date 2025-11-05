from Enemy import *
import random

class Zombie(Enemy):
    
    
    # this si zombie constructor
    def __init__(self , steps, enemy_damage, health = 10):
        # this is parent constructor 
        # when we implement inhritance we required to add super classes to get all the attr from the parent class
        # assign the properties
        super().__init__(
            type_of_enemy = "Zombie",
            steps = steps,
            enemy_damage = enemy_damage,
            health = health,
        )
         
    def spread(self):
        print(f'it spread the desease.')    
    
    def talk(self):
        print(f'***grumbling***')    
    
    def attack(self):
        print(f'{self.get_type_of_enemy()} attack with {self.enemy_damage}')    
        
        # add special attack
    def special_attack(self):
        did_special_attack_work = random.random() < 0.5
        if did_special_attack_work :
           print(f'Zombie has regenerated health by 2')     
           self.health += 2
        