from Zombie import * 
from Hero import * 
from Orge import * 


def HeroBattle(hero: Hero , enemy: Enemy):
    

    hero.talk()
    enemy.talk()

    
    while hero.health > 0 and enemy.health > 0:
        print(f'---------')
        enemy.special_attack()
        
        print(f'{enemy.get_type_of_enemy()} has {enemy.health} HP left')
        print(f'{hero.get_type_hero()} has {hero.health} HP left')
       
        enemy.attack()
        hero.health -= enemy.enemy_damage
        
        hero.attack()
        enemy.health -= hero.enemy_damage
        print(f'---------')


    if hero.health > 0:
        print(f'Hero Wins') 
    else:
        print(f'{enemy.get_type_of_enemy()} Wins') 
    


zm = Zombie(100,1)
og = Orge(100, 1)
hr = Hero(100 , 1)
weapon = Weapon('hammer' , 4)
weapon.get_weapon_type()

hr.weapon = weapon
hr.assign_weapon()

HeroBattle(hr , zm)
