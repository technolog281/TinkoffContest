import sys

list_of_lifts = []
start_stage_list = []
max_floor_list = []
num_of_chain = 0
current_floor = 0

lift_amount = int(input())
if 1 >= lift_amount <= 10**5:
    sys.exit('Кол-во лифтов не может быть меньше (или равно) 1 и больше (или равно) 10^5')


for i in range(1, lift_amount + 1):
    list_of_lifts.append(input().split(' '))

for every in list_of_lifts:
    start_stage_list.append(every[0])

for every in list_of_lifts:
    max_floor_list.append(every[1])

max_floor = max(max_floor_list)
start_floor_index = start_stage_list.index(min(start_stage_list))
current_floor = list_of_lifts[start_floor_index][1]
list_of_lifts.pop(start_floor_index)
num_of_chain += 1


while current_floor < max_floor:
    temp_list = []
    next_floor_list = []
    for every_lift in list_of_lifts:
        if current_floor == every_lift[0]:
            temp_list.append(every_lift)
    remove_list = []
    for al in temp_list:
        next_floor_list.append(al[1])
    min_floor = min(next_floor_list)
    remove_list.append(current_floor)
    remove_list.append(min_floor)
    current_floor = min_floor
    list_of_lifts.remove(remove_list)
    num_of_chain += 1

print(num_of_chain)

