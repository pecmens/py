from functools import reduce

'''
1.map How to use
'''

### other method

list_m = [i for i in range(12)]

# list_m = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

list_m_n = [j * 2 for j in list_m]

# list_m_n = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]


### map method

list_m_m = list(map(lambda x: x * 2, list_m))

# list_m_m = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]


'''
2.filter How to use
'''

### other method

list_f = [k for k in range(24)]

# list_f = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]

list_f_n = [l for l in range(24) if l % 2 == 0]

# list_f_n = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]


###  filter method

list_f_f = list(filter(lambda x: x % 2 == 0, list_f))

# list_f_f = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]


'''
3. reduce How to use
'''

### other method

list_r = [m for m in range(20)]

# list_r = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

temp = 0

for n in range(20):
    temp += n

list_r_total = temp

# list_r_total = 190


### reduce method

list_r_r = reduce(lambda x, y: x + y, list_r)

# list_r_r = 190




