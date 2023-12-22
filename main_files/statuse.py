"""
该文件用于设计状态类。
"""

class Statuse:
    """游戏角色受技能影响后的状态，灼烧、冰冻、麻痹、击退、守护、愈合、诅咒、腐蚀、蓄力
    """
    def __init__(self):
        self.burn = None
        self.freeze = None
        self.paralysis = None
        self.repel = None
        self.guard = None
        self.heal = None
        self.curse = None
        self.corrosion = None
        self.charge = None
