first_str = input().split(' ')
second_str = input().split(' ')

list_of_x = [first_str[0], first_str[2], second_str[0], second_str[2]]
list_of_y = [first_str[1], first_str[3], second_str[1], second_str[3]]

min_x = min(list_of_x)
max_x = max(list_of_x)
min_y = min(list_of_y)
max_y = max(list_of_y)

dif_x = int(max_x) - int(min_x)
dif_y = int(max_y) - int(min_y)

list_of_change = [dif_y, dif_x]

result_square = max(list_of_change) ** 2

print(result_square)

