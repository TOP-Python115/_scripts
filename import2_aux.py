def count_words(text):
	return {word: text.count(word) for word in set(text.lower().split())}
