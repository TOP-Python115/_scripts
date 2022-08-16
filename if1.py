# if ... elif ... else ...

s = input("String: ")
c = input("Character: ")

if c in s:
    if c*2 in s:
        print(f"substring '{c*2}' is in string '{s}'")
    else:
        print(f"substring '{c}' is in string '{s}'")
else:
    print(f"substring '{c}' is not in string '{s}'")
