from abc import  ABC, abstractmethod

class Figure(ABC):
    #абстрактный класс геометрическая фигура
    @abstractmethod
    def square(selfself):
        #виртуальный метод вычисления площади
        pass