"""Реализация Компоновщика с использованием класса-примеси."""

class Connectable:
    def connect_to(self, other):
        if self == other:
            return
        for self_neuron in self:
            for other_neuron in other:
                self_neuron.outputs.append(other_neuron)
                other_neuron.inputs.append(self_neuron)


class Neuron(Connectable):
    def __init__(self, name: str):
        self.name = name
        self.inputs: list = []
        self.outputs: list = []

    def __str__(self):
        return f'<{self.name}: {len(self.inputs)}i, {len(self.outputs)}o>'

    # def connect_to(self, other):
    #     self.outputs.append(other)
    #     other.inputs.append(self)

    def __iter__(self):
        yield self


class NeuronLayer(list, Connectable):
    def __init__(self, name: str, count: int):
        super().__init__()
        self.name = name
        for i in range(count):
            self.append(Neuron(f'{self.name} Neuron{i+1}'))

    def __str__(self):
        return f'<{self.name}: {len(self)}n>'


# def connect_to(obj1, obj2):
#     if obj1 == obj2:
#         return
#     for el1 in obj1:
#         for el2 in obj2:
#             el1.outputs.append(el2)
#             el2.inputs.append(el1)
#
#
# Neuron.connect_to = connect_to
# NeuronLayer.connect_to = connect_to

n1 = Neuron('Neuron1')
n2 = Neuron('Neuron2')
n1.connect_to(n2)
# connect_to(n1, n2)
print(n1, n2, sep='\n', end='\n\n')

l1 = NeuronLayer('Layer1', 3)
l2 = NeuronLayer('Layer2', 4)

l1.connect_to(l2)
n1.connect_to(l1)
l2.connect_to(n2)
# connect_to(l1, l2)
# connect_to(n1, l1)
# connect_to(l2, n2)
print(n1, n2, l1, l2, sep='\n', end='\n\n')
for neuron in l1:
    print(neuron)
for neuron in l2:
    print(neuron)
