import time

class cm_timer_1:

    def __init__(self):
        self.start_time=time.time()

    def __enter__(self):
        # Должен возвращаться значимый объект
        # например, открытый файл
        return 0

    def __exit__(self, exp_type, exp_value, traceback):
        if exp_type is not None:
            print(exp_type, exp_value, traceback)
        else:
            print('time=' + str(time.time() - self.start_time))


from contextlib import contextmanager
@contextmanager
def cm_timer_2():
    start_time=time.time()
    yield 0
    print('time='+str(time.time()-start_time))



'''if __name__ == '__main__':
    with cm_timer_1():
        time.sleep(5.5)

    with cm_timer_2():
        time.sleep(5.5)'''