# Итератор для удаления дубликатов
class UniqueClass:
    #конструктор, принимающий кименованные значения
    def __init__(self, items, **kwargs):
        if 'ignore_case' in kwargs.keys(): #обработка ignore_case
            self.ignore_case = kwargs['ignore_case']
        else:
            self.ignore_case = False
        items=sorted(items) 
        self.__it=iter(items)
        self.__seen=set()


    def __next__(self):
        while True:
            next_item=next(self.__it)
            if self.ignore_case and isinstance(next_item, str):
                seen2=set()
                for x in self.__seen.copy():
                    seen2.add(x.lower())
                if next_item.lower() not in seen2:
                    self.__seen.add(next_item)
                    return next_item
            elif next_item not in self.__seen:
                    self.__seen.add(next_item)
                    return next_item


    def __iter__(self):
        return self
'''
if __name__ == '__main__':
    data1=['dDDdDa',"AAA", 'bbb', 'aaa', 'CCccC', 'aaa', 'ccccc']
    data2=[8,7,7,1,1,2,1,3,4,5,6]
    for u in UniqueClass (data1, ignore_case=True):
        print (u,end=' ')
    print('\n')
    for u in UniqueClass (data1):
        print (u,end=' ')
    print('\n')
    for u in UniqueClass (data2):
        print (u, end=' ')


'''