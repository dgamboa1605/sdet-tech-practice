def sum_list(list):
    result = 0
    for i in list:
        result += i
    
    return result

print(sum_list([1, 2, 3]))


def sum_list2(list):
    return sum(list)

print(sum_list2([1, 2, 3]))