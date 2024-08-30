# Write a Python function to find the second largest number in a list.

def second_largest_number(numbers):
    result = sorted(numbers)[::-1]
    return result[1]

print(second_largest_number([1, 2, 6, 4]))
print(second_largest_number([1, 2, 3, 4, 5]))

def second_largest(numbers):
    unique_list = list(set(numbers))
    unique_list.sort()
    return unique_list[-2]

print(second_largest([1, 2, 6, 4]))
print(second_largest([1, 2, 3, 4, 5]))