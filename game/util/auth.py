def validate(username: str, password: str) -> tuple[bool, str]:
    username_status = True
    password_status = True
    message = ""

    if len(username) == 0:
        username_status = False
        message += "[*] Username cannot be empty"
    elif not all(x.isalnum() or x in {"-", "_"} for x in username):
        username_status = False
        message += "[*] Username can only contain alphanumeric, - and _\n"

    if len(password) < 8:
        password_status = False
        message += "[*] Minimum password length is 8 characters\n"
        
    return username_status and password_status, message