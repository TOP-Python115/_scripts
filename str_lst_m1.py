# На вход программе подается строка генетического кода, состоящая из букв А (аденин), Г (гуанин), Ц (цитозин), Т (тимин). 
# Напишите программу, которая подсчитывает сколько аденина, гуанина, цитозина и тимина входит в данную строку генетического кода.
# Сгруппируйте по тройкам, для каждой тройки сгенерируйте комплементарные: А–Т, Ц–Г, Г–Ц, Т–А.

gen = input()
nucl = [(c, gen.count(c)) for c in ('А', 'Т', 'Ц', 'Г')]
print(f'\nnucl = {nucl}\n')

gen_triples = [gen[i:i+3] for i in range(0, len(gen), 3)]
print(f'\ngen_triples = {gen_triples}\n')

# gen_triples_compl = []
# for t in gen_triples:
    # s = ''
    # for c in t:
        # if c == 'А': s += 'Т'
        # elif c == 'Т': s += 'А'
        # elif c == 'Г': s += 'Ц'
        # elif c == 'Ц': s += 'Г'
    # gen_triples_compl += [s]
# print(f'\ngen_triples_compl = {gen_triples_compl}\n')

for cp in (('А', 'Т'), ('Ц', 'Г')):
    gen = gen.replace(cp[0], cp[1].lower())
    gen = gen.replace(cp[1], cp[0].lower())
gen_triples_compl = [gen.upper()[i:i+3] for i in range(0, len(gen), 3)]
print(f'\ngen_triples_compl = {gen_triples_compl}\n')