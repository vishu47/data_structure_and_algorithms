class Weapon:
    
    
    def __init__(self ,  type_of_weapon , attack_increase):
        self.attack_increase = attack_increase
        self.__type_of_weapon = type_of_weapon
        
        
    def get_weapon_type(self):
        return self.__type_of_weapon
    
    
