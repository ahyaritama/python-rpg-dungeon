from ..util import clear_screen
from ..struct import Player

def show_stats(player: Player):
    clear_screen()
    header = "=" * 12 + " STATS " + "=" * 12

    print(f"{'Name':<8}: {player.name}")
    print(f"{'Balance':<8}: {player.money}")
    print(header)
    
    for k, v in player.stats.items():
        print(f"{k:<7}: {v}{'/100' if k == 'Exp' else ''}")

    print("=" * len(header))
    input("[Back]")