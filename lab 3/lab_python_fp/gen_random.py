# задача 2

import random as rd
#рандомайзер n чисел от a до b
def gRand(num_count, begin, end):
    return [rd.randint(begin, end) for i in range(num_count)]

'''if __name__ == '__main__':

    print(gRand(10,2,5))
    print(gRand(5,1,3))'''
