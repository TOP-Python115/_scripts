
def myprint2(message, filler='='):
	l = myprint3(message, 5)
	if ' ' in message:
		return f"{filler} {message} {filler}"
	else:
		return f"{filler}{message}{filler}"

def myprint3(message, num):
	return [message for _ in range(num)]


print(myprint2('asd'))


# s = input()
# print(myprint2(s, '##'))
