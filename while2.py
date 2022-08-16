
while True:
    command = input()
    if command == 'quit' or command == 'exit' or \
       command == 'выход' or command == 'выйти':
        break
    else:
        for char in command:
            if not char.isdecimal():
                print("can't turn into 'int'")
                break
        else:
            n = int(command)
            print(f"{n} – {type(n)}")
