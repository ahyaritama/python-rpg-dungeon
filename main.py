from game import auth, core, util, struct
from game.struct import item
from game.struct.map import init as map_init
from game.struct.skill import build_skill

def main():
    players = auth.load()
    monster = struct.monster.init()
    items = item.init()
    dungeon_map = map_init(monster, items)
    skill_tree = build_skill()

    while True:
        util.clear_screen()
        print("[1] Login")
        print("[2] Register")
        print("[*] Quit")
        choice = input("Your Choice: ")

        match choice:
            case "1":
                player = auth.login(players, items)
                if not player:
                    util.clear_screen()
                    continue
            case "2":
                player = auth.register(players)
                if not player:
                    util.clear_screen()
                    continue
            case _:
                print("\nThank you for playing our game!")
                break
        
        core.main_menu(player, items, skill_tree, dungeon_map)
    

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nThank you for playing our game!")
        pass