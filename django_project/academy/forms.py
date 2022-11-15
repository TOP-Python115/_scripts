from django.forms import Form, CharField, DateField


class GroupAdd(Form):
    group_name = CharField(label='Идентификатор группы', min_length=4, max_length=10)
    group_start_year = DateField(label='Год начала обучения', input_formats=['%Y'])
