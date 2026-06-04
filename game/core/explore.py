from ..util import clear_screen

from ..struct import (
    Player,
    SkillTree,
    Map
)

def explore(player: Player, skill_tree: SkillTree, dungeon_map: Map):
    while True:
        clear_screen()
        header = "=" * 12 + " EXPLORE " + "=" * 12

        print(f"{'Name    '}: {player.name}")
        print(f"{'Balance '}: {player.money}")
        print(header)

        print("=" * len(header))
        break