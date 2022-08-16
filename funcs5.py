
def func1(pos1, pos2, key1='', key2=0):
    print(f"{pos1 = }")
    print(f"{pos2 = }")
    print(f"{key1 = }")
    print(f"{key2 = }")
    
def func2(pos1, pos2, /, pos_or_key1, pos_or_key2, *, key1, key2):
    print(f"{pos1 = }")
    print(f"{pos2 = }")
    print(f"{pos_or_key1 = }")
    print(f"{pos_or_key2 = }")
    print(f"{key1 = }")
    print(f"{key2 = }")
    
