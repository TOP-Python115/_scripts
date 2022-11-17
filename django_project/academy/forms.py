from django.forms import Form, CharField, DateField, CheckboxInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit, HTML
from crispy_forms.bootstrap import PrependedText, InlineCheckboxes


class GroupAdd(Form):
    group_name = CharField(label='Идентификатор группы', min_length=4, max_length=10)
    group_start_year = DateField(label='Год начала обучения', input_formats=['%Y'])


class StudentAdd(Form):
    student_name = CharField()
    is_curator_name = CheckboxInput()

    class Meta:
        fields = ['student_name', 'is_curator']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            HTML('<h4>{{ group.name }}</h4>'),
            PrependedText('student_name', text='ФИО студента'),
            # Field('student_name', title='ФИО студента'),
            # Field('is_curator_name', title='куратор'),
            # InlineCheckboxes('is_curator'),
            Submit('submit', 'Добавить студента')
        )
