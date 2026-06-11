from ..struct import Player
from ..util import create_header

def reset_progress(player: Player):
    """Reset player's progress. Player need to confirm
    this action.
    """
    header_len = create_header(player.name, player.money, "RESET PROGRESS")
    print("Are you sure want to reset your progress?")
    print("This process is permanent.")
    print("=" * header_len)
    print("[1] Yes")
    print("[*] No")
    choice = input("Your Choice: ")
    match choice:
        case "1":
            player.reset()
        case _:
            pass