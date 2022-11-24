from django import forms
from django.forms import fields
from django.forms import widgets

from datetime import datetime as dt


years_range = [year for year in range(dt.now().year, dt.now().year-6, -1)]


class GroupAdd(forms.Form):
    group_name = fields.CharField(
        label='Идентификатор группы',
        min_length=4,
        max_length=10
    )
    group_start_year = fields.DateField(
        label='Год начала обучения',
        input_formats=['%Y'],
        widget=widgets.SelectDateWidget(
            years=years_range
        )
    )


class StudentAdd(forms.Form):
    """"""
    surname = fields.CharField(
        label='Фамилия студента:',
        min_length=1
    )
    name = fields.CharField(
        label='Имя студента:',
        min_length=1
    )
    is_curator = fields.BooleanField(
        required=False
    )
    rating = fields.IntegerField(
        label='Рейтинг студента:',
        min_value=0,
        max_value=5,
        widget=widgets.NumberInput(
            # attrs={
            #     'class': ''
            # }
        )
    )
