type SkillList = list[Skill]

class Skill:
    def __init__(self, _id: int, name: str, _type: str, effect: int, min_level: int):
        self.id = _id
        self.name = name
        self.type = _type
        self.effect = effect
        self.min_level = min_level

class SkillNode:
    def __init__(self, data: Skill):
        self.data = data
        self.left: SkillNode | None = None
        self.right: SkillNode | None = None

class SkillTree:
    def __init__(self):
        self.root: SkillNode | None = None
        
    def insert(self, data: Skill):
        new_node = SkillNode(data)

        if self.root is None:
            self.root = new_node
            return
        
        current = self.root
        while True:
            if data.id < current.data.id:
                if current.left is None:
                    current.left = new_node
                    break
                current = current.left
            elif data.id > current.data.id:
                if current.right is None:
                    current.right = new_node
                    break
                current = current.right
            else:
                break
    
    def in_order(self) -> list:
        result_list = []
        self._in_order_recursive(self.root, result_list)
        return result_list
    
    def _in_order_recursive(self, current: SkillNode | None, result_list: list):
        if current is not None:
            self._in_order_recursive(current.left, result_list)
            result_list.append(current.data)
            self._in_order_recursive(current.right, result_list)


def build_skill() -> SkillTree:
    skill_tree = SkillTree()
    skill_tree.insert(Skill(4, "Cyclone Drill", "ATK", 5, 1))

    skill_tree.insert(Skill(2, "Fire And Ice Blast", "ATK", 15, 3))
    skill_tree.insert(Skill(6, "Good Striker", "HP", 35, 3))

    skill_tree.insert(Skill(1, "Victory Striker", "ATK", 20, 4))
    skill_tree.insert(Skill(5, "Evil Eye", "HP", 50, 4))

    skill_tree.insert(Skill(3, "Baraju Spinner", "ATK", 45, 5))
    skill_tree.insert(Skill(7, "Raven Chaser", "HP", 50, 5))
    
    return skill_tree