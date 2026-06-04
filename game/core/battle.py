from ..struct import Player, Monster
from ..util import clear_screen

def start_battle(player: Player):
    while True:
        clear_screen()
        header = "=" * 12 + " BATTLE " + "=" * 12

        print(f"Name   : {player.name}")
        print(f"Health : {player.stats["HP"]}")
        print(f"{'VS':^32}")
        print(f"Name   : {player.name}")
        print(f"Health : {player.stats["HP"]}")
        print(header)

        print("=" * len(header))
        input()
        break