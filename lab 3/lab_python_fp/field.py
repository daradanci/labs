
# задача 1
def field2(items, *args):
    result, temp = [], {}
    for item in items:
        for arg in args:
            if (arg in item):
                temp[arg]=item[arg]
        if len(temp)>0:
            result.append(temp.copy())
            temp.clear()
        yield result
#генератор
def field(items, *args):
    if len(args)==1:
        for item in items:
            if (item.get(args[0])!=None):
                yield item.get(args[0])
    elif len(args)>1:
        result={}
        for item in items:
            for arg in args:
                if item.get(arg)!=None:
                    result[arg]=item.get(arg)
            if len(result)>0:
                yield result
            result.clear()


def field1(items, *args):
    return [{arg: item[arg] for arg in args if arg in item} for item in items]



if __name__ == '__main__':
    goods = [
        {'title': 'ковёр', 'price': '2000', 'color': 'зелёный'},
        {'title': 'диван для отдыха', 'color': 'черный'},
        {'title': 'кресло', 'price': '5000', 'color': 'розовый'},
        {'name': 'обезьяна'}
    ]

    for i in field(goods,'color','title','price'):
        print(i)



