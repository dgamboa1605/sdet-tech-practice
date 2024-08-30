def find_max(list):
    aux = list[0]
    for i in list:
        if i > aux:
            aux = i
    return aux

print(find_max([2, 3, 6, 7, 2, 10, 25, 3, 5]))

def find_max2(list):
    return max(list)

print(find_max2([2, 3, 6, 7, 2, 10, 25, 3, 5]))