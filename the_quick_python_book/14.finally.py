import string


class EmptyStringError(Exception):
    pass


punct = str.maketrans('', '', string.punctuation)


def clean_line(line):
    """Изменяет регистр и удаляет знаки препинания"""
    # Выдать исключение, если строка пустая
    if not line.strip():
        raise EmptyStringError()
    # Привести к одному регистру
    cleaned_line = line.lower()

    # Удалить знаки препинания
    cleaned_line = cleaned_line.translate(punct).replace(' ', '')
    return cleaned_line


def count_words(words):
    """Получает очищенный список слов, возвращает словать счётчиков"""
    word_count = {}
    for word in words:
        try:
            count = word_count.setdefault(word, 0)
        except TypeError:
            # Если word не хешируется, перейти к следующему слову
            pass
        word_count[word] += 1
    return word_count


def word_stats(word_count):
    """Получает словарь счётчиков и возвращает верхние и нижние пять элементов"""
    word_list = list(word_count.items())
    word_list.sort(key=lambda x: x[1])
    try:
        least_common = word_list[:5]
        most_common = word_list[-1:-6:-1]
    except IndexError as e:
        # Усли список пустой или слишком короткий, просто вернуть список
        least_common = word_list
        most_common = list(reversed(word_list))

    return most_common, least_common


cl = clean_line('ASDasda,/uiopuiopuiol.uilui,xcv/><c\'aasdfaluiln.nm,vncxcvx\
                asdasd asdasda as as as as as as as as s[uiopuiopuiopadsfadsfv\'asdgasdgasdgafgsgv,\'asgsadgasgd\]')

print(word_stats(count_words(cl)))
