from typing import TypeVar, List, Tuple, Sequence, Iterable

IntFloatStr = TypeVar('IntFloatStr', int, str, float)


def copy_list(sequence: Iterable[IntFloatStr]) -> List[IntFloatStr]:
    new_list: List[IntFloatStr] = []
    for elem in sequence:
        new_list.append(elem)
    return new_list


def copy_list2(sequence: Iterable[Tuple[str, IntFloatStr]]) -> List[IntFloatStr]:
    new_list: List[IntFloatStr] = []
    for elem in sequence:
        new_list.append(elem[1])
    return new_list


test_data = [
    ('1', 10),
    ('1', 10),
    ('1', '1'),
]

test_value0 = copy_list2(test_data)
test_value1 = copy_list([1, 2, 3])
test_value2 = copy_list([1, 2, 9])
test_value3 = copy_list([1.3, 2.1, 3])
test_value4 = copy_list(["srt", "rts", "str"])
test_value5 = copy_list(("srt", "rts", "str"))
test_value6 = copy_list({"srt", "rts", "str"})
print(test_value0)
print(test_value1)
print(test_value3)
