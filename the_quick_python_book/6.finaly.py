with open('moby_01.txt') as infile, open('moby_01_clean.txt', 'w') as outline:
    for line in infile:
        x = line.lower()
        y = x.translate(str.maketrans(',.-', '   ')).split()
        for i in y:
            outline.write(f'{i}\n')
