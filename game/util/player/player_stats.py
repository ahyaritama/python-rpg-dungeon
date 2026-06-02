from ...struct import Player

def get_player_stats(username: str) -> dict[str, int]:
    stats: dict[str, int] = {}
    with open(f"game/storage/stats/{username}", "r") as f:
        for line in f:
            key, value = line.split("=", 1)
            stats[key] = int(value)
    
    return stats

def set_player_stats(player: Player):
    key = ("money", "health", "max_hp", "attack", "defence", "exp", "level")
    value = (player.money, *player.stats.values())

    with open(f"game/storage/stats/{username}", "w") as f:
        for i in range(key):
            f.write(key[i] + "=" + value[i])