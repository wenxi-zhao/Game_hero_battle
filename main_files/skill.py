"""
该文件用于设计技能类。
"""

class Skill:
    """
    基础技能，用于定义技能的基本属性。
    """
    def __init__(self, name, damage, cost, effect):
        self.name = name
        self.damage = damage
        self.cost = cost
        self.effect = effect

class Skill_fire(Skill):
    """火球术，造成伤害，并添加灼烧效果，造成持续伤害。

    Args:
        Skill (_type_): _description_
    """
    pass

class Skill_ice(Skill):
    """冰冻术，造成伤害，并添加冰冻效果，限制对手行动。

    Args:
        Skill (_type_): _description_
    """
    pass

class Skill_thunder(Skill):
    """闪电术，造成伤害，并添加麻痹效果，降低对手防御力。

    Args:
        Skill (_type_): _description_
    """
    pass

class Skill_wind(Skill):
    """风刃术，造成伤害，并添加击退效果，降低对手攻击力。

    Args:
        Skill (_type_): _description_
    """
    pass

class Skill_earth(Skill):
    """土墙术，造成伤害，并添加守护效果，提高自身防御力。

    Args:
        Skill (_type_): _description_
    """
    pass

class Skill_water(Skill):
    """水波术，造成伤害，并添加愈合效果，恢复自身生命值。

    Args:
        Skill (_type_): _description_
    """
    pass

class Skill_light(Skill):
    """圣光术，造成伤害，并添加净化效果，解除自身异常状态，可以在异常状态中使用。

    Args:
        Skill (_type_): _description_
    """
    pass

class Skill_dark(Skill):
    """暗影术，添加诅咒效果，降低对手攻击力和防御力。

    Args:
        Skill (_type_): _description_
    """
    pass

class Skill_poison(Skill):
    """毒液术，添加腐蚀效果，在数回合内使对手的装备效果失效。

    Args:
        Skill (_type_): _description_
    """
    pass

class Skill_cure(Skill):
    """治愈术，大幅恢复自身生命值。

    Args:
        Skill (_type_): _description_
    """
    pass

class Skill_stamina(Skill):
    """蓄力，提高自身攻击力，持续数回合，并在接下来的一回合内提升防御力。

    Args:
        Skill (_type_): _description_
    """
    pass

class Skill_restore_manapoint(Skill):
    """聚气术，大幅恢复自身魔法值。

    Args:
        Skill (_type_): _description_
    """
    pass