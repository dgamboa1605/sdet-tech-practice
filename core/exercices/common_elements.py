# Write a Python function to find common elements between two lists.
def common_elements(list1, list2):
    result = []
    for i in list1:
        if i in list2:
            result.append(i)
    
    return result

print(common_elements([1, 2, 3], [2, 3, 5]))

def common_elements2(list1, list2):
    return list(set(list1) & set(list2))

print(common_elements2([1, 2, 3], [2, 3, 4]))