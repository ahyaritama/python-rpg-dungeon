def clear_screen():
    print("\033[H\033[2J")

def create_header(username: str, money: int, menu_name: str) -> int:
    header = f"{'=' * 12} {menu_name} {'=' * 12}"

    clear_screen()
    print(f"Name : {username}")
    print(f"Coin : {money}")
    print(header)

    return len(header)