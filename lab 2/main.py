import numpy as np
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square


def main():
    rect=Rectangle("синего", 6, 6)
    circ=Circle('зелёного', 6)
    squa=Square('красного', 6)

    ar = np.array([rect, circ, squa])
    print (ar[0:3])



if __name__ == "__main__":
    main()
