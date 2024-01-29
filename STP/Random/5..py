list = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
new_list = []

for i in list:
    for j in list2:
        new = i * j
        new_list.append(new)

print(new_list)
