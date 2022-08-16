import sys

years = int(input())
if 1 >= years <= 10**3:
    sys.exit('Количество лет не может быть меньше (или равно) 1 и больше (или равно), чем 10^3')
else:
    pass

list_of_names = []
for i in range(1, years + 1):
    name_str = input().split(' ')
    for every in name_str:
        if len(every) > 10:
            sys.exit('Длина имени ' + every + ' превышает 10 символов')
    list_of_names.append(name_str)

new_list_of_names = []

for ever in list_of_names:
    new_ever = sorted(ever)
    new_list_of_names.append(" ".join(map(str, new_ever)))

maximal_name = max(set(new_list_of_names), key=lambda x: new_list_of_names.count(x))
print(new_list_of_names.count(maximal_name))
