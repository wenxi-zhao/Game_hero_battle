"""
该文件用于设计游戏角色的初始模板。
"""

import random

class Hero():
    def __init__(self):
        self.name = None
        self.hp = None
        self.mp = None
        self.atk = None
        self.defense = None
        
        self.level = None
        self.exp = None
        self.growth_preference = None
        
        self.skill = None
        
        self.money = None
        self.bag = None
        
        self.weapon = None
        self.armor = None
        self.shoes = None


class Soldier(Hero):
    pass

class Mage(Hero):
    pass

class Gruard(Hero):
    pass

