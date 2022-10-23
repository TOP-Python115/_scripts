from abc import ABC, abstractmethod
from datetime import datetime as dt
from time import sleep


class Patient(ABC):
    """Интерфейс наблюдаемого объекта."""
    def __init__(self, name: str):
        self.name = name
        self.__monitors: list['Monitor'] = []

    def add_monitor(self, device: 'Monitor'):
        """Подписка объекта наблюдателя."""
        self.__monitors.append(device)

    def remove_monitor(self, device: 'Monitor'):
        """Отмена подписки объекта наблюдателя."""
        self.__monitors.remove(device)

    def update_monitors(self, subject: 'Patient'):
        """Уведомление наблюдателей о событии."""
        for device in self.__monitors:
            device.update(subject)

    @abstractmethod
    def get_value(self, parameter: str):
        pass

    @abstractmethod
    def set_value(self, parameter: str, value):
        pass


class COVIDPatient(Patient):
    """Наблюдаемый объект (субъект наблюдения)."""
    def __init__(self, name: str):
        super().__init__(name)
        self.__parameters = {
            'temperature': 36.9,
            'heartrate': 92,
            'saturation': 95.3
        }

    def get_value(self, parameter: str):
        return self.__parameters.get(parameter)

    def set_value(self, parameter: str, value):
        """Устанавливает значения наблюдаемых параметров — генерирует отслеживаемое наблюдателями событие."""
        if parameter in self.__parameters:
            self.__parameters[parameter] = value
            self.update_monitors(subject=self)


class Monitor(ABC):
    """Интерфейс наблюдателя."""
    @abstractmethod
    def update(self, subject: Patient):
        """Анализирует значения наблюдаемых параметров и генерирует различную реакцию."""

    # методы реакции
    @staticmethod
    def info_message(text: str):
        print(f'ИНФО - {text}')

    @staticmethod
    def warn_message(text: str):
        print(f'ПРЕДУПРЕЖДЕНИЕ - {text}')

    @staticmethod
    def emrg_message(text: str):
        print(f'КРИТИЧНО! {text}')


class Thermometer(Monitor):
    """Наблюдатель температуры."""
    def update(self, subject: Patient):
        temperature = subject.get_value('temperature')
        message = f'ТЕМПЕРАТУРА: {subject.name} - {temperature}'
        if 36.4 <= temperature < 37.2:
            self.info_message(message)
        elif 37.2 <= temperature < 38.1:
            self.warn_message(message)
        else:
            self.emrg_message(message)


class Heartbeat(Monitor):
    """Наблюдатель пульса."""
    def update(self, subject: Patient):
        heartrate = subject.get_value('heartrate')
        message = f'ПУЛЬС: {subject.name} - {heartrate}'
        if heartrate < 95:
            self.info_message(message)
        elif 95 <= heartrate < 115:
            self.warn_message(message)
        else:
            self.emrg_message(message)


class Oxymeter(Monitor):
    """Наблюдатель сатурации."""
    def update(self, subject: Patient):
        saturation = subject.get_value('saturation')
        message = f'САТУРАЦИЯ: {subject.name} - {saturation}'
        if 95 <= saturation:
            self.info_message(message)
        elif 93 < saturation < 95:
            self.warn_message(message)
        else:
            self.emrg_message(message)


ivan = COVIDPatient('Иван')

monitor = [
    Thermometer(),
    Heartbeat(),
    Oxymeter()
]

for sensor in monitor:
    ivan.add_monitor(sensor)

ivan.update_monitors(ivan)

start_temp = ivan.get_value('temperature')
start_rate = ivan.get_value('heartrate')
start_satur = ivan.get_value('saturation')

for i in range(1, 61):
    print(f'\n{dt.now():%H:%M:%S}')
    # генерация событий
    ivan.set_value('temperature', start_temp + i*0.04)
    ivan.set_value('heartrate', round(start_rate + i*0.5))
    ivan.set_value('saturation', start_satur - i*0.05)
    sleep(1)
