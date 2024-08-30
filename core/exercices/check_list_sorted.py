# Write a Python function to check whether a list is sorted in ascending order.
def check_list(numbers):
    return numbers == sorted(numbers)

print(check_list([1, 2, 3]))
print(check_list([1, 3, 2]))