def getID():
    ids = input('Please input you IDs number:')
    if len(ids) != 17:
        while True:
            ids = input('Please type right IDs Number(17bit):')
            if len(ids) != 17:
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


def run():
    
    ids = getID()

    check(ids)

    print(ids + str(check(ids)))


if __name__ == '__main__':
    run()