dict = {}
with open('moby_01_clean.txt') as f:
    for line in f:
        x = line.strip()
        dict[x] = dict.get(x, 0) + 1
word_list = list(dict.items())
word_list.sort(key=lambda x: x[-1])
x = word_list[:]
x.reverse()

print(x[:5], word_list[:5], sep='\n')
