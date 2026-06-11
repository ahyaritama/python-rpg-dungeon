from ..util import create_header
from ..struct import Player

def show_stats(player: Player):
    """Show player's full stats."""
    header_len = create_header(player.name, player.money, "STATS")
    print(f"HP     : {player.stats["HP"]}")
    print(f"Max HP : {player.stats["Max HP"]}")
    print(f"ATK    : {player.stats["ATK"]} (+{player.equipment.get_total_attack()})")
    print(f"DEF    : {player.stats["DEF"]} (+{player.equipment.get_total_defence()})")
    print(f"Exp    : {player.exp} / 100")
    print(f"Level  : {player.level}")
    print("=" * header_len)
    input("[Back]")