def get_player_skills(username: str) -> set[str]:
    skill_set: set[str] = set()
    with open(f"game/storage/skills/{username}", "r") as f:
        for line in f:
            skill_set.add(str(line).strip())
    
    return skill_set

def set_player_skills(username: str, skill_set: set[str]):
    with open(f"game/storage/skills/{username}", "w") as f:
        for skill in skill_set:
            f.write(skill + "\n")
