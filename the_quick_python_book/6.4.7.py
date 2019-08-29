x = ['"abc"', 'def', '"ghi"', '"klm"', 'nop']
y = []
for i in x:
    i = i.strip('"')
    y += [i]
print(y)

z = ''.join(x)
z = z.replace('"', ' ')
z = z.split()
print(z)

q = 'Mississippi'
v = q.rfind('p')
w = list(q)
del(w[v])
w = ''.join(w)
print(w)
