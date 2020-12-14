from random import randint
import time

ls = list()


def md(nn):
    if nn == 0:
        return ls
    else:
        ri = randint(1, 65535)
        ls.append(ri)
        # print(ls)
        return md(nn - 1)


def sets(ls):
    lis = set(ls)
    return list(lis)


def qs(ls):
    if not ls:
        return []
    else:
        m = ls[0]
        l = qs([x for x in ls[1:] if x < m])
        u = qs([y for y in ls[1:] if y >= m])
        return l + [m] + u


print(qs(sets(md(700))))
print(len(set(md(700))))
# print(md(500))
