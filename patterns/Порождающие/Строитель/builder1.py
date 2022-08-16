"""Простой строитель на примере конструирования HTML документа"""

# <p>
#   text
#   <ul>
#     <li>
#       list elem
#     </li>
#     <li>
#       list elem
#     </li>
#   </ul>
# </p>

class HtmlElement:
    default_indent = 2
    
    def __init__(self, tag_name, tag_content=''):
        self.name = tag_name
        self.content = tag_content
        self.elements = []
        
    def __str__(self):
        return self.__str()
    
    def __str(self, indent_level=0):
        tab = ' '*(self.__class__.default_indent * indent_level)
        lines = ()
        lines += (f'{tab}<{self.name}>',)
        if self.content:
            ttab = ' '*(self.__class__.default_indent * (indent_level + 1))
            lines += (f'{ttab}{self.content}',)
        for el in self.elements:
            lines += (el.__str(indent_level + 1),)
        lines += (f'{tab}</{self.name}>',)
        return '\n'.join(lines)
    
    @staticmethod
    def create(root_tag_name):
        return HtmlBuilder(root_tag_name)


class HtmlBuilder:
    def __init__(self, root_tag_name):
        self.__root = HtmlElement(root_tag_name)
    
    def add_child(self, child_tag_name, child_tag_content=''):
        q = HtmlElement(child_tag_name, child_tag_content)
        self.__root.elements += [q]
        return self
    
    def __str__(self):
        return str(self.__root)


# root = HtmlBuilder('ul')
root = HtmlElement.create('ul')
root.add_child('li', 'list elem 1')\
    .add_child('li', 'list elem 2')
print(root)
