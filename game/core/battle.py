# from ..struct import Battle, Monster, Player, Room, Skill
# from ..util import clear_screen, create_header, set_player_stats

from ..struct import Battle, Monster, Player, Skill
from ..struct.skill import SkillList
from ..util import create_header, set_player_stats

def start_battle(player: Player, monster: Monster, skill_list: SkillList) -> bool:
    battle = Battle()
    battle.add_char(player)
    battle.add_char(monster)

    result = False
    current_turn = battle.head
    while current_turn and battle.total_char > 1:
        header_len = create_header(player.name, player.money, "BATTLE")
        _show_stats(player, monster)
        print("=" * header_len)
        if current_turn and current_turn.char == player:
            if battle.cooldown > 0:
                battle.cooldown -= 1

            print("[1] Use Skill")
            print("[*] Attack")
            choice = input("Your Choice: ")

            is_dead = False
            match choice:
                case "1":
                    is_dead = _use_skill(player, monster, skill_list, battle)
                case _:
                    is_dead = _player_attack_action(player, monster)
            if is_dead:
                battle.remove_char(monster)
                result = True
        else:
            is_dead = _monster_attack_action(monster, player)
            if is_dead:
                battle.remove_char(player)
            
        input("[OK]")
        current_turn = current_turn.next
    monster.reset()
    return result

# PRIVATE FUNCTION
def _monster_attack_action(monster: Monster, player: Player):
    defence = player.stats["DEF"] + player.equipment.get_total_defence()
    damage = max(0, monster.stats["ATK"] - defence)

    player.stats["HP"] -= damage
    set_player_stats(player.name, player.get_stats())
    print(f"{monster.name} deal {damage} damage to you.")

    if not player.is_alive():
        print("You died.")
        player.reset()
        return True


def _player_attack_action(player: Player, monster: Monster, bonus: int = 0):
    attack = player.stats["ATK"] + player.equipment.get_total_attack() + bonus
    damage = max(0, attack - monster.stats["DEF"])

    monster.stats["HP"] -= damage
    print(f"You deal {damage} damage to {monster.name}.")

    if not monster.is_alive():
        player.exp += monster.exp_drop
        player.money += monster.coin_drop

        print("\nYou successfully defeated")
        print(f"{monster.name}. You received")
        print(f"{monster.exp_drop} exp and {monster.coin_drop} coins.")

        player.check_level_up()
        set_player_stats(player.name, player.get_stats())
        return True
    
    return False

def _show_stats(player: Player, monster: Monster):
    print(f"Name   : {player.name}")
    print(f"Health : {player.stats["HP"]}")
    print(f"ATK    : {player.stats["ATK"]} (+{player.equipment.get_total_attack()})")
    print(f"DEF    : {player.stats["DEF"]} (+{player.equipment.get_total_defence()})")

    print(f"{'VS':^32}")

    print(f"Name   : {monster.name}")
    print(f"Health : {monster.stats["HP"]}")
    print(f"ATK    : {monster.stats["ATK"]}")
    print(f"DEF    : {monster.stats["DEF"]}")

