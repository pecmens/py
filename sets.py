def sets(a1, a2):
    arr = []
    for i in a1:
        for j in a2:
            if i == j:
                arr.append(i)
    
    # for x in range(len(arr) - 1):
    #     for y in range(len(arr) - 1):
    #         if arr[x] == arr[y]:
    #             del arr[x]
    # print(arr)

    return arr

def sets1(a1, a2):
    arr = []
    for i in a1:
        if i not in a2:
            arr.append(i)

    for j in a2:
        if j not in a1:
            arr.append(j)
    return arr

def sets2(a1, a2):
    arr = []
    for i in a1:
        arr.append(i)

    for j in a2:
        if j not in a1:
            arr.append(j)

    return arr


def sets3(a1, a2):
    arr = []
    for i in a1:
        if i not in a2:
            arr.append(i)

    return arr




num1 = [1, 7, 9, 4]
num2 = [3, 2, 4, 9]
# print(sets(num1, num2))
# print(sets1(num1, num2))
# print(sets2(num1, num2))
# print(sets3(num1, num2))

def sor(arrays):
    print(arrays)
    for i in range(len(arrays)):
        for j in range(len(arrays)):
            if i != j:
                if arrays[i] < arrays[j]:
                    arrays[i], arrays[j] = arrays[j], arrays[i]
                    print(arrays[i])
                    print(arrays[j])
                    print(i)
                    print(j)
                    print(arrays)

    return arrays

print(sor(sets2(num1, num2)))
