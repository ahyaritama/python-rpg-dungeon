class Skill:
    def __init__(self, _id: int, _type: str, effect: int, min_level: int):
        self.id = _id
        self.type = _type
        self.effect = effect
        self.min_level = min

class SkillNode:
    def __init__(self, data: Skill):
        self.data = data
        self.left: Skill = None
        self.right: Skill = None

class SkillTree:
    def __init__(self):
        self.root = None
