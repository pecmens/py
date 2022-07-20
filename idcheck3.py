from re import I


def getID():
    ids = input('Please input you IDs number:')
    if len(ids) != 17 or int(ids[6:10]) > 2022 or int(ids[6:10]) < 1920 or int(ids[10:12]) > 12 or int(ids[10:12]) == 00 or int(ids[12:14]) == 00 or int(ids[12:14]) > 31:
        while True:
            ids = input('Please type right IDs Number(17bit):')
            if len(ids) != 17 or int(ids[6:10]) > 2022 or int(ids[6:10]) < 1920 or int(ids[10:12]) > 12 or int(ids[10:12]) == 00 or int(ids[12:14]) == 00 or int(ids[12:14]) > 31:
                continue
            elif ids.isdigit():
                break
            else:
                continue
    
    return ids


def check(ids):
    xsl = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]

    modsl = [1, 0, 'x', 9, 8, 7, 6, 5, 4, 3, 2]

    idss = [int(z) for z in ids]

    suml = [a * b for a, b in zip(xsl, idss)]

    sums = sum(suml) % 11

    totel = modsl[sums]

    return totel


def myids(ids):

    mydisinfo = ids

    if int(mydisinfo[-1]) % 2 == 0:
        sexual = 'Female'
    else:
        sexual = 'Male'

    return sexual


def mybirthday(ids):

    mybirthdays = ids

    date = f'{mybirthdays[6:10]} - {mybirthdays[10:12]} - {mybirthdays[12:14]}'

    return date



def run():
    
    ids = getID()

    print(ids + str(check(ids)))

    print(myids(ids))

    print(mybirthday(ids))


if __name__ == '__main__':
    run()