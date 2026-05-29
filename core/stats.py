import utils
from structure.player import Player

def stats(player: Player):
    utils.clear_screen()
    header = "=" * 10 + " STATS " + "=" * 10

    print(f"{'Name':<8}: {player.name}")
    print(f"{'Balance':<8}: {player.money}")
    print(header)
    
    for k, v in player.stats.items():
        print(f"{k:<7}: {v}")

    print("=" * len(header))
    input("[Back]")