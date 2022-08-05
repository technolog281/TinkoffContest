incisions = int(input('Введите кол-во частей рулета: '))


def roll(inc):
    cut_num = 0
    pieces = 1
    while pieces < inc:
        cut_num += 1
        pieces *= 2
    return cut_num


print(roll(incisions))
