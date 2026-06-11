from game import auth, core, util
from game.struct import item, monster, skill
from game.struct.map import init as map_init


def main():
    players = auth.load()
    monster_list = monster.init()
    item_dict = item.init()
    dungeon_map = map_init(monster_list, item_dict)
    skill_tree = skill.build()

    while True:
        util.clear_screen()
        print("[1] Login")
        print("[2] Register")
        print("[*] Quit")
        choice = input("Your Choice: ")

        match choice:
            case "1":
                player = auth.login(players, item_dict)
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
        
        core.main_menu(player, item_dict, skill_tree, dungeon_map)
    

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nThank you for playing our game!")
        pass