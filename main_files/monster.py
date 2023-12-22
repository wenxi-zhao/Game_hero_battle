"""
该文件用于实现怪物类
"""

import random

class Monster():
    def __init__(self):
        self.name = None
        self.hp = None
        self.mp = None
        self.atk = None
        self.defense = None
        
        self.skill = None
        
        self.weapon = None
        self.armor = None
        self.shoes = None

class Slime(Monster):
    pass

class Wolf(Monster):
    pass

class Goblin(Monster):
    pass

class Orc(Monster):
    pass

class Dragon(Monster):
    pass

class Demon(Monster):
    pass

class Tentacle(Monster):
    pass

class Burglar(Monster):
    pass

class king(Monster):
    pass