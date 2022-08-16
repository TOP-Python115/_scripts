"""Простой строитель на примере конструирования фрагментов кода"""

# class Foo:
#   pass
#
# class Bar:
#   def __init__(self):
#     self.name = ""
#     self.age = 0


class ClassBuilder:
    indent_length = 4
    
    def __init__(self, class_name):
        self.name = class_name
        self.inst_fields = {}
    
    def add_field(self, field_name, def_value):
        self.inst_fields[field_name] = def_value
        return self
    
    def __str__(self):
        lines = ()
        lines += (f'class {self.name}:',)
        tab = ' '*self.__class__.indent_length
        if self.inst_fields:
            lines += (f'{tab}def __init__(self):',)
            for name, value in self.inst_fields.items():
                lines += (f'{tab*2}{name} = {value}',)
        else:
            lines += (f'{tab}pass',)
        return '\n'.join(lines)


class1 = ClassBuilder('Foo')
print(class1, end='\n\n')

class2 = ClassBuilder('Person')
class2.add_field('name', '""')\
      .add_field('age', '0')\
      .add_field('birthdate', '""')
print(class2, end='\n\n')
