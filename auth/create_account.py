def create_account(x):
    while True:
        username = input("Input your username: ")
        if username in x:
            print("[*] Username already taken\n")
            continue
        
        password = input("Input your password: ")
        ok, msg = _validate(username, password)
        if ok:
            x[username] = password
            break
        print(msg)
    
    _add_auth(username, password)

def _validate(username: str, password: str) -> bool:
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

def _add_auth(username: str, password: str):
    with open("storage/auth", "a") as f:
        f.write(f"{username},{password}\n")