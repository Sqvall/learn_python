with open('moby_01.txt') as f:
    line = f.read().split('\n')
    x = [i.translate(str.maketrans('-,!?\n.', '      ')) for i in line]
    xq = ''.join(x).split()
    print(f"Строк: {len(line)}\nСлов: {len(xq)}\nСимволов {len(''.join(xq))}")
