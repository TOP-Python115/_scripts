from pprint import pprint
import json

# в переменных ниже заменить ... на абсолютный путь к файлу
file_r_path = "...\\first.json"
file_w1_path = "...\\file3.json"
file_w2_path = "...\\file3_2.json"

with open(file_r_path, encoding='utf-8') as fin:
	obj1 = json.load(fin)

with open(file_r_path, encoding='utf-8') as fin:
	text = fin.read()
obj2 = json.loads(text)

print('obj1 == obj2\t->\t', obj1 == obj2)


cashe = {'ss64.com': ['cmd', 'bash', 'how-to'],
         'docs.python.org': ['library', 'language', 'reference', 'modules'],
         'docs.microsoft.com': ['windows', 'office', 't-sql', 'server'],
         'sqlite.com': ['SELECT', 'clause', 'INSERT', 'agregate', 'functions']}

with open(file_w1_path, 'w', encoding='utf-8') as fout:
	json.dump(cashe, fout, indent=8)

str_to_json = json.dumps(cashe, indent=2)
with open(file_w2_path, 'w', encoding='utf-8') as fout:
	fout.write(str_to_json)
