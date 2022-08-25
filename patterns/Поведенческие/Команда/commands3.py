from abc import ABC, abstractmethod
from time import time, sleep
from datetime import datetime as dt


class Light:
    @staticmethod
    def turn_on() -> None:
        print('Light is turned on')

    @staticmethod
    def turn_off() -> None:
        print('Light is turned off')


class Switch:
    def __init__(self):
        self._commands = {}
        self.history = []

    def register(self,
                 command_name: str,
                 command: object):
        self._commands[command_name] = command

    def execute(self, command_name: str):
        if command_name in self._commands:
            self._commands[command_name].execute()
            self.history.append((command_name, time()))
        else:
            print(f'wrong command')

    def show_history(self):
        for command_name, timestamp in self.history:
            time_read = dt.fromtimestamp(timestamp).strftime('%H:%M:%S')
            print(f'{time_read}: {command_name}')


class InterfaceSwitch(ABC):
    @staticmethod
    @abstractmethod
    def execute(self):
        pass

class SwitchONCommand(InterfaceSwitch):
    def __init__(self, receiver: Light):
        self._receiver = receiver

    def execute(self):
        self._receiver.turn_on()

class SwitchOFFCommand(InterfaceSwitch):
    def __init__(self, receiver: Light):
        self._receiver = receiver

    def execute(self):
        self._receiver.turn_off()



l1 = Light()

switch = Switch()
switch.register('ON', SwitchONCommand(l1))
switch.register('OFF', SwitchOFFCommand(l1))

switch.execute('ON')
sleep(2)
switch.execute('OFF')

switch.show_history()




