class Item:
    def __init__(self, name, code,  effect, price):
        self.name = name
        self.code = code
        self.effect = effect
        self.price = price

def init():
    item_dict = {

        "ATK_01": Item("Rusty Sword", "ATK_01", 10, 250),
        "ATK_02": Item("Wooden Bow", "ATK_02", 7, 120),
        "ATK_03": Item("X-Bow", "ATK_03", 10, 300),
        "ATK_04": Item("Wooden Spear", "ATK_04", 5, 50),
        
        "DEF_01": Item("Leather Armor", "DEF_01", 7, 180),
        "DEF_02": Item("Wooden Shield", "DEF_02", 5, 80),
        "DEF_03": Item("Leather Helmet", "DEF_03", 4, 40),
        
        "HP_01": Item("Bread", "HP_01", 5, 15),
        "HP_02": Item("Health Potion", "HP_02", 10, 60),
        "HP_03": Item("Meat", "HP_03", 7, 30)
        }
    
    return item_dict