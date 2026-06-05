from ..util import clear_screen
from ..struct import Player

def show_stats(player: Player):
    clear_screen()
    header = "=" * 12 + " STATS " + "=" * 12

    print(f"Name    : {player.name}")
    print(f"Balance : {player.money}")
    print(header)
    
    print(f"HP     : {player.stats["HP"]}")
    print(f"Max HP : {player.stats["Max HP"]}")
    print(f"ATK    : {player.stats["ATK"]} (+{player.equipment.get_total_attack()})")
    print(f"DEF    : {player.stats["DEF"]} (+{player.equipment.get_total_defence()})")
    print(f"Exp    : {player.exp} / 100")
    print(f"Level  : {player.level}")

    print("=" * len(header))
    input("[Back]")