from django.db import models

from transliterate import translit


class Faculty(models.Model):
    name = models.CharField(max_length=100)

    @property
    def short(self):
        return self.__repr__()

    def __repr__(self):
        short = [
            translit(word[0].lower(), 'ru', reversed=True)
            for word in str(self.name).replace('-', ' ').split()
            if len(word) > 1
        ]
        return ''.join(short)

    def __str__(self):
        return f'{self.name}'


class Department(models.Model):
    name = models.CharField(max_length=100)
    building = models.PositiveSmallIntegerField()
    financing = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    faculty_id = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


class Group(models.Model):
    name = models.CharField(max_length=10)
    year = models.PositiveSmallIntegerField()
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


class Curator(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    groups = models.ManyToManyField(Group)


class Teacher(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    is_professor = models.BooleanField(default=False)


class Subject(models.Model):
    name = models.CharField(max_length=100)
    teachers = models.ManyToManyField(Teacher, through='Lecture')


class Lecture(models.Model):
    date = models.DateTimeField()
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    groups = models.ManyToManyField(Group)


class Student(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    rating = models.PositiveSmallIntegerField()
    groups = models.ManyToManyField(Group)