def _skill_handler(player: Player, monster: Monster, skill: Skill) -> tuple[bool, int]:
    bonus = 0
    match skill.name:
        case "Baraju Spinner":
            if player.stats["HP"] <= 15:
                print("Not have enough HP.")
                input("[OK]")
                return False, 0
            player.stats["HP"] -= 15
            bonus += skill.effect
            print(f"Using {skill.name} buff:")
            print(f"    - {skill.type} +{skill.effect}")
            print("    - HP -15")

        case "Evil Eye":
            attack = player.stats["ATK"] + player.equipment.get_total_attack()
            damage = max(0, attack - monster.stats["DEF"])
            bonus_hp = damage * skill.effect / 100
            player.stats["HP"] += int(damage)
            if player.stats["HP"] > player.stats["Max HP"]:
                player.stats["HP"] = player.stats["Max HP"]
            print(f"Using {skill.name} buff:")
            print(f"    - {skill.type} +{skill.effect}% of damage (+{bonus_hp} HP)")

        case "Raven Chaser":
            lost_hp = player.stats["Max HP"] - player.stats["HP"]
            bonus_hp = lost_hp * skill.effect / 100
            player.stats["HP"] += int(bonus_hp)
            if player.stats["HP"] > player.stats["Max HP"]:
                player.stats["HP"] = player.stats["Max HP"]
            print(f"Using {skill.name} buff:")
            print(f"    - {skill.type} +{skill.effect}% of lost HP (+{bonus_hp} HP)")

        case _:
            if skill.type == "ATK":
                bonus += skill.effect
            else:
                player.stats["HP"] += skill.effect
                if player.stats["HP"] > player.stats["Max HP"]:
                    player.stats["HP"] = player.stats["Max HP"]
            print(f"Using {skill.name} buff:")
            print(f"    - {skill.type} +{skill.effect}")
    return True, bonus

def _use_skill(player: Player, monster: Monster, skill_list: SkillList, battle: Battle) -> bool:
    if battle.cooldown > 0:
        print(f"You cannot use skills in {battle.cooldown} rounds.")
        return _player_attack_action(player, monster)
    
    while True:
        header_len = create_header(player.name, player.money, "BATTLE")
        _show_stats(player, monster)
        print("=" * header_len)

        player_skills = list(player.skill_set)
        for i, skill in enumerate(player_skills, 1):
            print(f"[{i}] {skill}")
        
        print("[*] Basic Attack")
        choice = input("Your Choice: ")
        try:
            selected_skill = player_skills[int(choice) - 1]
        except (KeyError, ValueError):
            return _player_attack_action(player, monster)
    
        skill = [x for x in skill_list if x.name == selected_skill][0]
        ok, bonus = _skill_handler(player, monster, skill)
        if not ok:
            continue
        battle.cooldown = 4
        return _player_attack_action(player, monster, bonus)



# def start_battle(player: Player, monster: Monster, skills: list[Skill]) -> bool:
#     battle = Battle()
#     battle.add_char(player)
#     battle.add_char(monster)

#     current_turn = battle.head
#     result = False

#     while battle.total_char > 1:
#         clear_screen()
#         header_len = create_header(player.name, player.money, "BATTLE")
#         print(header_len)
#         _show_stats(player, monster)
#         print("=" * header_len)

#         if current_turn and current_turn.char == player:
#             if battle.cooldown > 0:
#                 battle.cooldown -= 1

#             print("[1] Use Skill")
#             print("[*] Attack")
#             choice = input("Your Choice: ")

#             is_dead = False
#             match choice:
#                 case "1":
#                     is_dead = _use_skill(player, monster, skills, battle)
#                 case _:
#                     is_dead = _player_attack_action(player, monster)

#             if is_dead:
#                 battle.remove_char(monster)
#                 result = True
#         else:
#             is_dead = _monster_attack_action(monster, player)
#             if is_dead:
#                 battle.remove_char(player)
            
#         input("[OK]")
#         current_turn = current_turn.next

#     monster.reset()
#     return result





# # PRIVATE FUNCTION
# def _use_skill(player: Player, monster: Monster, skills: list[Skill], battle: Battle) -> bool:
#     if battle.cooldown > 0:
#         print(f"You cannot use skills in {battle.cooldown} rounds.")
#         return _player_attack_action(player, monster)

#     while True:
#         clear_screen()
#         header_len = create_header(player.name, player.money, "BATTLE")
#         print(header_len)

#         _show_stats(player, monster)

#         print("=" * header_len)

#         player_skills = list(player.skill)
#         for i, skill in enumerate(player_skills, 1):
#             print(f"[{i}] {skill}")
        
#         print("[*] Cancel")
#         choice = input("Your Choice: ")
#         try:
#             selected_skill = player_skills[int(choice) - 1]
#         except (ValueError, KeyError):
#             return _player_attack_action(player, monster)

