from lab_python_oop.figure import Figure
from lab_python_oop.color import FigureColor

class Rectangle(Figure):
    #прямоугольник - наследник фигуры

    FIGURE_TYPE="Прямоугольник"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, color_param, width_param, height_param):
        #объект класса FigureColor создаётся здесь для хранения цвета
        self.width=width_param
        self.height=height_param
        self.fc=FigureColor()
        self.fc.colorproperty=color_param

    def square(self):
        #переопределение метода вычисления площади
        return self.width*self.height

    def __repr__(self):
        #объект класса в виде строки
        return '{} {} цвета шириной {}, высотой {} и площадью {}'.format(
            Rectangle.get_figure_type(),
            self.fc.colorproperty,
            self.width,
            self.height,
            self.square()
        )