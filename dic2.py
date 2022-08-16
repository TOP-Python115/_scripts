cashe = {'ss64.com': 'cmd bash how-to',
         'docs.python.org': 'library language reference modules',
         'docs.microsoft.com': 'windows office t-sql server',
         'sqlite.com': 'SELECT clause INSERT agregate functions'}

while word := input('введите слово для поиска: '):
    for site, text in cashe.items():
        if word.lower() in text.lower():
            print(site)
            break
    else:
        print('не найдено')
