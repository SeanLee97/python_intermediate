matrix = 'ABCESFCSADEE'
mat = []
n = 0
item = []
for x in matrix:
    n += 1
    if n % 4 == 0 and len(item) > 0:
        item.append(x)
        mat.append(item)
        item = []
        n = 0
    else:
        item.append(x)

print(mat)
