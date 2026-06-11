from ..struct import Player, SkillNode, SkillTree
from ..util import (
    create_header,
    set_player_skills,
    set_player_stats
)

def show_skills(player: Player, skill_tree: SkillTree):
    """Main handler of skill feature. Show all player's
    unlocked skills and its details.
    """
    while True:
        header_len = create_header(player.name, player.money, "SKILLS")
        print("Your Active Skills:\n")
        _show_unlocked_skill(player, skill_tree)
        print("=" * header_len)
        print("[1] Unlock Skill")
        print("[*] Back")
        choice = input("Your Choice: ")
        match choice:
            case "1":
                _select_skill(player, skill_tree)
            case _:
                break


# PRIVATE FUNCTION
def _learn_skill(player: Player, skill_node: SkillNode | None, skill_id: int):
    """Unlock a skill and validate if player is eligible to
    unlock that skill.
    """
    if not skill_node:
        print("Skill not found")
        input("[OK]")
        return
    
    if skill_id == skill_node.data.id:
        if skill_node.data.name in player.skill_set:
            print("You already have this skill")
            input("[OK]")
            return
        
        if (
            player.level < skill_node.data.min_level
            or player.money < skill_node.data.min_level * 50
        ):
            print("You are unqualified to learn\nthis skill.")
            input("[OK]")
            return
        else:
            player.money -= skill_node.data.min_level * 50
            player.skill_set.add(skill_node.data.name)
            set_player_skills(player.name, player.skill_set)
            set_player_stats(player.name, player.get_stats())
            print("You successfully learned this skill.")
            input("[OK]")
            return

    if not skill_node.data.name in player.skill_set:
        print(f"You must learn the {skill_node.data.name} (ID {skill_node.data.id}) first.")
        input("[OK]")
        return

    if skill_id < skill_node.data.id:
        _learn_skill(player, skill_node.left, skill_id)
    else:
        _learn_skill(player, skill_node.right, skill_id)

def _select_skill(player: Player, skill_tree: SkillTree):
    """Handler for select locked skills."""
    while True:
        header_len = create_header(player.name, player.money, "SKILLS")
        is_available = _show_locked_skill(player, skill_tree)
        print("=" * header_len)

        if is_available:
            print("[*] Back")
            try:
                choice = int(input("Your Choice (Skill ID): "))
            except ValueError:
                return
            _learn_skill(player, skill_tree.root, choice)
        else:
            input("[Back]")
            break

def _show_locked_skill(player: Player, skill_tree: SkillTree) -> bool:
    """Show all of player's locked skills"""
    skill_list = skill_tree.in_order()
    if len(player.skill_set) == len(skill_list):
        print("You have unlocked all skills")
        return False

    print("-" * 32)
    for data in skill_list:
        if not data.name in player.skill_set:
            print(f"| Name   : {data.name:<19} |")
            print(f"| ID     : {data.id:<19} |")
            print(f"| Type   : {data.type:<19} |")
            print(f"| Effect :", end=" ")
            match data.name:
                case "Evil Eye":
                    print(f"{'HP +50% of damage':<19} |")
                case "Baraju Spinner":
                    print(f"{'ATK +45 and HP -15':<19} |")
                case "Raven Chaser":
                    print(f"{'HP +50% of lost HP':<19} |")
                case _:
                    print(f"{data.type + " +" + str(data.effect):<19} |")
            print(f"| Level  : {data.min_level:<19} |")
            print(f"| Price  : {data.min_level * 50:<19} |")
            print("-" * 32)
    return True

def _show_unlocked_skill(player: Player, skill_tree: SkillTree):
    """Show all of player's unlocked skills"""
    if len(player.skill_set) <= 0:
        print("You haven't unlocked any skills")
        return

    skill_list = skill_tree.in_order()
    print("-" * 32)
    for data in skill_list:
        if data.name in player.skill_set:
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