# Write a Python function to remove duplicates from a list.
def remove_duplicates(list):
    result = []
    for i in list:
        if i not in result:
            result.append(i)
    
    return result

print(remove_duplicates([2, 2, 1, 5, 4]))
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))

def remove_duplicates2(list1):
    return list(set(list1))

print(remove_duplicates2([2, 2, 1, 5, 4]))
print(remove_duplicates2([1, 2, 2, 3, 4, 4, 5]))