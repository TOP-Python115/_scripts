# H  E  L  L  O  Z
# 8  5  12 12 15 26    +5
# 13 10 17 17 20 5
# M  J  Q  Q  T  E  -5

msg = input('enter message: ')
shift = int(input('enter shift number: '))

for ch in msg:
    if ord(ch) + shift > ord('z'):
        print( chr(ord(ch) + shift - 26), end='' )
    else:
        print( chr(ord(ch) + shift), end='' )
