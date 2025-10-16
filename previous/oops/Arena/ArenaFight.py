from Zombie import *

zombie = Zombie('zombie' , 100 , 5)
zombie.talk()
zombie.walk_forward()
zombie.attack()

print(f'{zombie.get_type_of_enemy()}')
