def concat_sequence_v1(s1, s2):
    for elem in s1:
        yield elem
    yield 'sep'
    for elem in s2:
        yield elem


def concat_sequence_v2(s1, s2):
    yield from s1
    yield 'sep'
    yield from s2


seq1 = range(10)
seq2 = range(0, 20)
result = concat_sequence_v1(seq1, seq2)

print('Seq 1')
print(list(result))


seq1 = range(10)
seq2 = range(0, 20)
result = concat_sequence_v2(seq1, seq2)

print('Seq 2')
print(list(result))
