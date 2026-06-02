from ..struct import (
    Skill,
    SkillTree
)

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