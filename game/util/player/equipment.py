def get_player_equipment(username: str) -> set[str]:
    code_set: set[str] = set()
    with open(f"game/storage/equipment/{username}", "r") as f:
        for line in f:
            code = line.strip()
            if code == "":
                continue
            code_set.add(code)
    
    return code_set

def set_player_equipment(username: str, code_set: set[str]):
    with open(f"game/storage/equipment/{username}", "w") as f:
        for code in code_set:
            f.write(code + "\n")



# def get_player_equipment(username: str, items: ItemDict) -> Equipment:
#     codes: set[str] = set()
#     itemset: ItemSet = set()
#     with open(f"game/storage/equipment/{username}", "r") as f:
#         for line in f:
#             codes.add(str(line).strip())
#             itemset.add(items[str(line).strip()])

#     return Equipment(codes, itemset)

# def set_player_equipment(username: str, codes: set[str]):
#     with open(f"game/storage/equipment/{username}", "w") as f:
#         for code in codes:
#             f.write(code + "\n")