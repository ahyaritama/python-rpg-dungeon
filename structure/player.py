from .character import Character

class Player(Character):
    def __init__(
        self,
        name: str,
        money: int,
        health: int,
        max_hp: int,
        attack: int,
        defence: int,
        exp: int,
        level: int
    ):
        super().__init__(name, health, max_hp, attack, defence, exp, level)
        self.money = money
    