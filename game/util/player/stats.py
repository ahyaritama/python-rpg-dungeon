def get_player_stats(username: str) -> dict[str, int]:
    stats_dict: dict[str, int] = dict()
    with open(f"game/storage/stats/{username}", "r") as f:
        for line in f:
            line_strip = line.strip()
            if line_strip == "":
                continue

            key, value = line.split("=", 1)
            stats_dict[key] = int(value)

    return stats_dict

def set_player_stats(username: str, stats_dict: dict[str, int]):
    with open(f"game/storage/stats/{username}", "w") as f:
        for key, value in stats_dict.items():
            f.write(f"{key}={value}\n")