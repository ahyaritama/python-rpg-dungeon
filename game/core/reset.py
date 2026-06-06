from ..struct import Player
from ..util import clear_screen

def reset_progress(player: Player):
    clear_screen()
    header = "=" * 12 + " RESET PROGRESS " + "=" * 12

    print(f"{'Name    '}: {player.name}")
    print(f"{'Balance '}: {player.money}")
    print(header)

    print("Are you sure want to reset your progress?")
    print("This process is permanent.")

    print("=" * len(header))
    print("[1] Yes")
    print("[*] No")

    choice = input("Your Choice: ")
    match choice:
        case "1":
            player.reset()
        case _:
            pass