"""Пример реализации Компоновщика для рендера различных графических элементов"""

from abc import ABC, abstractmethod


class Graphic(ABC):
    @abstractmethod
    def render(self) -> None:
        pass


class Line(Graphic):
    def __init__(self, name: str):
        self.name = name

    def render(self) -> None:
        print(f'Line {self.name}')


class Text(Graphic):
    def __init__(self, name: str, text: str):
        self.name = name
        self.text = text

    def render(self) -> None:
        print(f'Text {self.name}\n\t{self.text}')


class GroupGraphic(Graphic):
    def __init__(self):
        self.components: list[Graphic] = []

    def add(self, component: Graphic):
        self.components.append(component)

    def render(self) -> None:
        for component in self.components:
            component.render()

    def __getitem__(self, index: int) -> Graphic:
        return self.components[index]


l1 = Line('AB')
l2 = Line('BC')
l3 = Line('CD')
l4 = Line('DA')
shape = GroupGraphic()
for line in (l1, l2, l3, l4):
    shape.add(line)

t1 = Text('formula', 'P = AB + BC + CD + DA')

figure = GroupGraphic()
figure.add(shape)
figure.add(t1)

figure.render()

print('\n')

figure[0][0].render()
figure[0][-1].render()
