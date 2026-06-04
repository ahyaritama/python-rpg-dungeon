from .character import Character

class Monster(Character):
    def __init__(
        self,
        name: str,
        health: int,
        attack: int,
        defence: int,
        exp_drop: int,
        coin_drop: int
    ):
        self.exp_drop = exp_drop
        self.coin_drop = coin_drop
        super().__init__(name, health, health, attack, defence)
    
    def take_damage(self, damage: int):
        self.stats["HP"] -= damage
        if self.stats["HP"] < 0:
            self.stats["HP"] = 0
    
    def is_alive(self):
        return self.stats["HP"] > 0

def init() -> list[Monster]:
    return [
        Monster("Serpo", 30, 8, 2, 15, 10),
        Monster("Goche", 40, 10, 3, 20, 15),
        Monster("Korn", 50, 11, 4, 25, 20),
        Monster("Destra", 65, 14, 5, 35, 40),
        Monster("Gin", 75, 16, 6, 40, 50),
        Monster("Flatwoods", 95, 18, 8, 45, 70),
        Monster("Rum", 115, 22, 9, 50, 100),
        Monster("Red Baron", 130, 25, 11, 55, 130),
        Monster("Zamigo", 155, 28, 13, 65, 180),
        Monster("Vlad", 185, 32, 15, 75, 250),
        Monster("Dogranio", 220, 36, 17, 85, 350),
        Monster("Renya Karasuma", 280, 42, 20, 100, 700)
    ]