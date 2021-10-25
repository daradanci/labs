class FigureColor:
    #класс цвет фигуры
    def __init__(self):
        self._color=None

    @property
    def colorproperty(self):
        #геттер
        return self._color

    @colorproperty.setter
    def colorproperty(self,value):
        #сеттер
        self._color=value
