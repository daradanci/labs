import json
import sys
from print_result import print_result
import cm_timer
from unique import UniqueClass as uniqum
from gen_random import gRand
path = "data_light.json"


with open(path,'r', encoding='utf-8') as f:
    data = json.load(f)


def IT_filter(el):
    if el['job-name'][0:11].lower()=='программист':
        return True
    else:
        return False


@print_result
def f1(arg):
    return [u for u in uniqum([el.get('job-name') for el in arg], ignore_case=True)]
@print_result
def f2(arg):
    return list(filter(lambda el: el[0:11].lower()=='программист', arg))

@print_result
def f3(arg):

   return list(el+' с опытом Python' for el in arg)

@print_result
def f4(arg):
    zipped=list(zip(arg, gRand(len(arg),100000,200000)))
    return [x+' с зарплатой '+str(y) for x,y in zipped]

if __name__ == '__main__':
    with cm_timer.cm_timer_1():
        f4(f3(f2(f1(data))))
