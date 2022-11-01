from django.http import HttpResponse

from .models import Faculty

from pprint import pprint


def institutes_list(request):
    institutes = Faculty.objects.all()
    document = '<h2>Институты университета</h2>\n'
    document += '<ol>\n'
    for obj in institutes:
        document += f'\t<li><a href=/academy/{obj!r}>{obj!s}</a></li>\n'
    document += '</ol>'
    return HttpResponse(document)


def faculty_main(request, faculty_obj: Faculty):
    print()
    pprint([attr for attr in dir(request) if not attr.startswith('__')])
    print(f'\n{request.path}\n')
    pprint(list(request.headers.keys()))
    print()

    document = f'<h2>{faculty_obj.name}</h2>\n'
    document += '<h4>История института</h4>\n' \
                '<p>...</p>\n'
    departments = faculty_obj.department_set.all()
    document += '<h4>Кафедры</h4>\n' \
                '<ol>\n'
    for obj in departments:
        document += f'\t<li>{str(obj).capitalize()}</li>\n'
    document += '</ol>'
    return HttpResponse(document)
