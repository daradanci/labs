from operator import itemgetter

# выводится название улицы, номер здания на этой улице и количество работающих в здании людей
def taskA1(one_to_many:list):
    return [i for i in sorted(one_to_many, key=itemgetter(0))]

# создание списка улиц, которые участвуют в связях со зданиями.
# вывод суммарного числа работников в зданиях на каждой улице
def taskA2(one_to_many:list):
    res=[]
    filled_streets = set([s_name for s_name, num, people in one_to_many])
    # перебор этого списка
    for s in filled_streets:
        sum = 0
        # поиск в списке связей зданий, расположенных на текущей улице, и подсчёт людей, в них работающих
        for s_name, num, people in one_to_many:
            if s == s_name:
                sum += people
        res.append((s, sum))
    return sorted(res, key=itemgetter(1), reverse=True)

# вывод проспектов и номеров зданий на них
def taskA3(many_to_many: list):
    #выбирается слово, искомое в названиях улиц.
    str_to_find='пр-кт' #по заданию - поиск проспектов
    #формируется список проспектов, участвующих в отношениях
    prospects=[s_name for s_name, num, people in many_to_many if s_name.find(str_to_find)!=-1]
    #создаётся словарь, ключ - название проспекта, значение - список номеров домов, расположенных на этих улицах
    return {pr:sorted([num for s_name, num, people in many_to_many if pr==s_name]) for pr in prospects }