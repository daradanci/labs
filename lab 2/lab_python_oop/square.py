from lab_python_oop.rectangle import Rectangle

class Square (Rectangle):
    FIGUTE_TYPE= "Квадрат"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGUTE_TYPE

    def __init__(self, color_param, side_param):
        self.side=side_param
        Rectangle.__init__(self,color_param, self.side, self.side)

    def __repr__(self):
        return  '{} {} цвета со стороной {} и площадью {}'.format(
            Square.get_figure_type(),
            self.fc.colorproperty,
            self.side,
            self.square()
        )