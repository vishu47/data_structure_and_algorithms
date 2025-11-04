from Enemy import *
from Zombie import *
from Orge import *

# zm = Enemy('Zombie' , 100 , 1)
# zm.get_type_of_enemy()
# zm.talk()
# zm.walk_forword()
# zm.attack()

# encapsulation : it can not override the current obj create a new obj at diff location but point to same ver zm
# this is not possible in encap
# zm.get_type_of_enemy()



# polymorphism : means it has many form and it can execute the smlass as object during the runtime.abs

# def battle(e :Enemy):
#     e.talk() 
#     e.attack() 

# zm = Zombie(100 , 1 , True)
# og = Orge(200 , 3 , 30)

# battle(zm)
# battle(og)


# print(f"{zm.get_type_of_enemy()} has {zm.health} points and have damage {zm.enemy_damage}")
# print(f"{og.get_type_of_enemy()} has {og.health} points and have damage {og.enemy_damage}")




# final battle

def FinalBattle(e1 : Enemy , e2 : Enemy):
    
    while e1.health > 0 and e2.health > 0:
        
        print('----------') 
        
        e1.special_attack()  
        e2.special_attack()  
        
        print(f'{e1.get_type_of_enemy()} has {e1.health} HP left')
        print(f'{e2.get_type_of_enemy()} has {e2.health} HP left')
        
        e1.attack()
        e2.health -= e1.enemy_damage
        e2.attack()
        e1.health -= e2.enemy_damage
        
        print('----------') 
        
    if e1.health <= 0:
        print(f'{e2.get_type_of_enemy()} wins')
    else:    
        print(f'{e1.get_type_of_enemy()} wins')
        
            
zm = Zombie(100 , 1 , True)
og = Orge(200 , 2 , 20)       
        
FinalBattle(zm,og)       