#         skill = [x for x in skills if x.name == selected_skill][0]
#         bonus = 0
#         match selected_skill:
#             case "Evil Eye":
#                 attack = player.stats["ATK"] + player.equipment.get_total_attack()
#                 damage = max(0, attack - monster.stats["DEF"])
#                 bonus_hp = damage * skill.effect / 100
#                 player.stats["HP"] += int(damage)
#                 if player.stats["HP"] > player.stats["Max HP"]:
#                     player.stats["HP"] = player.stats["Max HP"]

#                 print(f"Using {skill.name} buff:")
#                 print(f"    - {skill.type} +{skill.effect}% of damage (+{bonus_hp} HP)")
#             case "Baraju Spinner":
#                 if player.stats["HP"] <= 15:
#                     print("Not have enough HP.")
#                     input("[OK]")
#                     continue

#                 player.stats["HP"] -= 15
#                 bonus += skill.effect

#                 print(f"Using {skill.name} buff:")
#                 print(f"    - {skill.type} +{skill.effect}")
#                 print("    - HP -15")
#             case "Raven Chaser":
#                 lost_hp = player.stats["Max HP"] - player.stats["HP"]
#                 bonus_hp = lost_hp * skill.effect / 100
#                 player.stats["HP"] += int(bonus_hp)
#                 if player.stats["HP"] > player.stats["Max HP"]:
#                     player.stats["HP"] = player.stats["Max HP"]
                
#                 print(f"Using {skill.name} buff:")
#                 print(f"    - {skill.type} +{skill.effect}% of lost HP (+{bonus_hp} HP)")
#             case _:
#                 if skill.type == "ATK":
#                     bonus += skill.effect
#                 else:
#                     player.stats["HP"] += skill.effect
#                     if player.stats["HP"] > player.stats["Max HP"]:
#                         player.stats["HP"] = player.stats["Max HP"]

#                 print(f"Using {skill.name} buff:")
#                 print(f"    - {skill.type} +{skill.effect}")

#         battle.cooldown = 4
#         return _player_attack_action(player, monster, bonus)

# def _monster_attack_action(monster: Monster, player: Player):
#     defence = player.stats["DEF"] + player.equipment.get_total_defence()
#     damage = max(0, monster.stats["ATK"] - defence)

#     player.stats["HP"] -= damage
#     set_player_stats(player.name, player.get_stats())
#     print(f"{monster.name} deal {damage} damage to you.")

#     if not player.is_alive():
#         print("You died.")
#         player.reset()
#         return True


# def _player_attack_action(player: Player, monster: Monster, bonus: int = 0):
#     attack = player.stats["ATK"] + player.equipment.get_total_attack() + bonus
#     damage = max(0, attack - monster.stats["DEF"])

#     monster.stats["HP"] -= damage
#     print(f"You deal {damage} damage to {monster.name}.")

#     if not monster.is_alive():
#         player.exp += monster.exp_drop
#         player.money += monster.coin_drop

#         print("\nYou successfully defeated")
#         print(f"{monster.name}. You received")
#         print(f"{monster.exp_drop} exp and {monster.coin_drop} coins.")

#         player.check_level_up()
#         set_player_stats(player)
#         return True
    
#     return False

# def _show_stats(player: Player, monster: Monster):
#     print(f"Name   : {player.name}")
#     print(f"Health : {player.stats["HP"]}")
#     print(f"ATK    : {player.stats["ATK"]} (+{player.equipment.get_total_attack()})")
#     print(f"DEF    : {player.stats["DEF"]} (+{player.equipment.get_total_defence()})")

#     print(f"{'VS':^32}")

#     print(f"Name   : {monster.name}")
#     print(f"Health : {monster.stats["HP"]}")
#     print(f"ATK    : {monster.stats["ATK"]}")
#     print(f"DEF    : {monster.stats["DEF"]}")