a = [['Петя', 10, 130, 35], ['Вася', 11, 135, 39], ['Женя', 9, 140, 33], ['Дима', 10, 128, 30]]

n = input('Сортировать по имени (1), возрасту (2), росту (3), весу (4): ')
n = int(n) - 1

t = input('По возрастанию (1), по убыванию (2): ')
if t == '1':
    t = False
elif t == '2':
    t = True

# def sort_col(my_list):
#     return my_list[n]
#
# a.sort(key=sort_col)

a.sort(key=lambda my_list: my_list[n], reverse=t)

print("%7s %7s %4s %3s" % ('Имя', 'Возраст', 'Рост', 'Вес'))

for i in a:
    print("%7s %7d %4d %3d" % (i[0], i[1], i[2], i[3]))
