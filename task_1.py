list_of_inputs = [int(input('Абонентская плата: ')), int(input('Размер трафика в тарифе (в Мб): ')),
                  int(input('Стоимость доп. мегабайта: ')), int(input('Запланированный трафик (в Мб): '))]


def rate_calc(loi):
    if loi[3] >= loi[1]:
        result_rate = loi[0] + loi[2] * (loi[3] - loi[1])
    else:
        result_rate = loi[0]
    return result_rate


print(rate_calc(list_of_inputs))
