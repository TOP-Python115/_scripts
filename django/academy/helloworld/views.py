from django.shortcuts import render

from django.template import Template, Context, Engine

from django.http import HttpResponse


def helloworld(request):
    # строковый шаблон
    content = """
    <h2>{{ title }}</h2>
    <p><i>{{ lead }}</i></p>
    """
    # движок шаблонизатора — по умолчанию используется первый корректно загруженный из TEMPLATES в модуле проекта settings
    engine = Engine()
    # объект шаблона — дерево
    template = Template(content, engine=engine)
    # объект контекста — стек (словароподобный)
    context = Context({
        'title': 'Главная страница',
        'lead': 'Приветствуем вас на сайте helloworld!'
    })
    # context['text'] = 'Описание проекта...'
    # рендер шаблона — подстановка значений из контекста в шаблон и генерация окончательного документа
    document = template.render(context)
    print(document)
    print(type(document))
    return HttpResponse(document)
