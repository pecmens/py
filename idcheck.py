xsl = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]

modsl = [1, 0, 'x', 9, 8, 7, 6, 5, 4, 3, 2]

ids = '21010419860731282'

idss = [int(z) for z in ids]

# print(len(idss))

suml = [a * b for a, b in zip(xsl, idss)]

sums = sum(suml)

sumss = sums % 11

totel = modsl[sumss]

print(totel)
print(ids + str(totel))

