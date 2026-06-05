from ..struct import Battle, Monster, Player, Room
from ..util import clear_screen, set_player_stats

def start_battle(player: Player, monster: Monster) -> bool:
    battle = Battle()
    battle.add_character(player)
    battle.add_character(monster)

    current_turn = battle.head
    result = False

    while battle.total_char > 1:
        clear_screen()
        header = "=" * 12 + " BATTLE " + "=" * 12
        print(header)

        _show_stats(player, monster)

        print("=" * len(header))

        if current_turn.character == player:
            print("[*] Attack")
            choice = input("Your Choice: ")

            match choice:
                case _:
                    is_dead = _player_attack_action(player, monster)
                    if is_dead:
                        battle.remove_character(monster)
                        result = True
        else:
            is_dead = _monster_attack_action(monster, player)
            if is_dead:
                battle.remove_character(player)
            
        input("[OK]")
        current_turn = current_turn.next

    return result





# PRIVATE FUNCTION
def _monster_attack_action(monster: Monster, player: Player):
    defence = player.stats["DEF"] + player.equipment.get_total_defence()
    damage = max(0, monster.stats["ATK"] - defence)

    player.stats["HP"] -= damage
    set_player_stats(player)
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
        player.check_level_up()
        player.money += monster.coin_drop
        set_player_stats(player)

        print("\nYou successfully defeated")
        print(f"{monster.name}. You received")
        print(f"{monster.exp_drop} exp and {monster.coin_drop} coins.")
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