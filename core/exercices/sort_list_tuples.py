# Write a Python function to sort a list of tuples by the second value.

def get_second_value(tuple):
    return tuple[1]

def sort_by_second(tuples):
    tuples.sort(key=get_second_value)
    return tuples



print(sort_by_second([(1, 3), (2, 1), (3, 2)]))  # Output: [(2, 1), (3, 2), (1, 3)]