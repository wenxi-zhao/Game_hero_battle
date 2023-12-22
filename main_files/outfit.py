"""
该文件用于设计游戏角色的装备。
"""

class Outfit:
    """
    该类用于设计游戏角色的装备。
    """
    def __init__(self, name, attack, defense, health, magic):
        """
        该方法用于初始化装备的属性。
        :param name: 装备的名称。
        :param attack: 装备的攻击力。
        :param defense: 装备的防御力。
        :param health: 装备的生命值。
        :param magic: 装备的魔法值。
        """
        self.name = name
        self.attack = attack
        self.defense = defense
        self.health = health
        self.magic = magic

    def __str__(self):
        """
        该方法用于打印装备的属性。
        :return: 装备的属性。
        """
        return f"装备名称：{self.name}\n" \
               f"装备攻击力：{self.attack}\n" \
               f"装备防御力：{self.defense}\n" \
               f"装备生命值：{self.health}\n" \
               f"装备魔法值：{self.magic}\n"

class Weapon(Outfit):
    """
    该类用于设计游戏角色的武器。
    """
    pass

class Armor(Outfit):
    """
    该类用于设计游戏角色的防具。
    """
    pass

class Shoes(Outfit):
    """
    该类用于设计游戏角色的鞋子。
    """
    pass
