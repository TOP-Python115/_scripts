s = input()
while s:
    print(s[::-1])
    s = input()


while True:
    s = input()
    if s != 'quit':
        print(s[::-1])
    else:
        break
    
    if s == 'z':
        break


while s := input():
    print(s[::-1])
