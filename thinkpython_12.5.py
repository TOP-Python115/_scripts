# sprite -> ('spite', 'sprit')
# spite
# spit
# pit
# it

from time import perf_counter as pc

words_path = 'd:\\G-Doc\\YandexDisk\\Scripts\\_Educational\\Think Python\\words.txt'

with open(words_path, encoding='utf-8') as f_in:
    text = f_in.read()

words = tuple(text.split())

def down(*strings):
    for word in strings:
        if word in words_down:
            return True
    for word in strings:
        if len(word) == 2:
            return True
        else:
            t = tuple()
            for i in range(len(word)):
                q = word[:i] + word[i+1:]
                if q in words and q not in t:
                    t += (q, )
            return down(*t)
    return False

words_down = tuple()
words_filtered = tuple(filter(lambda word: len(word) > 9, words))
lwf = len(words_filtered)
start = pc()
for i in range(lwf):
    if down(words_filtered[i]):
        words_down += (words_filtered[i], )
    print('\b'*15 + f'{i*100/lwf:.1f}' + '%',
          f'{pc()-start:.0f} сек',
          sep='\t', end='', flush=True)
