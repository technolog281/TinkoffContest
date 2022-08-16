from functools import reduce
import sys


def input_values():
    try:
        first_str = input().split(' ')
        inst_first_str = list(map(lambda i: int(i), first_str))
        if inst_first_str[0] >= 2:
            pass
        elif inst_first_str[1] <= 100:
            pass
        else:
            sys.exit('Условия не соблюдены')
        second_str = input().split(' ')
        inst_second_str = list(map(lambda i: int(i), second_str))
        if inst_first_str[0] != len(inst_second_str):
            sys.exit('Условия не соблюдены')
        else:
            pass
        for w in inst_second_str:
            if w > 100:
                sys.exit('Условия не соблюдены')
        three_str = input().split(' ')
        inst_three_str = list(map(lambda i: int(i), three_str))
        return inst_three_str, inst_second_str, inst_first_str
    except ValueError:
        print('Пожалуйста, введите числовые значения')



