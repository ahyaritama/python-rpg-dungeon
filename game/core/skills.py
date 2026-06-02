from ..struct import (
    Player,
    SkillNode,
    SkillTree,
)
from ..util import clear_screen

def show_skills(player: Player, skill_tree: SkillTree):
    while True:
        clear_screen()
        header = "=" * 12 + " SKILLS " + "=" * 12

        print(f"{'Name    '}: {player.name}")
        print(f"{'Balance '}: {player.money}")
        print(header)

        print("Your Active Skills:\n")
        _show_unlocked_skill(player.skills, skill_tree)
        print("=" * len(header))

        input("[Back]")
        break



# PRIVATE FUNCTION
def _show_unlocked_skill(skill_set: set[str], skill_tree: SkillTree):
    if len(skill_set) <= 0:
        print("You haven't unlocked any skills yet")
        return

    skill_list = skill_tree.in_order()

    print("-" * 32)
    for data in skill_list:
        if data.name in skill_set:
            print(f"| {'Name  '}: {data.name:<20} |")
            print(f"| {'ID    '}: {data.id:<20} |")
            print(f"| {'Type  '}: {data.type:<20} |")
            print(f"| {'Effect'}:", end=" ")

            match data.name:
                case "Evil Eye":
                    print(f"{'HP +50% of damage':<20} |")
                case "Baraju Spinner":
                    print(f"{'ATK +45 and HP -15':<20} |")
                case "Raven Chaser":
                    print(f"{'HP +50% of lost HP':<20} |")
                case _:
                    print(f"{data.type + " +" + str(data.effect):<20} |")
            
            print("-" * 32)