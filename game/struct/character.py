class Character:
    def __init__(
        self,
        name: str,
        health: int,
        max_health: int,
        attack: int,
        defence: int,
        exp: int,
        level: int
    ):
        self.name = name
        self.stats = {
            "HP": health,
            "Max HP": max_health,
            "ATK": attack,
            "DEF": defence,
            "Exp": exp,
            "Lvl": level
        }