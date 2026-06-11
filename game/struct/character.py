class Character:
    """Parent of class Player and class Monster"""
    def __init__(
        self,
        name: str,
        health: int,
        max_health: int,
        attack: int,
        defence: int,
    ):
        self.name = name
        self.stats = {
            "HP": health,
            "Max HP": max_health,
            "ATK": attack,
            "DEF": defence,
        }
    
    def reset_stats(self):
        self.stats = {
            "HP": 100,
            "Max HP": 100,
            "ATK": 15,
            "DEF": 5,
        }