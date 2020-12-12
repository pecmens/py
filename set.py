import ast


a = [x for x in range(1,1001) if x % 170 == 0]
b = [y for y in range(100,1001) if y % 410 == 0]
ca = len(set(a) & set(b))
cl = [set(a) & set(b)]
ast1 = set(a)
bst1 = set(b)
ca1 = len(ast1 & bst1)
cal = [ast1 & bst1]
print(ca)
print(ca1)
print(cal)
print(cl)
if ca == ca1:
    print('Yes!')
else:
    print('No!')