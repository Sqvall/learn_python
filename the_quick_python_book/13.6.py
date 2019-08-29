import mio


def main():
    mio.capture_output("myfile.txt")  # Инициализируем, отрываем файл и перенаправляем вывод в него
    print("hello")
    print(1 + 3)
    mio.restore_output()  # Отменяем вывод, закрываем файл

    mio.print_file("myfile.txt")  # Читаем содержимое файла


if __name__ == '__main__':
    main()
