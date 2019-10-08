import threading

print(threading.active_count())
current = threading.current_thread()
print(current.getName())
print(current.is_alive())
# что произойдет, если попробуем ещё раз его запустить
try:
    current.start()
except RuntimeError as error:
    print(f'ERROR: {error}')
current.setName('SuperThread')
print(current.getName())

# На самом деле setName - это просто старый интерфейс.
# в реальных задачах вы смело можете работать напрямую с атрибутом name
current.name = 'SuperThread1'
print(current.name)
print(current.getName())

# Вывод всех запущенных и живых трэдов
print(threading.enumerate())

# Напишем пример для демонстрации потокобезопасного хранилища данных.
thread_data = threading.local()
thread_data.value = 5


def print_results():
    print(threading.current_thread())
    print(f'Result: {thread_data.value}')


def counter(started, to_value):
    print(hasattr(thread_data, 'value'))
    thread_data.value = started
    for i in range(to_value):
        thread_data.value += 1
    print_results()


task1 = threading.Thread(target=counter, args=(0, 10), name='Task1')
task2 = threading.Thread(target=counter, args=(100, 3), name='Task2')
task1.name = 'task1'
task2.name = 'task2'

task1.start()
task2.start()

counter(20, 5)
print_results()

task1.join()
task2.join()
print_results()
