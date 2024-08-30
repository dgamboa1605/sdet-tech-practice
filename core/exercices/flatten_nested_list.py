# Write a Python function to flatten a nested list.
# print(flatten([1, [2, [3, 4], 5], 6]))  # Output: [1, 2, 3, 4, 5, 6]

def flatter_list(numbers):
    result = []
    for i in numbers:
        if isinstance(i, list):
            result.extend(flatter_list(i))
        else:
            result.append(i)
    return result

print(flatter_list([1, [2, [3, 4], 5], 6]))
