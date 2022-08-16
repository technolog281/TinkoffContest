from functools import reduce

list_of_inputs = input().split(' ')


def rate_calc(input_list):
    int_list = list(map(lambda i: int(i), input_list))
    if int_list[3] > int_list[1]:
        overrate = reduce(lambda d, b: int_list[3] - int_list[1], int_list)
        overrate_price = reduce(lambda x, c: overrate * int_list[2], int_list)
        result_rate = reduce(lambda a, y: overrate_price + int_list[0], int_list)
        return result_rate
    else:
        return int_list[0]


print(rate_calc(list_of_inputs))
