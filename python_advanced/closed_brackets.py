def check_brackets(my_string):
    my_list = []
    for i in my_string:
        if i == '(':
            my_list.append(i)
        elif i == ')':
            if my_list and my_list[-1] == '(':
                my_list.pop()
            else:
                my_list.append(i)

        if i == '[':
            my_list.append(i)
        elif i == ']':
            if my_list and my_list[-1] == '[':
                my_list.pop()
            else:
                my_list.append(i)

        if i == '{':
            my_list.append(i)
        elif i == '}':
            if my_list and my_list[-1] == '{':
                my_list.pop()
            else:
                my_list.append(i)

    if my_list:
        print('String NOT valid')
    else:
        print('String is valid!!!')


test_1 = '()()({}()hello world)'
test_2 = '{}{{[{()'
test_3 = '{()()({}()hello world)}'
test_4 = '{()}()({}()hello world)}'
test_5 = '{({{}})}'

check_brackets(test_1)
check_brackets(test_2)
check_brackets(test_3)
check_brackets(test_4)
check_brackets(test_5)
