from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def info(self):
        print('Abstract basic class')

class B(A):
    def info(self):
        super().info()
        print('Realization class')
