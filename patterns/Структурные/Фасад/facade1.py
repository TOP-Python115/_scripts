"""Реализация шаблона Фасад на примере проектирования интерфейса для последовательности запуска персонального компьютера."""


class CPU:
    @staticmethod
    def cooling() -> None:
        print('CPU cooler start')

    @staticmethod
    def read_register(register: str) -> None:
        print(f'Register {register} read')

    @staticmethod
    def execute() -> None:
        print('Execute')


class RAM:
    @staticmethod
    def load(data: str) -> None:
        print(f'Data {data} loaded')


class Drive:
    @staticmethod
    def read(block: str) -> str:
        return f'Data from {block} block read'


class Computer:
    """Фасад для компонентов компьютера."""
    def __init__(self):
        self.cpu = CPU()
        self.ram = RAM()
        self.drive = Drive()

    def start(self) -> bool:
        """Выполняет последовательность запуска."""
        try:
            self.cpu.cooling()
            self.cpu.read_register('0x0001')
            self.ram.load(self.drive.read('00A0100'))
            self.cpu.execute()
        except:
            return False
        else:
            return True


PC = Computer()
if PC.start():
    print('Success')
else:
    print('Failure')
